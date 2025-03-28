# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 12:48:00 2025

@author: bllanes
"""

from pyAudioAnalysis import audioTrainTest as aT
import numpy as np

# we may want to use another RabbitMQ connection to retrieve the data from data cleaning
import pika

import os
import tempfile
import requests

FASTAPI_URL = "http://localhost:8000/process_data/"

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='audio_input', durable=True)

def callback(ch, method, properties, body):
    # temp file to save audio data
    with tempfile.NamedTemporaryFile(delete=False, suffix='.wav') as tmp_file:
        tmp_file.write(body)
        tmp_file_path = tmp_file.name
        print(f" [x] Saved audio data to {tmp_file_path}")

    c, p, p_nam = aT.file_classification(tmp_file_path, "CarSounds_Challenge/carsounds-sm/motorsoundsmodel",
                                        "gradientboosting")
    n = np.array(p)
    maxindex = np.argmax(n)
    predictedclass = p_nam[maxindex]
    confidence = max(p)
    print("\n\033[1;31;34mPredicted Class:", str.upper(predictedclass))
    print("Confidence =", round(confidence, 5))

    result_data = {
        "predictedclass": predictedclass,
        "confidence": confidence
    }

    # Send the data to FastAPI via POST
    try:
        response = requests.post(FASTAPI_URL, json=result_data)
        if response.status_code == 200:
            print("Successfully sent the result to FastAPI.")
        else:
            print(f"Failed to send data to FastAPI. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error sending POST request: {e}")

    # clean temp file
    os.remove(tmp_file_path)

# fair dispatch (one message a time per worker)
channel.basic_qos(prefetch_count=1)

channel.basic_consume(queue='audio_input',auto_ack=True,on_message_callback=callback)
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
