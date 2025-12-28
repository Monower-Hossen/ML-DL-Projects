# 🚗 Car Price Prediction using Machine Learning

## 1. Abstract

Car price prediction is an important problem in the automobile and resale market, where accurate estimation of vehicle value helps buyers and sellers make informed decisions. This project focuses on predicting the selling price of used cars using supervised machine learning techniques. Multiple regression models are implemented and compared, including Linear Regression and Lasso Regression. The models are trained on historical car data containing both numerical and categorical features. The performance of each model is evaluated using standard regression metrics, and the best-performing model is deployed through a Streamlit-based web application.


## 2. Keywords

Car Price Prediction, Machine Learning, Linear Regression, Lasso Regression, Used Cars, Streamlit, Supervised Learning


## 3. Introduction

The rapid growth of the used car market has created a need for reliable pricing mechanisms. Traditional manual pricing methods are often subjective and inconsistent. Machine learning offers a data-driven approach to estimate car prices by learning patterns from historical data.
This project aims to build an accurate and interpretable car price prediction system using regression-based algorithms. The system considers multiple vehicle attributes such as manufacturing year, fuel type, transmission, and ownership history to estimate the selling price.


## 4. Dataset Description

The dataset used in this study consists of used car records with the following attributes:

| Feature Name  | Description                           |
| ------------- | ------------------------------------- |
| name          | Car model name                        |
| year          | Manufacturing year                    |
| selling_price | Target variable (car price)           |
| km_driven     | Distance driven in kilometers         |
| fuel          | Fuel type (Petrol, Diesel, CNG, etc.) |
| seller_type   | Seller category                       |
| transmission  | Manual or Automatic                   |
| owner         | Ownership status                      |

### Dataset Source

The dataset is collected from publicly available used car sales records and online automobile marketplaces.


## 5. Data Preprocessing

The following preprocessing steps were applied:

* Removal of irrelevant features (e.g., car name)
* Handling of categorical variables using label encoding
* Feature-target separation
* Train-test split (80% training, 20% testing)

These steps ensure data consistency and improve model performance.


## 6. Methodology

This project implements and compares the following machine learning models:

### 6.1 Linear Regression

Linear Regression models the relationship between input features and the target price using a linear function. It serves as a baseline model due to its simplicity and interpretability.

### 6.2 Lasso Regression

Lasso Regression introduces L1 regularization, which helps reduce overfitting and performs feature selection by shrinking less important coefficients to zero.


## 7. Model Training and Evaluation

The dataset was divided into training and testing subsets. Models were trained using the training data and evaluated on the test data.

### Evaluation Metrics:

* **R² Score**
* **Mean Absolute Error (MAE)**
* **Mean Squared Error (MSE)**

### Visualization:

A scatter plot of **Actual vs Predicted Prices** was used to visually assess model performance.


## 8. Results and Discussion

The experimental results indicate that:

* Linear Regression provides a strong baseline with good interpretability.
* Lasso Regression reduces model complexity and helps mitigate overfitting.
* Both models perform reasonably well, with minor differences in prediction accuracy.

In practical scenarios, more advanced ensemble models may yield higher accuracy, but linear models remain valuable for academic and explanatory purposes.


## 9. Model Deployment

The trained models were serialized using the `pickle` library and deployed using a **Streamlit web application**.
The application allows users to input car details and receive an instant predicted selling price.


## 10. Conclusion

This study demonstrates the effectiveness of regression-based machine learning models in predicting used car prices. While simple models such as Linear and Lasso Regression provide interpretable results, future work can explore advanced algorithms to further improve accuracy. The deployed application shows the practical usability of the proposed system.


## 11. Technologies Used

* Python
* Pandas, NumPy
* Scikit-learn
* Matplotlib
* Streamlit


## 12. How to Run the Project

```bash
pip install -r requirements.txt
python train_model.py
streamlit run app.py
```


## 🚀 Installation & Usage

```bash
<<<<<<< HEAD
=======
# Clone the repository
git clone https://github.com/Monower-Hossen/Loan-Status-Prediction.git

# Navigate to project directory
cd Loan-Status-Prediction

>>>>>>> 427eba4eec4dab12ff768c474b2475065b7f3acd
# Install dependencies
pip install -r requirements.txt

# Run Streamlit app
streamlit run app.py
```

<<<<<<< HEAD
## 📈 Results & Performance

The Random Forest model demonstrates strong predictive performance and generalization ability, making it suitable for real-world loan approval systems.

=======
>>>>>>> 427eba4eec4dab12ff768c474b2475065b7f3acd

## ⚙️ Installation
![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python\&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?logo=scikitlearn\&logoColor=white)
![Random Forest](https://img.shields.io/badge/Algorithm-Random%20Forest-green)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-red?logo=streamlit)
![License](https://img.shields.io/badge/License-MIT-brightgreen)

## 📸 App Screenshots

### Manual Input Mode
<<<<<<< HEAD
![Manual Input](screenshots/manual_input.png)

### CSV Upload Mode
![CSV Upload](screenshots/csv_upload.png)
=======
![Manual Input](screenshots/car_price_app.png)
>>>>>>> 427eba4eec4dab12ff768c474b2475065b7f3acd


## 📜 License

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.

<<<<<<< HEAD
## 📬 Contact

**Monower Hossen**
[GitHub](https://github.com/Monower-Hossen) | [LinkedIn](https://www.linkedin.com/in/monower-hossen/)
=======
## Author

**Monower Hossen**
BSc in Computer Science and Engineering
[GitHub](https://github.com/Monower-Hossen) | [LinkedIn](https://www.linkedin.com/in/monower-hossen/)








>>>>>>> 427eba4eec4dab12ff768c474b2475065b7f3acd
