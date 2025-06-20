# -*- coding: utf-8 -*-
"""stroke_app.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1LiNKazL3Qe2ulPwQMYYKPEQ1ixJiS95r
"""


import streamlit as st
import pandas as pd
import joblib

model = joblib.load("stroke_model.pkl")
encoders = joblib.load("label_encoders.pkl")

# Input fields
import streamlit as st

st.set_page_config(page_title="Stroke Predictor", page_icon="🧠")
st.title("🧠 Stroke Prediction App")
st.markdown("Fill in your health details below to check your stroke risk:")

# 👤 Gender
gender = st.selectbox("👤 Gender", ["Male", "Female", "Other"])

# 🎂 Age
age = st.slider(
    "🎂 Age",
    min_value=0,
    max_value=100,
    value=25,
    step=1,
    help="Drag to select age"
)

# ❤️ Heart Disease
heart_disease = st.selectbox("❤️ Do you have heart disease?", ["No", "Yes"])

# 🍬 Average Glucose Level
avg_glucose_level = st.slider(
    "🍬 Average Glucose Level (mg/dL)",
    min_value=50.0,
    max_value=300.0,
    value=100.0,
    step=0.5,
    help="Normal fasting glucose is below 100 mg/dL"
)

# ⚖️ BMI
bmi = st.slider(
    "⚖️ Body Mass Index (BMI)",
    min_value=10.0,
    max_value=60.0,
    value=22.0,
    step=0.1,
    help="Healthy BMI is between 18.5 and 24.9"
)

# 🚬 Smoking Status
smoking_status = st.selectbox("🚬 Smoking Status", ["never smoked", "formerly smoked", "smokes", "Unknown"])

import joblib
import numpy as np

# Load trained model and label encoders
model = joblib.load("stroke_model.pkl")
encoders = joblib.load("label_encoders.pkl")

# When user clicks the predict button
if st.button("🔍 Predict Stroke"):
    # Encode categorical values using saved encoders
    gender_encoded = encoders['gender'].transform([gender])[0]
    smoking_encoded = encoders['smoking_status'].transform([smoking_status])[0]
    heart_disease_encoded = 1 if heart_disease == "Yes" else 0

    # Prepare input data
    input_data = np.array([[gender_encoded, age, heart_disease_encoded, avg_glucose_level, bmi, smoking_encoded]])

    # Make prediction
    prediction = model.predict(input_data)[0]

    # Show result
    if prediction == 1:
        st.error("⚠️ You may be at risk of stroke. Please consult a doctor.")
    else:
        st.success("✅ You are not likely at risk of stroke.")
if st.button("Predict Stroke Risk"):
    # Encode inputs
    gender_encoded = encoders["gender"].transform([gender])[0]
    smoking_encoded = encoders["smoking_status"].transform([smoking_status])[0]
    heart_disease_bin = 1 if heart_disease == "Yes" else 0

    # Prepare input DataFrame
    input_df = pd.DataFrame([[gender_encoded, age, heart_disease_bin, avg_glucose_level, bmi, smoking_encoded]],
                            columns=["gender", "age", "heart_disease", "avg_glucose_level", "bmi", "smoking_status"])

    # Predict
    prediction = model.predict(input_df)[0]

    # Output
    if prediction == 1:
        st.error("⚠️ High Risk of Stroke!")
    else:
        st.success("✅ Low Risk of Stroke.")
# --- Footer ---
st.markdown("---")
st.markdown("<h4 style='text-align: center;'>❤️ Developed by Godwin ❤️</h4>", unsafe_allow_html=True)
