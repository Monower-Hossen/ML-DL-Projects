from flask import Flask, render_template, request
import numpy as np
import pickle
import pandas as pd

# Flask app
app = Flask(__name__)

# Load trained model and scaler
model = pickle.load(open('diabetes_svm_model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

# Feature names
feature_names = ['Pregnancies','Glucose','BloodPressure','SkinThickness','Insulin','BMI','DiabetesPedigreeFunction','Age']

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():

    # Get input values from form
    data = []
    for feature in features:
        value = float(request.form[feature])
        data.append(value)
    
    # Convert to DataFrame
    input_df = pd.DataFrame([input_data], columns=feature_names)
    
    # Scale
    input_scaled = scaler.transform(input_df)
    
    # Predict
    prediction = model.predict(input_scaled)[0]
    
    # Output message
    if prediction == 0:
        result = "The person is NOT diabetic"
    else:
        result = "The person is diabetic"
    
    return render_template('index.html', prediction_text=result)

if __name__ == "__main__":
    app.run(debug=True)
