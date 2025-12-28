# Fake News Detection Using Linear Regression

## Abstract
The rapid spread of misinformation through online platforms poses significant social, political, and economic risks. Fake news detection has therefore become an important research problem in the fields of Natural Language Processing (NLP) and Machine Learning. This project investigates the feasibility of using **Linear Regression** as a baseline statistical model for detecting fake news based on textual features. Although linear regression is traditionally used for continuous prediction tasks, it is adapted here for binary classification through thresholding, providing an interpretable and computationally efficient benchmark.


## Keywords
Fake News Detection, Linear Regression, Natural Language Processing, Text Classification, Machine Learning


## 1. Introduction
The proliferation of digital media has enabled rapid dissemination of information, but it has also facilitated the spread of misleading or false content, commonly referred to as *fake news*. Automated fake news detection systems aim to assist human fact-checkers by identifying potentially unreliable content at scale.

Most existing approaches rely on advanced classifiers such as Support Vector Machines, Random Forests, or Deep Neural Networks. In contrast, this project focuses on **Linear Regression** as a simple and interpretable baseline model to study the relationship between textual features and news authenticity.


## 2. Problem Statement
Given a dataset of news articles labeled as **fake** or **real**, the objective is to:
- Extract meaningful numerical features from text,
- Train a linear regression model to predict a continuous authenticity score,
- Convert the regression output into binary class labels using a decision threshold.


## 3. Dataset
The dataset consists of news articles with corresponding labels:
- `1` – Real news  
- `0` – Fake news  

Each record typically contains:
- Title
- Body text
- Label

> **Note:** Any publicly available fake news dataset (e.g., Kaggle Fake News Dataset) can be used. Ensure proper citation if publishing results.


## 4. Methodology

### 4.1 Text Preprocessing
The following preprocessing steps are applied:
- Lowercasing
- Removal of punctuation and special characters
- Stopword removal
- Tokenization
- Optional stemming or lemmatization

### 4.2 Feature Extraction
Textual data is converted into numerical representations using:
- Bag of Words (BoW), or
- Term Frequency–Inverse Document Frequency (TF-IDF)

These features serve as input variables for the regression model.

### 4.3 Model Selection
**Linear Regression** is used to model the relationship between extracted text features and the target label.

Although linear regression outputs continuous values, classification is achieved by applying a threshold (e.g., 0.5):
- Output ≥ threshold → Real news
- Output < threshold → Fake news

### 4.4 Training and Testing
The dataset is split into:
- Training set
- Testing set  

The model is trained using Ordinary Least Squares (OLS).


## 5. Evaluation Metrics
Model performance is evaluated using standard classification metrics:
- Accuracy
- Precision
- Recall
- F1-Score

These metrics provide insight into the effectiveness of a regression-based approach for a classification task.


## 6. Results and Discussion
The linear regression model demonstrates that even simple statistical approaches can capture meaningful patterns in textual data. However, performance is generally inferior to specialized classification algorithms, especially on complex or highly imbalanced datasets. The primary advantage of this approach lies in its **interpretability** and **computational efficiency**, making it suitable as a baseline model.


## 7. Limitations
- Linear regression is not inherently designed for classification.
- Performance may degrade with high-dimensional sparse text features.
- Non-linear relationships in language are not effectively captured.


## 8. Future Work
Potential improvements include:
- Comparing results with Logistic Regression and SVMs
- Incorporating n-grams and semantic embeddings
- Applying regularization techniques (Ridge, Lasso)
- Exploring deep learning approaches such as LSTM or Transformer-based models


## 9. Technologies Used
- Python
- NumPy
- Pandas
- Scikit-learn
- Natural Language Toolkit (NLTK)


## 10. Conclusion
This project demonstrates the application of linear regression to the task of fake news detection as a baseline research experiment. While not optimal for real-world deployment, it provides valuable insights into feature behavior and serves as a foundation for more advanced machine learning models.


## 🚀 Installation & Usage

```bash
# Install dependencies
pip install -r requirements.txt

# Run Streamlit app
streamlit run app.py
```

## 📈 Results & Performance

The Random Forest model demonstrates strong predictive performance and generalization ability, making it suitable for real-world loan approval systems.


## ⚙️ Installation
![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python\&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?logo=scikitlearn\&logoColor=white)
![Random Forest](https://img.shields.io/badge/Algorithm-Random%20Forest-green)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-red?logo=streamlit)
![License](https://img.shields.io/badge/License-MIT-brightgreen)

## 📸 App Screenshots

### Manual Input Mode
![Manual Input](Screenshots/fake-news.png)



## 📜 License

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.

## 📬 Contact

**Monower Hossen**
[GitHub](https://github.com/Monower-Hossen) | [LinkedIn](https://www.linkedin.com/in/monower-hossen/)
