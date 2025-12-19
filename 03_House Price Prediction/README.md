# 🏠 House Price Prediction Using Machine Learning

## Abstract

Accurate house price prediction plays a crucial role in real estate valuation, urban planning, and financial decision-making. This project presents a supervised machine learning approach to predict residential house prices based on structural and historical features. An XGBoost regression model is employed due to its strong performance on tabular data. The model is trained after systematic data preprocessing, including outlier handling and feature selection. Additionally, a Streamlit-based web application is developed to allow real-time predictions using both manual input and CSV file uploads.

## 1. Introduction

House price estimation is a complex problem influenced by multiple factors such as property size, location attributes, construction year, and renovation history. Traditional valuation methods often rely on expert judgment, which can be time-consuming and subjective. Machine learning techniques offer a data-driven alternative that can improve prediction accuracy and consistency.

The objective of this project is to design and implement a robust machine learning model capable of predicting house prices with high accuracy and deploy it through an interactive web application.

## 2. Dataset Description

The dataset used in this study consists of residential property records containing both numerical and categorical attributes. The key features include:

* **bedrooms**: Number of bedrooms
* **bathrooms**: Number of bathrooms
* **sqft_living**: Living area in square feet
* **sqft_lot**: Total lot size in square feet
* **floors**: Number of floors
* **waterfront**: Presence of a waterfront view (binary)
* **view**: Quality of the view
* **condition**: Overall condition of the house
* **sqft_above**: Area above ground level
* **sqft_basement**: Basement area
* **yr_built**: Year of construction
* **yr_renovated**: Year of renovation (if applicable)

The target variable is the **house price**, represented as a continuous numerical value.

## 3. Data Preprocessing

To ensure data quality and improve model performance, several preprocessing steps were applied:

1. **Handling Missing Values**: Records with missing or inconsistent values were addressed.
2. **Outlier Detection and Removal**: The Interquartile Range (IQR) method was used to identify and remove extreme outliers.
3. **Feature Selection**: Relevant features contributing to price prediction were selected based on domain knowledge.
4. **Train-Test Split**: The dataset was divided into training and testing subsets to evaluate generalization performance.


## 4. Model Selection and Training

The **XGBoost Regressor** was chosen as the primary model due to its ability to handle non-linear relationships and complex feature interactions. XGBoost is an ensemble learning method based on gradient boosting that has demonstrated superior performance in regression tasks involving structured data.

The model was trained on the processed dataset, and hyperparameters were tuned to achieve optimal predictive accuracy.


## 5. Model Evaluation

The trained model was evaluated using standard regression performance metrics, including:

* Mean Absolute Error (MAE)
* Mean Squared Error (MSE)
* Root Mean Squared Error (RMSE)
* R² Score

These metrics provided quantitative insight into the model’s prediction accuracy and robustness.


## 6. Web Application Deployment

To enhance usability and practical applicability, the trained model was deployed using **Streamlit**, a lightweight Python framework for building data applications. The application provides two modes of prediction:

1. **CSV File Upload**: Users can upload a dataset containing multiple house records and generate predicted prices in batch form.
2. **Manual Input**: Users can enter individual house features and receive instant price predictions.

The application also supports downloading the prediction results as a CSV file.


## 7. Conclusion

This project demonstrates the effectiveness of machine learning techniques, particularly XGBoost, in predicting house prices with high accuracy. The integration of a user-friendly web interface further bridges the gap between theoretical modeling and real-world application. Future work may include incorporating location-based features, experimenting with deep learning models, and deploying the application on a cloud platform.

## 8. Technologies Used

* Python
* Pandas, NumPy
* Scikit-learn
* XGBoost
* Streamlit
* Joblib


## ⚙️ Installation
[![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python\&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-orange?logo=streamlit\&logoColor=white)](https://streamlit.io/)
[![XGBoost](https://img.shields.io/badge/XGBoost-Regression-red?logo=xgboost\&logoColor=white)](https://xgboost.readthedocs.io/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)


## 📁 Folder Structure

```
House-Price-Prediction/
│
├── models/               # Trained model file (xgb_model.pkl)
├── data/                 # Sample dataset CSV files
├── app.py                # Streamlit app script
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
└── .gitignore
```

## 📜 License

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.

## 📬 Contact

**Monower Hossen**
[GitHub](https://github.com/Monower-Hossen) | [LinkedIn](https://www.linkedin.com/in/monower-hossen/)
