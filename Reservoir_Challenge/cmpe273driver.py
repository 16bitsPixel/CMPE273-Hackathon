# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 12:48:00 2025

@author: bllanes
"""

# used to locally test the api

import requests

BASE_URL = "http://127.0.0.1:8000"

def invoke_api():
    # Test the root endpoint
    response = requests.get(f"{BASE_URL}/")
    print("Root Response:", response.json())

    # Test the process_data endpoint
    payload = {"name": "John Doe", "age": 30}
    response = requests.post(f"{BASE_URL}/process_data/", json=payload)
    print("Process Response:", response.json())

if __name__ == "__main__":
    invoke_api()
