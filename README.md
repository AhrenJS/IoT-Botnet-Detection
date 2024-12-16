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
2. Create and activate a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use venv\Scripts\activate
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt

## Usage
After installation, you can train and evaluate the model by running:
```bash
python train.py
```
Make sure the dataset is in the /data folder. The script will preprocess the data, train the model, and evaluate it.

## Model Architecture
The model uses a **Sequential Neural Network** with the following layers:
- **Input Layer**: Accepts preprocessed network traffic features.
- **Hidden Layers**: Three dense layers with 512, 256, and 128 neurons, each with **ReLU** activation and **L2 regularization**.
- **Dropout Layers**: Dropout (0.3) after each hidden layer to prevent overfitting.
- **Output Layer**: A softmax layer with three outputs corresponding to the three classes: **Benign**, **Torii**, and **Mirai**.

## Results
The model achieved **perfect classification performance** across all classes:
- **Precision (Benign)**: 1.00
- **Precision (Torii)**: 1.00
- **Precision (Mirai)**: 1.00
- **Recall (Benign)**: 1.00
- **Recall (Torii)**: 1.00
- **Recall (Mirai)**: 1.00
- **F1-Score (Benign)**: 1.00
- **F1-Score (Torii)**: 1.00
- **F1-Score (Mirai)**: 1.00
