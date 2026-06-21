# Credit Scoring Model

## Overview

This project predicts whether a loan applicant is a high credit risk or low credit risk using Machine Learning.

## Features

* Data preprocessing and cleaning
* Missing value handling
* Label Encoding for categorical features
* Logistic Regression model
* Model evaluation using Accuracy, Confusion Matrix, and Classification Report
* Streamlit web application for predictions

## Dataset

Credit Risk Dataset containing applicant information such as:

* Age
* Income
* Home Ownership
* Employment Length
* Loan Intent
* Loan Grade
* Loan Amount
* Interest Rate
* Credit History Length

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* Streamlit
* Pickle

## Model Performance

* Accuracy: 83.72%

## Project Structure

Credit_Scoring_Model/
│
├── data/
├── models/
│   ├── credit_scoring_model.pkl
│   └── scaler.pkl
├── notebooks/
│   └── 01_data_exploration.ipynb
├── app.py
├── requirements.txt
└── README.md

## How to Run

Install dependencies:

pip install -r requirements.txt

Run the Streamlit application:

streamlit run app.py

## Author

Joshna Ala
CodeAlpha Machine Learning Internship
