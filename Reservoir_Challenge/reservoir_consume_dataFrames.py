import asyncio
import aio_pika
import pandas as pd
import json
import httpx  # For sending data to FastAPI

# Dictionary to store DataFrames for each reservoir
reservoir_dataframes = {}

# List of reservoir codes
reservoir_codes = ["SHA", "SNL", "BER", "BUL", "CLE", "DNP", "FOL", "NML", "ORO", "PNF"]

# Initialize an empty DataFrame for each reservoir
for code in reservoir_codes:
    reservoir_dataframes[code] = pd.DataFrame(columns=["date", "value"])

# Queue to track message completion
message_queue = asyncio.Queue()

FASTAPI_URL = "http://127.0.0.1:8000/reservoir-statistics"  # FastAPI endpoint

async def process_message(message: aio_pika.IncomingMessage):
    """Process each message received from RabbitMQ and store it in DataFrame."""
    async with message.process():
        msg_body = message.body.decode()
        row_data = json.loads(msg_body)

        reservoir_code = row_data.get("reservoirCode")
        date = row_data.get("date")
        value = row_data.get("value")

        # Handle NaN or missing values
        try:
            value = float(value) if value not in ["NaN", "None", None] else None
        except ValueError:
            value = None  # Set invalid values to None
        
        # Ensure the reservoir exists in our dictionary
        if reservoir_code in reservoir_dataframes:
            new_row = pd.DataFrame([{"date": date, "value": value}])
            reservoir_dataframes[reservoir_code] = pd.concat([reservoir_dataframes[reservoir_code], new_row], ignore_index=True)

        # Signal that a message has been processed
        await message_queue.put(1)

async def compute_final_statistics():
    """Computes min, max, average, and latest water depth for all reservoirs, then sends data to FastAPI."""
    print("\n--- Final Reservoir Statistics ---")
    statistics = []

    for code, df in reservoir_dataframes.items():
        if not df.empty and df['value'].notna().any():
            min_val = df['value'].min()
            max_val = df['value'].max()
            avg_val = df['value'].mean()
            
            # Convert 'date' column to datetime for sorting
            df['date'] = pd.to_datetime(df['date'])
            latest_depth = df.sort_values(by='date', ascending=False).iloc[0]['value']

            stats = {
                "reservoir_code": code,
                "min_value": round(min_val, 2),
                "max_value": round(max_val, 2),
                "avg_value": round(avg_val, 2),
                "latest_depth": round(latest_depth, 2)
            }
            statistics.append(stats)

            print(f"Reservoir {code}: Min={min_val:.2f}, Max={max_val:.2f}, Avg={avg_val:.2f}, Latest Depth={latest_depth:.2f}")
        else:
            print(f"Reservoir {code}: No valid data received.")

    print("----------------------------------\n")

    # Send the statistics to FastAPI
    async with httpx.AsyncClient() as client:
        response = await client.post(FASTAPI_URL, json=statistics)
        print(f"Sent data to FastAPI. Response: {response.status_code} - {response.text}")

async def consume_from_rabbitMQ():
    """Connect to RabbitMQ and start consuming messages."""
    connection = await aio_pika.connect_robust("amqp://guest:guest@localhost/")
    async with connection:
        channel = await connection.channel()
        
        # Declare queue
        queue = await channel.declare_queue("reservoir_data", durable=True)
        
        print("Waiting for messages...")
        await queue.consume(process_message)

        # Wait for all messages to be processed
        await asyncio.sleep(2)  # Small delay to ensure all messages are processed
        while not message_queue.empty():
            await message_queue.get()

        # Compute final statistics after all messages
        await compute_final_statistics()

# Run the consumer
asyncio.run(consume_from_rabbitMQ())
