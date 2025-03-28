# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 12:48:00 2025

@author: bllanes
"""

from fastapi import FastAPI, WebSocket
from pydantic import BaseModel

# we may want to use another RabbitMQ connection to retrieve the data from data cleaning
"""
import pika
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='cleaned_data_queue', durable=True)
"""

app = FastAPI(
    title="Data Retrieval API",
    description="After data has been cleaned, this API is used to transfer the data to frontend",
    version="0.0.1")

# Define request model (we may need to modify this if we want to get from another queue)
class InputData(BaseModel):
    name: str
    age: int

@app.get("/")
def read_root():
    return {"message": "Welcome Class CMPE 273 - FastAPI is running!"}

@app.post("/process_data/")
def process_data(data: InputData):
    return {"message": f"Hello {data.name}, you are {data.age} years old."}

"""
@app.get("/get_cleaned_data/")
def get_cleaned_data():
    # Fetch the latest cleaned data from RabbitMQ
    body = channel.basic_get(queue="cleaned_data_queue", auto_ack=True)
    if body:
        return {"cleaned_data": body.decode()}
    return {"cleaned_data": None}

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    # WebSocket endpoint for real-time updates.
    await websocket.accept()
    while True:
        body = channel.basic_get(queue="cleaned_data_queue", auto_ack=True)
        if body:
            await websocket.send_text(body.decode())
"""
