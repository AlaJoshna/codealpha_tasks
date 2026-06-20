import streamlit as st
import pickle

# Load model
with open("models/heart_disease_model.pkl", "rb") as file:
    model = pickle.load(file)

# Load scaler
with open("models/scaler.pkl", "rb") as file:
    scaler = pickle.load(file)

st.title("❤️ Heart Disease Prediction System")

st.write("Enter patient details below.")

age = st.number_input("Age", 1, 120, 50)

sex_option = st.selectbox("Sex", ["Female", "Male"])

sex = 0 if sex_option == "Female" else 1

cp = st.number_input("Chest Pain Type (cp)", 0, 3, 0)
trestbps = st.number_input("Resting Blood Pressure", 50, 250, 120)
chol = st.number_input("Cholesterol", 100, 600, 200)
fbs_option = st.selectbox(
    "Fasting Blood Sugar",
    ["No", "Yes"]
)

fbs = 1 if fbs_option == "Yes" else 0
restecg = st.number_input("Rest ECG", 0, 2, 1)
thalach = st.number_input("Max Heart Rate", 50, 250, 150)
exang_option = st.selectbox(
    "Exercise Induced Angina",
    ["No", "Yes"]
)

exang = 1 if exang_option == "Yes" else 0
oldpeak = st.number_input("Oldpeak", 0.0, 10.0, 1.0)
slope = st.number_input("Slope", 0, 2, 1)
ca = st.number_input("CA", 0, 4, 0)
thal = st.number_input("Thal", 0, 3, 2)

if st.button("Predict"):

    sample_data = [[
        age, sex, cp, trestbps, chol,
        fbs, restecg, thalach,
        exang, oldpeak, slope,
        ca, thal
    ]]

    sample_data = scaler.transform(sample_data)

    prediction = model.predict(sample_data)

    if prediction[0] == 1:
        st.error("⚠️ Heart Disease Risk: YES")
    else:
        st.success("✅ Heart Disease Risk: NO")