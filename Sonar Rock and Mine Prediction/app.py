# sonar_web_app.py
# A web app to predict Rock or Mine from sonar signals using SVM

from flask import Flask, request, render_template
import numpy as np
import pandas as pd
import joblib

# Step 1: Load trained SVM model and scaler
svm_model = joblib.load('sonar_svm_model.pkl')
scaler = joblib.load('scaler.pkl')

# Step 2: Create Flask app
app = Flask(__name__)

# Step 3: Home route
@app.route('/')
def home():
    return render_template('index.html')  # This will be our main web page

# Step 4: Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Check if file is uploaded
        if 'file' in request.files:
            file = request.files['file']
            df = pd.read_csv(file, header=None)  # CSV file with 60 features per row
            # Scale features
            X_scaled = scaler.transform(df)
            # Predict
            predictions = svm_model.predict(X_scaled)
            df['Prediction'] = predictions
            return render_template('index.html', tables=[df.to_html(classes='data', header=False)], result="Predictions generated from uploaded file!")
        else:
            # If manual input from form
            input_features = [float(x) for x in request.form.values()]
            input_array = np.array(input_features).reshape(1, -1)
            input_scaled = scaler.transform(input_array)
            prediction = svm_model.predict(input_scaled)[0]
            return render_template('index.html', result=f'Predicted Class: {prediction}')
    except Exception as e:
        return render_template('index.html', result=f"Error: {str(e)}")

# Step 5: Run the app
if __name__ == "__main__":
    app.run(debug=True)
