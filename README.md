Overview
This repository contains the source code for an Artificial Neural Network (ANN) model designed to detect botnet activity within Internet of Things (IoT) devices. The model is trained on network traffic data, and it classifies IoT traffic as benign or malicious (specifically identifying attacks such as Mirai and Torii botnets).

Technologies
Python 3.8+
TensorFlow and Keras for deep learning
scikit-learn for data preprocessing, evaluation metrics, and classification tasks
pandas, NumPy, and matplotlib for data handling and visualization
imblearn for resampling techniques (RandomOverSampler)

Installation
To set up the project and run the model, follow these steps:

Clone this repository:

bash
Copy code
git clone https://github.com/AhrenJS/IoT-Botnet-Detection.git
cd IoT-Botnet-Detection
Create and activate a virtual environment (recommended):

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate
Install the required dependencies:

bash
Copy code
pip install -r requirements.txt
