import streamlit as st
import pickle
import pandas as pd
import numpy as np

# Load model and scaler
with open('diabetes_svm_model.pkl', 'rb') as file:
    model = pickle.load(file)

with open('scaler.pkl', 'rb') as file:
    scaler = pickle.load(file)

st.title("Diabetes Prediction Web App")

st.write("Enter patient medical details:")

# Feature inputs
Pregnancies = st.number_input('Pregnancies', min_value=0)
Glucose = st.number_input('Glucose', min_value=0)
BloodPressure = st.number_input('BloodPressure', min_value=0)
SkinThickness = st.number_input('SkinThickness', min_value=0)
Insulin = st.number_input('Insulin', min_value=0)
BMI = st.number_input('BMI', min_value=0.0, step=0.1)
DiabetesPedigreeFunction = st.number_input('DiabetesPedigreeFunction', min_value=0.0, step=0.001)
Age = st.number_input('Age', min_value=0)

# Button to predict
if st.button('Predict'):
    input_data = (Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age)
    
    # Convert to DataFrame
    feature_names = ['Pregnancies','Glucose','BloodPressure','SkinThickness','Insulin','BMI','DiabetesPedigreeFunction','Age']
    input_df = pd.DataFrame([input_data], columns=feature_names)
    
    # Scale
    input_scaled = scaler.transform(input_df)
    
    # Predict
    prediction = model.predict(input_scaled)[0]
    
    # Display result
    if prediction == 0:
        st.success("The person is NOT diabetic")
    else:
        st.error("The person is diabetic")
