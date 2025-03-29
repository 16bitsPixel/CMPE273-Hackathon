# -*- coding: utf-8 -*-
"""
Created on Fri Mar 28 12:29:15 2025

@author: Earl Padron
"""
import asyncio
import aio_pika
import pandas as pd
import json

async def read_and_transform(file_path):
    df = pd.read_excel(file_path)
    
    # List to store individual row messages
    row_messages = []

    # Transform each row into a separate JSON object
    for _, row in df.iterrows():
        reservoir_code = row['STATION_ID']
        date = row['DATE TIME']
        value = row['VALUE']
        
        row_message = {
            "reservoirCode": reservoir_code,
            "date": str(date),
            "value": float(value)
        }
        
        row_messages.append(row_message)

    return row_messages

async def send_to_rabbitMQ(file_path):
    # Connect to RabbitMQ
    connection = await aio_pika.connect_robust("amqp://guest:guest@localhost/")
    async with connection:
        channel = await connection.channel()

        # Declare a custom exchange and a durable queue
        exchange = await channel.declare_exchange("reservoir_exchange", type="direct", durable=True)
        queue = await channel.declare_queue('reservoir_data', durable=True)
        await queue.bind(exchange, routing_key="reservoir_data")
        
        # Transform the Excel file
        row_messages = await read_and_transform(file_path)
        
        # Send each row as a separate JSON message
        for row in row_messages:
            message = json.dumps(row)
            await exchange.publish(
                aio_pika.Message(body=message.encode()),
                routing_key="reservoir_data",
            )
            print(f"Sent row: {message}")
            

async def process_all_reservoirs(file_paths):
    """Loops through all reservoir Excel files and sends their data to RabbitMQ."""
    tasks = [send_to_rabbitMQ(file_path) for file_path in file_paths]
    await asyncio.gather(*tasks)  # Run all send tasks concurrently

if __name__ == "__main__":
    reservoir_files = [
        "./resources/SHA_6.xlsx", "./resources/ORO_6.xlsx","./resources/CLE_6.xlsx","./resources/PNF_6.xlsx","./resources/BUL_6.xlsx",
        "./resources/FOL_6.xlsx","./resources/BER_6.xlsx","./resources/DNP_6.xlsx","./resources/SNL_6.xlsx","./resources/NML_6.xlsx"
    ]
    
    asyncio.run(process_all_reservoirs(reservoir_files))