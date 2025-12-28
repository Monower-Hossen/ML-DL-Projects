import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("model/xgb_model.pkl")

st.title("House Price Predictor")

# Required columns
features = [
    "bedrooms","bathrooms","sqft_living","sqft_lot","floors",
    "waterfront","view","condition","sqft_above","sqft_basement",
    "yr_built","yr_renovated"
]

# ================= CSV INPUT =================
st.header("Predict using CSV")

file = st.file_uploader("Upload CSV", type="csv")

if file:
    data = pd.read_csv(file)

    if set(features).issubset(data.columns):
        if st.button("Predict CSV"):
            data["Predicted_Price"] = model.predict(data[features])
            st.dataframe(data)

            st.download_button(
                "Download Result",
                data.to_csv(index=False),
                "house_price_predictions.csv"
            )
    else:
        st.error("CSV columns do not match model features")

# ================= MANUAL INPUT =================
st.header(" Manual Prediction")

col1, col2 = st.columns(2)

with col1:
    bedrooms = st.number_input("Bedrooms", 1, 10, 3)
    bathrooms = st.number_input("Bathrooms", 1, 10, 2)
    sqft_living = st.number_input("Living Area (sqft)", 300, 10000, 1500)
    sqft_lot = st.number_input("Lot Size (sqft)", 300, 50000, 5000)
    floors = st.number_input("Floors", 1, 5, 1)
    waterfront = st.selectbox("Waterfront", [0, 1])

with col2:
    view = st.number_input("View (0-4)", 0, 4, 0)
    condition = st.number_input("Condition (1-5)", 1, 5, 3)
    sqft_above = st.number_input("Above Ground Area", 300, 10000, 1000)
    sqft_basement = st.number_input("Basement Area", 0, 5000, 500)
    yr_built = st.number_input("Year Built", 1800, 2025, 1990)
    yr_renovated = st.number_input("Year Renovated", 0, 2025, 0)

if st.button("Predict Price"):
    input_data = pd.DataFrame([[bedrooms, bathrooms, sqft_living, sqft_lot, floors,
                                waterfront, view, condition, sqft_above,
                                sqft_basement, yr_built, yr_renovated]],
                              columns=features)

    price = model.predict(input_data)[0]
    st.success(f"Predicted Price: ${price:,.2f}")
