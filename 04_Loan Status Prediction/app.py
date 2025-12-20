import streamlit as st
import pandas as pd
import joblib

# Load model & scaler
model = joblib.load("model/loan_rf_model.pkl")
scaler = joblib.load("model/loan_scaler.pkl")

# App title
st.title("🏦 Loan Status Prediction App")
st.write("Predict whether a loan will be approved or rejected.")

# Choose mode
mode = st.sidebar.radio("Choose Prediction Mode", ["Manual Input", "CSV Upload"])

# MANUAL INPUT MODE

if mode == "Manual Input":
    st.subheader("Enter Applicant Details")

    gender = st.selectbox("Gender", ["Male", "Female"])
    married = st.selectbox("Married", ["Yes", "No"])
    education = st.selectbox("Education", ["Graduate", "Not Graduate"])
    dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])
    self_employed = st.selectbox("Self Employed", ["Yes", "No"])
    income = st.number_input("Applicant Income", value=5000)
    co_income = st.number_input("Co-applicant Income", value=0)
    loan_amount = st.number_input("Loan Amount", value=150)
    term = st.selectbox("Loan Term (Days)", [360, 180, 120, 84, 60, 36])
    credit_history = st.selectbox("Credit History", ["Good", "Bad"])
    property_area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])

    # Encode categorical values
    gender = 1 if gender == "Male" else 0
    married = 1 if married == "Yes" else 0
    dependents = 3 if dependents == "3+" else int(dependents)
    education = 0 if education == "Graduate" else 1
    self_employed = 1 if self_employed == "Yes" else 0
    credit_history = 1 if credit_history == "Good" else 0
    property_area = 0 if property_area == "Rural" else 1 if property_area == "Semiurban" else 2

    if st.button("Predict Loan Status"):
        # Create DataFrame
        df = pd.DataFrame([[gender, married, dependents, education, self_employed,
                            income, co_income, loan_amount, term, credit_history, property_area]],
                          columns=["Gender", "Married", "Dependents", "Education", "Self_Employed",
                                   "ApplicantIncome", "CoapplicantIncome", "LoanAmount",
                                   "Loan_Amount_Term", "Credit_History", "Property_Area"])
        # Scale & predict
        df_scaled = scaler.transform(df)
        pred = model.predict(df_scaled)[0]

        st.write("---")
        if pred == 1:
            st.success("✅ Loan Approved")
        else:
            st.error("❌ Loan Rejected")
            
# CSV UPLOAD MODE
else:
    st.subheader("Upload CSV File")
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        st.write("Preview of Uploaded Data")
        st.dataframe(data.head())

        if st.button("Predict from CSV"):
            # Keep only feature columns
            features = ["Gender", "Married", "Dependents", "Education", "Self_Employed",
                        "ApplicantIncome", "CoapplicantIncome", "LoanAmount",
                        "Loan_Amount_Term", "Credit_History", "Property_Area"]
            input_data = data[features].copy()

            # Scale & predict
            input_scaled = scaler.transform(input_data)
            predictions = model.predict(input_scaled)

            # Add predictions to original data
            data["Loan_Status"] = ["Approved" if p==1 else "Rejected" for p in predictions]

            st.write("Prediction Results")
            st.dataframe(data)

            # Download predictions
            csv = data.to_csv(index=False).encode("utf-8")
            st.download_button("⬇️ Download Predictions", csv, "loan_prediction_result.csv", "text/csv")

st.write("---")
st.write("Developed by Monower Hossen | [GitHub](https://github.com/Monower-Hossen)")
