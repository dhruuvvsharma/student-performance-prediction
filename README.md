# Student Performance Prediction

An end-to-end Machine Learning project that predicts a student's **Math Score** based on demographic information, parental education, test preparation, Reading Score, and Writing Score.

The project covers the complete ML workflow from **EDA and data preprocessing to model training, evaluation, hyperparameter tuning, prediction, and Flask deployment**.

---

## Problem Statement

The objective is to predict:

**Target:** `math_score`

Using the following features:

- Gender
- Race/Ethnicity
- Parental Level of Education
- Lunch
- Test Preparation Course
- Reading Score
- Writing Score

**Problem Type:** Supervised Learning — Regression


## Dataset

The project uses the **Students Performance in Exams** dataset.

- **Records:** 1000 students
- **Target:** `math_score`

The dataset contains demographic information and scores in Mathematics, Reading, and Writing.


## EDA Insights

Exploratory Data Analysis was performed to understand the data and identify useful relationships.

### Key Findings

- Reading Score and Writing Score have a strong positive relationship with Math Score.
- Students who completed the test preparation course generally performed better.
- Lunch type showed noticeable differences in academic performance.
- Parental education level showed variations in student performance.
- Reading, Writing, and Math Scores are positively correlated with each other.

These observations helped in selecting relevant features for the regression model.

## Machine Learning Workflow

Dataset
   ↓
Data Ingestion
   ↓
EDA & Feature Engineering
   ↓
Data Transformation
   ↓
Model Training
   ↓
Model Evaluation
   ↓
Hyperparameter Tuning
   ↓
Model Serialization
   ↓
Prediction Pipeline
   ↓
Flask Web Application

## Models Experimented With

Several regression algorithms were trained and compared:

Linear Regression
Lasso
Ridge
K-Nearest Neighbors
Decision Tree
Random Forest
AdaBoost
Gradient Boosting
XGBoost
CatBoost
Evaluation Metrics
MAE — Mean Absolute Error
RMSE — Root Mean Squared Error
R² Score

Lastly, Hyperparameter tuning was performed to improve the performance of the selected model.

## Prediction Pipeline
User Input
    ↓
DataFrame
    ↓
Preprocessor
    ↓
Trained Model
    ↓
Predicted Math Score

## Tech Stack
Programming: Python
Data Analysis: Pandas, NumPy
Visualization: Matplotlib, Seaborn
Machine Learning: Scikit-learn, XGBoost, CatBoost
Web: Flask, HTML, CSS, JavaScript
Development: Jupyter Notebook, Git, GitHub



## Project Structure

```text
Student-Performance-Prediction/
│
├── notebook/
│   ├── data/
│   │   └── stud.csv
│   ├── 1. EDA STUDENT PERFORMANCE.ipynb
│   └── 2. MODEL TRAINING.ipynb
│
├── src/
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   └── model_trainer.py
│   │
│   ├── pipelines/
│   │   ├── train_pipeline.py
│   │   └── predict_pipeline.py
│   │
│   ├── exception.py
│   ├── logger.py
│   └── utils.py
│
├── static/
│   ├── script.js
│   └── style.css
│
├── templates/
│   ├── home.html
│   └── index.html
│
├── logs/
│
├── app.py
├── setup.py
├── requirements.txt
├── .gitignore
└── README.md

