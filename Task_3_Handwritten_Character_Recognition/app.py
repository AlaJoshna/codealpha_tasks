import streamlit as st
import pickle
import numpy as np

# Load model
with open("models/handwritten_character_model.pkl", "rb") as file:
    model = pickle.load(file)

with open("models/scaler.pkl", "rb") as file:
    scaler = pickle.load(file)

st.title("✍️ Handwritten Character Recognition")

st.write("Enter 64 pixel values separated by commas")

pixel_text = st.text_area(
    "Pixels",
    "0,0,0,0,0,0,0,0," * 8
)

if st.button("Predict"):
    pixels = [float(x) for x in pixel_text.split(",") if x.strip()]

    if len(pixels) != 64:
        st.error("Please enter exactly 64 values.")
    else:
        data = np.array(pixels).reshape(1, -1)
        data = scaler.transform(data)
        prediction = model.predict(data)

        st.success(f"Predicted Digit: {prediction[0]}")