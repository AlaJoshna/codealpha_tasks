# ❤️ Heart Disease Prediction System

## 📌 Overview

This project predicts whether a patient is at risk of heart disease using Machine Learning techniques. The model is trained on a heart disease dataset and deployed through an interactive Streamlit web application.

## 🚀 Features

* Data Exploration and Analysis
* Data Preprocessing
* Train-Test Split
* Feature Scaling using StandardScaler
* Logistic Regression Classification
* Model Evaluation using:

  * Accuracy Score
  * Confusion Matrix
  * Classification Report
* Model Saving using Pickle
* Interactive Streamlit Web App

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit
* Jupyter Notebook
* Git & GitHub

## 📊 Model Performance

| Metric    | Value |
| --------- | ----- |
| Accuracy  | 79.5% |
| Precision | 80%   |
| Recall    | 79%   |
| F1-Score  | 79%   |

## 📂 Project Structure

```text
Disease-Prediction-System
│
├── app.py
├── data/
├── models/
│   ├── heart_disease_model.pkl
│   └── scaler.pkl
├── notebooks/
│   └── 01_data_exploration.ipynb
├── src/
│   └── predict.py
├── README.md
└── requirements.txt
```

## ▶️ How to Run

1. Clone the repository

```bash
git clone <repository-url>
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the Streamlit application

```bash
streamlit run app.py
```

## 🎯 Prediction Output

The application predicts:

* ⚠️ Heart Disease Risk: YES
* ✅ Heart Disease Risk: NO

based on patient health parameters.

## 👩‍💻 Author

Joshna Ala

CodeAlpha Machine Learning Internship Project
