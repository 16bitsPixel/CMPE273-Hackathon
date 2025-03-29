#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 14:42:51 2023

@author: user
"""


import pika
import argparse

# setup argument parser to accept a file path
parser = argparse.ArgumentParser(description="Send an audio file to RabbitMQ")
parser.add_argument('file_path', type=str, help="Path to the WAV audio file")

args = parser.parse_args()

# get the file path from command line
wav_file_path = args.file_path

try:
    with open(wav_file_path, 'rb') as f:
        audio_data = f.read()
    print(f"Successfully read the file: {wav_file_path}")
except FileNotFoundError:
    print(f"Error: The file {wav_file_path} was not found.")
    exit(1)

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='audio_input', durable=True)
channel.basic_publish(exchange='', routing_key='audio_input', body=audio_data, properties=pika.BasicProperties(delivery_mode=2))
connection.close()
