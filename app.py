import streamlit as st
import pandas as pd
import numpy as np
import joblib
import tensorflow as tf

#load the trained model
model = tf.keras.models.load_model("livestock_health_model.h5")
scaler = joblib.load("scaler.pkl")

# Streamlit app title
st.title("Livestock Health Predictor")
st.markdown("Enter cow data to predict health status (0 = Sick, 1 = Healthy).")

# Input fields for cow data
temperature = st.number_input("Body Temperature (°C)", min_value=10.0, max_value=100.0, value=38.5)
heart_rate = st.number_input("Heart Rate (bpm)", min_value=40, max_value=150, value=65)
respiration = st.number_input("Respiration Rate (bpm)", min_value=10, max_value=60, value=25)
feed_intake = st.number_input("Feed Intake (kg/day)", min_value=0.0, value=15.0)
rumination = st.number_input("Rumination Minutes (per day)", min_value=0, value=400)
activity = st.number_input("Activity Score", min_value=0, value=7)
water_intake = st.number_input("Water Intake (liters/day)", min_value=0.0, value=80.0)
ambient_temp = st.number_input("Ambient Temperature (°C)", min_value=10.0, value=25.0)
humidity = st.number_input("Humidity (%)", min_value=0.0, value=65.0)
age = st.number_input("Age (months)", min_value=1, value=60)

# Derived features (same as training)
stress_index = heart_rate + temperature
feed_efficiency = activity / (feed_intake + 0.1)
water_feed_ratio = water_intake / (feed_intake + 0.1)
rumination_activity_ratio = rumination / (activity + 0.1)
temp_diff = temperature - ambient_temp

# Combine all features
features = np.array([[age, ambient_temp, humidity, temperature, heart_rate, activity,
                      rumination, feed_intake, water_intake, respiration,
                      stress_index, feed_efficiency, water_feed_ratio, rumination_activity_ratio, temp_diff]])

# Scale the features
features_scaled = scaler.transform(features)

if st.button("Predict Health Status"):
    prediction = model.predict(features_scaled)
    status = "Healthy" if prediction[0][0] > 0.5 else "Sick"
    st.success(f"Predicted Health Status: **{status}** ({prediction[0][0]:.4f})")
    
    
