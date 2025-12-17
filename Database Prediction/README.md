## Project 2: Diabetes Prediction using Machine Learning (SVM)

### Project Overview

This project builds an **end-to-end machine learning pipeline** to predict whether a person has diabetes based on medical attributes.
A **Support Vector Machine (SVM)** classifier is used for binary classification.

**Classification Labels:**

* `0` → Non-diabetic
* `1` → Diabetic


### Dataset

**Pima Indians Diabetes Dataset**

**Features:**

* Pregnancies
* Glucose
* BloodPressure
* SkinThickness
* Insulin
* BMI
* DiabetesPedigreeFunction
* Age

**Target:**

* Outcome


### 🛠️ Tools & Libraries

* Python
* NumPy
* Pandas
* Matplotlib / Seaborn
* Scikit-learn
  
### Workflow (End-to-End)

1. Import required libraries
2. Load the dataset
3. Data exploration & cleaning
4. Feature scaling (Standardization)
5. Train-test split
6. Model training using SVM
7. Model evaluation
8. Prediction on new data

---

###  Results

* Achieved **~75–80% accuracy** (may vary depending on data split and parameters)
* Feature scaling significantly improved model performance

---

###  Conclusion

* Support Vector Machine (SVM) performs well for diabetes prediction
* Standardization is crucial for SVM models
* Model performance can be improved by:

  * Hyperparameter tuning (GridSearchCV)
  * Trying different kernels (RBF, Polynomial)
  * Proper handling of zero or missing values
