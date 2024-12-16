# IoT Botnet Detection

## Overview
This repository contains the source code for an **Artificial Neural Network (ANN)** model designed to detect botnet activity within Internet of Things (IoT) devices. The model is trained on network traffic data and classifies IoT traffic as benign or malicious, detecting attacks such as **Mirai** and **Torii** botnets.

## Table of Contents
- [Overview](#overview)
- [Technologies](#technologies)
- [Installation](#installation)
- [Usage](#usage)
- [Model Architecture](#model-architecture)
- [Results](#results)
- [License](#license)
- [Contributing](#contributing)

## Technologies
The following technologies are used in this project:
- **Python 3.8+**
- **TensorFlow** and **Keras** for deep learning
- **scikit-learn** for data preprocessing, evaluation metrics, and classification tasks
- **pandas**, **NumPy**, and **matplotlib** for data handling and visualization
- **imblearn** for resampling techniques (RandomOverSampler)

## Installation
To set up the project and run the model, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/AhrenJS/IoT-Botnet-Detection.git
   cd IoT-Botnet-Detection
