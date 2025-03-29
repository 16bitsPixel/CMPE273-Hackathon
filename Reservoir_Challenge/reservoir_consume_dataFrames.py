import asyncio
import aio_pika
import pandas as pd
import json
import httpx  # For sending data to FastAPI
import numpy as np  # For handling NaN values

# Dictionary to store DataFrames for each reservoir
reservoir_dataframes = {}

# List of reservoir codes
reservoir_codes = ["SHA", "SNL", "BER", "BUL", "CLE", "DNP", "FOL", "NML", "ORO", "PNF"]

# Initialize an empty DataFrame for each reservoir
for code in reservoir_codes:
    reservoir_dataframes[code] = pd.DataFrame(columns=["date", "value"])

# Queue to track message completion
message_queue = asyncio.Queue()

FASTAPI_URL = "http://localhost:8000/process_data/"  # FastAPI endpoint

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

            # Handle NaN values: replace with None
            min_val = None if np.isnan(min_val) else min_val
            max_val = None if np.isnan(max_val) else max_val
            avg_val = None if np.isnan(avg_val) else avg_val
            latest_depth = None if np.isnan(latest_depth) else latest_depth

            stats = {
                "reservoir_code": code,
                "min_value": round(min_val, 2) if min_val is not None else None,
                "max_value": round(max_val, 2) if max_val is not None else None,
                "avg_value": round(avg_val, 2) if avg_val is not None else None,
                "latest_depth": round(latest_depth, 2) if latest_depth is not None else None
            }
            statistics.append(stats)

            print(f"Reservoir {code}: Min={min_val}, Max={max_val}, Avg={avg_val}, Latest Depth={latest_depth}")
        else:
            print(f"Reservoir {code}: No valid data received.")

    print("----------------------------------\n")

    # Send the statistics to FastAPI
    async with httpx.AsyncClient() as client:
        response = await client.post(FASTAPI_URL, json=statistics)
        print(f"Sent data to FastAPI. Response: {response.status_code} - {response.text}")

async def consume_from_rabbitMQ():
    """Connect to RabbitMQ and start consuming messages."""
    connection = await aio_pika.connect_robust("amqp://guest:guest@localhost/")  # Change to your RabbitMQ server
    async with connection:
        channel = await connection.channel()
        
        # Declare queue
        queue = await channel.declare_queue("reservoir_data", durable=True)
        
        print("Waiting for messages...")

        # Continuously consume messages
        await queue.consume(process_message)

        # Keep the consumer alive and periodically compute statistics
        while True:
            # Wait for some time before computing statistics (e.g., every 10 seconds)
            await asyncio.sleep(10)
            await compute_final_statistics()

# Run the consumer
asyncio.run(consume_from_rabbitMQ())
