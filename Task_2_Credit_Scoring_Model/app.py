import streamlit as st
import pickle
import pandas as pd

with open("models/credit_scoring_model.pkl", "rb") as file:
    model = pickle.load(file)

with open("models/scaler.pkl", "rb") as file:
    scaler = pickle.load(file)

st.title("💳 Credit Scoring Model")

st.write("Enter applicant details below.")

person_age = st.number_input("Age", 18, 100, 25)
person_income = st.number_input("Income", 0, 1000000, 50000)
person_home_ownership = st.selectbox("Home Ownership", [0,1,2,3])
person_emp_length = st.number_input("Employment Length", 0.0, 50.0, 2.0)
loan_intent = st.selectbox("Loan Intent", [0,1,2,3,4,5])
loan_grade = st.selectbox("Loan Grade", [0,1,2,3,4,5,6])
loan_amnt = st.number_input("Loan Amount", 0, 1000000, 10000)
loan_int_rate = st.number_input("Interest Rate", 0.0, 50.0, 10.0)
loan_percent_income = st.number_input("Loan Percent Income", 0.0, 1.0, 0.2)
cb_person_default_on_file = st.selectbox("Previous Default", [0,1])
cb_person_cred_hist_length = st.number_input("Credit History Length", 0, 50, 5)

if st.button("Predict"):

    data = pd.DataFrame([[person_age,
                          person_income,
                          person_home_ownership,
                          person_emp_length,
                          loan_intent,
                          loan_grade,
                          loan_amnt,
                          loan_int_rate,
                          loan_percent_income,
                          cb_person_default_on_file,
                          cb_person_cred_hist_length]],
                        columns=[
                            "person_age",
                            "person_income",
                            "person_home_ownership",
                            "person_emp_length",
                            "loan_intent",
                            "loan_grade",
                            "loan_amnt",
                            "loan_int_rate",
                            "loan_percent_income",
                            "cb_person_default_on_file",
                            "cb_person_cred_hist_length"
                        ])

    data = scaler.transform(data)

    prediction = model.predict(data)

    if prediction[0] == 1:
        st.error("⚠️ High Credit Risk")
    else:
        st.success("✅ Low Credit Risk")