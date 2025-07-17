# IoT Botnet Detection

## Overview
This repository contains the source code for an **Artificial Neural Network (ANN)** model designed to detect botnet activity within Internet of Things (IoT) devices. The model is trained on network traffic data and classifies IoT traffic as benign or malicious, detecting attacks such as **Mirai**, **Torii**, and other botnets. Future work will require testing with live traffic and larger datasets, which is limited in this research due to hardware limitations.

## Technologies
The following technologies are used in this project:
- **Python 3.8+**
- **TensorFlow** and **Keras** for deep learning
- **scikit-learn** for data preprocessing, evaluation metrics, and classification tasks
- **pandas**, **NumPy**, and **matplotlib** for data handling and visualization
- **imblearn** for resampling techniques (RandomOverSampler)

## Model Architecture
The model uses an **Artificial Neural Network** with the following layers:
- **Input Layer**: Accepts preprocessed network traffic features.
- **Hidden Layers**: Three dense layers with 512, 256, and 128 neurons, each with **ReLU** activation and **L2 regularization**.
- **Dropout Layers**: Dropout (0.3) after each hidden layer to prevent overfitting.
- **Output Layer**: A softmax layer with the number of outputs corresponding to the number of botnet classes.

## Results
The model achieved **high classification performance** across all classes:
- **Accuracy**: 99.78%
- **Precision**: 99.75%
- **Recall**: 99.74%
- **F1-Score**: 99.75%