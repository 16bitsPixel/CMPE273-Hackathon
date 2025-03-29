# The Problem
A automobile company needs state approval to capture all the safety equipment within their cars. Provided are 10-second audio clips of motor sounds. Using a machine learning model, on an incoming sound clip live update onto a dashboard the machine type the audio recording originated from.

# Objective
A producer-consumer system interacting with a machine learning model to output live updates to a dashboard regarding car part sounds.

# System Architecture
The system consists of RabbitMQ producer-consumer interacting with a FastAPI to send live data updates to the React frontend through webhooks.
![System Architecture](https://github.com/16bitsPixel/CMPE273-Hackathon/blob/main/CarSounds_Challenge/resources/Car%20Sounds%20Architecture.png)

# Dashboard
![Waiting Dashboard](https://github.com/16bitsPixel/CMPE273-Hackathon/blob/main/CarSounds_Challenge/resources/CarDashboard_Waiting.png)

![Notification](https://github.com/16bitsPixel/CMPE273-Hackathon/blob/main/CarSounds_Challenge/resources/CarDashboard_Notification.png)

# Video Demo
https://youtu.be/XkBL8jglOMI  
https://youtu.be/XkBL8jglOMI  
https://youtu.be/XkBL8jglOMI  

https://github.com/user-attachments/assets/defc3fc6-d69e-436e-b816-7b02add52267

# How to Run
Start FastAPI
```
fastapi dev app.py
```

Start the webapp
```
cd carsounds-dashboard
npm install
npm run dev
cd ..
```

Have RabbitMQ running and start the RabbitMQ producer/consumer in separate terminals
```
python receiver.py
python producer.py
```
