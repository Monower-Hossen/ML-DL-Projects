import streamlit as st
import numpy as np
import pandas as pd
import joblib

# 1️ Load trained model & scaler
# Ensure wine_model.pkl and scaler.pkl are in 'model' folder

model = joblib.load("model/wine_model.pkl")
scaler = joblib.load("model/scaler.pkl")


# 2️ App Title and Description
st.title("🍷 Wine Quality Prediction App")
st.write("Predict wine quality and see if it's Good or Bad")

# 3️ Sidebar: CSV Upload for Batch Prediction

st.sidebar.header("Upload CSV for Batch Prediction")
uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type="csv")

if uploaded_file:
    # Read CSV
    df = pd.read_csv(uploaded_file)
    st.subheader("Uploaded Data")
    st.dataframe(df)

    # Predict for all rows
    features_scaled = scaler.transform(df.values)
    predictions = model.predict(features_scaled)
    df['Predicted_Quality'] = np.round(predictions).astype(int)

    # Add Good/Bad label
    df['Quality_Label'] = df['Predicted_Quality'].apply(lambda x: "Good" if x >= 6 else "Bad")

    st.subheader("Predictions with Labels")
    st.dataframe(df)
    st.success("Batch prediction completed!")

# 4️ Manual Input Section (Using Columns)

st.header("🧪 Test a Single Sample")

if model:
    # Use columns to make the UI look cleaner
    col1, col2, col3 = st.columns(3)
    
    with col1:
        fixed_acidity = st.number_input("Fixed Acidity", 0.0, 20.0, 7.0)
        volatile_acidity = st.number_input("Volatile Acidity", 0.0, 2.0, 0.5)
        citric_acid = st.number_input("Citric Acid", 0.0, 1.0, 0.3)
        residual_sugar = st.number_input("Residual Sugar", 0.0, 20.0, 2.0)

    with col2:
        chlorides = st.number_input("Chlorides", 0.0, 1.0, 0.05)
        free_sulfur = st.number_input("Free Sulfur Dioxide", 0.0, 100.0, 15.0)
        total_sulfur = st.number_input("Total Sulfur Dioxide", 0.0, 300.0, 45.0)
        density = st.number_input("Density", 0.9, 1.1, 0.99)

    with col3:
        ph = st.number_input("pH", 2.0, 5.0, 3.3)
        sulphates = st.number_input("Sulphates", 0.0, 2.0, 0.6)
        alcohol = st.number_input("Alcohol", 5.0, 20.0, 10.5)

    if st.button("Predict Quality", type="primary"):
        # Combine inputs into the correct shape
        features = np.array([[fixed_acidity, volatile_acidity, citric_acid, residual_sugar, 
                             chlorides, free_sulfur, total_sulfur, density, ph, sulphates, alcohol]])
        
        # Transform and Predict
        features_scaled = scaler.transform(features)
        prediction = model.predict(features_scaled)[0]
        score = int(np.round(prediction))
        
        # Display Result
        if score >= 6:
            st.balloons()
            st.success(f"### Result: {score} (Good Wine)")
        else:
            st.warning(f"### Result: {score} (Bad Wine)")


