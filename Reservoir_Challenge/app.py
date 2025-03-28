# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 12:48:00 2025

@author: bllanes
"""

from fastapi import FastAPI
from pydantic import BaseModel

# we may want to use another RabbitMQ connection to retrieve the data from data cleaning

app = FastAPI(
    title="Data Cleaning API",
    description="Post/Retrieve",
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
