# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 12:48:00 2025

@author: bllanes
"""

from fastapi import FastAPI, WebSocket
from pydantic import BaseModel

app = FastAPI(
    title="Data Retrieval API",
    description="After data has been cleaned, this API is used to transfer the data to frontend",
    version="0.0.1")

# Audio result to save
class AudioResult(BaseModel):
    predictedclass: str
    confidence: float

class SimpleCache:
    def __init__(self):
        self.cache={}
    def set(self,key,value):
        self.cache[key] = value
    def get(self,key):
        return self.cache.get(key, None)
    
cache = SimpleCache()

@app.get("/")
def read_root():
    return {"message": "Welcome Class CMPE 273 - FastAPI is running!"}

@app.post("/process_data/")
def insert_data_in_cache(data: AudioResult):
    cache.set("stored_audio_result", data)
    return {"message": f"Done! cache insert..."}

@app.get("/retrieve_data/")
def read_from_cache():
    return cache.get("stored_audio_result")
