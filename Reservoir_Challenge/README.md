# CMPE273-Hackathon
![Reservoir DashBoard](https://github.com/16bitsPixel/CMPE273-Hackathon/blob/main/Reservoir_Challenge/resources/Reservoir_Statistics.png)

* **Demo**
  
https://github.com/user-attachments/assets/047e2d4e-12f4-4edb-8393-6a2b2b3c9572

# ReservoirWatch : 



This project is designed to manage, process, and visualize real-time reservoir data using RabbitMQ for messaging, FastAPI for the backend API, and React for the user interface.

The system receives real-time data from various reservoir sensors, processes it, and calculates statistics such as the minimum, maximum, average, and the latest depth for each reservoir. The data is sent to a FastAPI backend, which stores it and provides an API for clients. The frontend is built using React, providing users with a dashboard to view the latest reservoir statistics.

## Architecture

![Reservoir Architecture](https://github.com/16bitsPixel/CMPE273-Hackathon/blob/main/Reservoir_Challenge/resources/Reservoir%20Architecture.png)

## Features

- Real-Time Data Processing:
   - The backend processes incoming data from reservoir sensors via RabbitMQ messages.
- Reservoir Statistics:
    - The system computes the following statistics for each reservoir:
      - Maximum Depth
      - Minimum Depth
      - Average Depth
      - Latest Depth
- Data Handling:
   - Invalid or missing data (e.g. placeholder for missing values) is filtered out and processed correctly.
- React UI:
  - The user interface allows users to view and interact with the real-time statistics of each reservoir.

## Built With

* RabbitMQ: Message broker used to handle incoming sensor data asynchronously.

* FastAPI: Web framework for creating APIs to process and serve reservoir data.

* React: Frontend framework for building a dynamic user interface.

* pandas: Libraries for data manipulation and handling of missing or invalid data.

##  Running
Start the RabbitMQ producer and consumer in separate terminals
```
cd ReservoirChallenge
pip install asyncio aio_pika pandas httpx numpy openpyxl
python reservoir_consume_dataFrames.py
python reservoir_transform_send.py
```
Run the backend FastAPI
```
fastapi dev app.py
```
Start the webapp
```
cd reservoir-dashboard
npm install
npm run dev
```
## Authors

* **Earl Padron**
* **Brandon Llanes**
* **Isla Shi**


