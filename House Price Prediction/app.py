import streamlit as st
import pandas as pd
import joblib


# Load the trained model

model = joblib.load("model/xgb_model.pkl")

# App Title and Description
st.title("🏠 House Price Prediction App")
st.write("Upload a CSV or enter data manually to predict house prices.")

# CSV Upload Option

st.subheader("Upload CSV File")
uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
    required_columns = ["bedrooms","bathrooms","sqft_living","sqft_lot","floors",
                        "waterfront","view","condition","sqft_above","sqft_basement",
                        "yr_built","yr_renovated"]
    
    if all(col in df.columns for col in required_columns):
        st.success("CSV looks good!")
        
        # Button to predict
        if st.button("Predict from CSV"):
            df["Predicted_Price"] = model.predict(df[required_columns])
            st.dataframe(df)
            st.download_button(
                label="Download CSV with Predictions",
                data=df.to_csv(index=False),
                file_name="predictions.csv",
                mime="text/csv"
            )
    else:
        st.error(f"CSV must have these columns: {required_columns}")

# Manual Input Option
st.subheader("Or enter data manually:")

bedrooms = st.number_input("Bedrooms", 1, 10, 3)
bathrooms = st.number_input("Bathrooms", 1, 10, 2)
sqft_living = st.number_input("Living Area (sqft)", 300, 10000, 1500)
sqft_lot = st.number_input("Lot Size (sqft)", 300, 50000, 5000)
floors = st.number_input("Floors", 1, 5, 1)
waterfront = st.selectbox("Waterfront (0=no, 1=yes)", [0,1])
view = st.number_input("View (0-4)", 0, 4, 0)
condition = st.number_input("Condition (1-5)", 1, 5, 3)
sqft_above = st.number_input("Above Ground Area (sqft)", 300, 10000, 1000)
sqft_basement = st.number_input("Basement Area (sqft)", 0, 5000, 500)
yr_built = st.number_input("Year Built", 1800, 2025, 1990)
yr_renovated = st.number_input("Year Renovated (0 if never)", 0, 2025, 0)

if st.button("Predict Price Manually"):
    input_df = pd.DataFrame([[bedrooms, bathrooms, sqft_living, sqft_lot, floors,
                              waterfront, view, condition, sqft_above, sqft_basement,
                              yr_built, yr_renovated]],
                            columns=required_columns)
    prediction = model.predict(input_df)
    st.success(f"Predicted House Price: ${prediction[0]:,.2f}")
