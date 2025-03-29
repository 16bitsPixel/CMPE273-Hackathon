# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 12:48:00 2025

@author: bllanes
"""

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from pydantic import BaseModel
from typing import List
from fastapi.middleware.cors import CORSMiddleware 

app = FastAPI(
    title="Data Retrieval API",
    description="After data has been cleaned, this API is used to transfer the data to frontend",
    version="0.0.1")

origins = [
    "http://localhost:3000/", # React frontend
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allow specific origins
    allow_credentials=True,
    allow_methods=[""],  # Allow all HTTP methods
    allow_headers=[""],  # Allow all headers
)

# Define request model (we may need to modify this if we want to get from another queue)
class ReservoirData(BaseModel):
    reservoir_code: str
    min_value: float
    max_value: float
    avg_value: float
    latest_depth: float

@app.get("/")
def read_root():
    return {"message": "Welcome Class CMPE 273 - FastAPI is running!"}

class SimpleCache:
    def __init__(self):
        self.cache={}
    def set(self,key,value):
        self.cache[key] = value
    def get(self,key):
        return self.cache.get(key, None)
    
cache = SimpleCache()

# store active websocket connections
active_connections = []

@app.get("/")
def read_root():
    return {"message": "Welcome Class CMPE 273 - FastAPI is running!"}

"""
@app.post("/process_data/")
def insert_data_in_cache(data: List[ReservoirData]):
    cache.set("stored_reservoir_data", data)
    return {"message": f"Done! cache insert..."}
"""

@app.post("/process_data/")
async def insert_data_in_cache(data: List[ReservoirData]):
    cache.set("stored_audio_result", data)

    # broadcast data to all websocket clients
    for connection in active_connections:
        await connection.send_json(data.dict())

    return {"message": f"Done! cache insert..."}

"""
@app.get("/retrieve_data/")
def read_from_cache():
    return cache.get("stored_reservoir_data")
"""
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    active_connections.append(websocket)

    try:
        while True:
            await websocket.receive_text()
    except WebSocketDisconnect:
        active_connections.remove(websocket)
