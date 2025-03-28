#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 14:42:51 2023

@author: user
"""


import pika

# wav file
wav_file_path = "CarSounds_Challenge/carsounds-sm/fan/section_00_source_train_normal_0050_strength_1_ambient.wav"
with open(wav_file_path, 'rb') as f:
    audio_data = f.read()

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='audio_input', durable=True)

channel.basic_publish(exchange='', routing_key='audio_input', body=audio_data, properties=pika.BasicProperties(delivery_mode=2))

connection.close()
