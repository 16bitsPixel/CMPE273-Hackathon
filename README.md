# CMPE273 Spring 2025 Hackathon 
**The repository holds the hackathon project(s) for CMPE273 at SJSU held on 3/28/2025 - 3/29/2025**

## Team Members
- Brandon Llanes
- Earl Pauldron
- Isla Shi

## Folders
Reservoir_Challenge directory holds all files for the California Reservoirs Dashboard project
CarSounds_Challenge directory holds all files for the Car Sounds Dashboard project

# The Problem
After graduation, you joined a high-profile consulting company that collaborates with various industry sectors. Due to the significant demand for scalable enterprise distributed architectures, you were assigned two major projects: one with the State Reservoir Water Department and another with a highly profitable automobile company.

The State Water Department aimed to renew their legacy architecture by implementing a new enterprise distributed architecture. They sought to develop a simple interface for the new system, which would consume existing data sources and reintegrate them into the re-architected framework.

The automobile company planned to obtain state approval and needed to capture all the safety equipment within the car.

Data Sources:CarSoundsAndAudioAnalysis.ipynbDownload CarSoundsAndAudioAnalysis.ipynb

DCASE2021 ChallengeLinks to an external site. data source.

 

California_Water_and_CarSounds_Dashboard_Final_20250328.pdf

Model: 

I have trained motor sound detection model. The dataset is from the Detection and Classification of Acoustic Scenes and Events (DCASE) 2021 Challenge Task 2, focusing on unsupervised anomalous sound detection (ASD) for machine condition monitoring under domain-shifted conditions. It contains normal and anomalous operating sounds of seven types of machines, with each recording being a 10-second single-channel audio clip that includes machine sounds and environmental noise for both industrial and domestic environments .

 

 The seven machine types are fan, gearbox, pump, slide rail, Car, Train, and valve. Unlike the 2020 version, which operated under ideal conditions, the 2021 task addresses real-world complexities where machine operating conditions and environmental noise vary between training and testing phases, leading to domain shift. This shift is exemplified by variations in motor speed and environmental noise across different seasons. The dataset is divided into three sections per machine type, each providing around 1,000 normal sound clips in the source domain for training, three normal clips in the target domain for training, and approximately 100 normal and anomalous clips in both source and target domains for testing. Anomalous sounds were recorded by deliberately damaging machines, and all recordings were single channel. The dataset includes labels for machine type, section index, normal/anomaly status, and additional attributes, with baseline systems available on GitHub to help researchers get started with ASD tasks.

Aston Martin gets neural network - CMPE239_DataMining_Session5_20160927.pdf

I have downloaded audio files from https://dcase.community/challenge2021/task-unsupervised-detection-of-anomalous-sounds#downloadLinks to an external site.

Download  carsounds-sm.zipDownload carsounds-sm.zip

Development dataset  (7.5 GB)Links to an external site.
Additional training dataset  (5.5 GB)Links to an external site.
Evaluation dataset  (2.2 GB)Links to an external site.
