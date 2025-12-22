import streamlit as st
import numpy as np
import pickle

# Load trained models

try:
    with open("linear_model.pkl", "rb") as f:
        linear_model = pickle.load(f)

    with open("lasso_model.pkl", "rb") as f:
        lasso_model = pickle.load(f)
except FileNotFoundError:
    st.error("Model files not found. Please ensure .pkl files are in the directory.")


# App Title

st.set_page_config(page_title="Car Price Predictor", page_icon="🚗")
st.title("🚗 Car Price Prediction App")
st.write("Predict the **selling price** in Bangladeshi Taka (BDT) using trained ML models.")


# User Input Section

col1, col2 = st.columns(2)

with col1:
    model_choice = st.selectbox("Choose a prediction model", ("Linear Regression", "Lasso Regression"))
    year = st.number_input("Manufacturing Year", min_value=1990, max_value=2025, value=2020, step=1)
    present_price = st.number_input("Present Showroom Price (in Lakhs)", min_value=0.0, value=5.0, format="%.2f")
    km_driven = st.number_input("Total Kilometers Driven", min_value=0, value=10000)

with col2:
    fuel = st.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG"])
    seller_type = st.selectbox("Seller Type", ["Individual", "Dealer"])
    transmission = st.selectbox("Transmission Type", ["Manual", "Automatic"])
    owner = st.selectbox("Previous Owners", [0, 1, 2, 3])


# Encoding (Must match your training LabelEncoding)

fuel_map = {"Petrol": 0, "Diesel": 1, "CNG": 2}
seller_map = {"Dealer": 0, "Individual": 1}
transmission_map = {"Manual": 0, "Automatic": 1}


# Prediction Logic

if st.button("🔍 Predict Car Price"):
    
    # Prepare input data
    input_features = np.array([[year, present_price, km_driven,
                                fuel_map[fuel], seller_map[seller_type],
                                transmission_map[transmission], owner]])

    # Select model
    model = linear_model if model_choice == "Linear Regression" else lasso_model

    # Make prediction
    prediction_lakhs = model.predict(input_features)[0]

    # Handle negative prices
    prediction_lakhs = max(0.05, prediction_lakhs)

    # Convert to Bangladeshi Taka (BDT)
    prediction_bdt = prediction_lakhs * 100000  # 1 lakh = 100,000 BDT

    st.divider()
    if prediction_lakhs > 0.05:
        st.balloons()
        st.success(f"### 💰 Estimated Selling Price: BDT {prediction_bdt:,.0f}")
    else:
        st.warning("⚠️ The model suggests this car has very low market value.")
