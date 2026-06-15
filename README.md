# Human Activity Recognition with Smartphones

## Project Overview

This project applies machine learning techniques to classify human physical activities using smartphone sensor data. The dataset contains measurements from accelerometer and gyroscope sensors collected while participants performed daily activities such as walking, sitting, standing, and lying down.

The objective is to compare multiple machine learning models and identify the most effective approach for accurate human activity recognition.

---

## Dataset

The dataset used is the Human Activity Recognition Using Smartphones Dataset. It includes:

- Sensor signals from accelerometer and gyroscope
- Engineered statistical features derived from raw signals
- Six activity classes:
  - LAYING
  - SITTING
  - STANDING
  - WALKING
  - WALKING_DOWNSTAIRS
  - WALKING_UPSTAIRS

Each sample represents a feature vector derived from a fixed window of sensor readings.

---

## Project Workflow

The project follows a structured machine learning pipeline:

1. Data loading and exploration
2. Feature and target separation
3. Train-validation split
4. Feature scaling (for applicable models)
5. Model training
6. Model evaluation
7. Model comparison
8. Feature importance analysis
9. Model selection and saving

---

## Models Used

The following machine learning models were evaluated:

- Logistic Regression
- K-Nearest Neighbours
- Support Vector Machine
- Random Forest
- Gradient Boosting

---

## Best Model

The best-performing model was Gradient Boosting Classifier.

### Performance

- Accuracy: approximately 0.99
- Macro F1-score: approximately 0.99

This model achieved the most balanced performance across all activity classes.

---

## Key Findings

- Tree-based models significantly outperformed linear models.
- Gradient Boosting provided the best overall performance.
- Minor misclassification occurred between Sitting and Standing due to similar sensor patterns.
- A small subset of features contributed disproportionately to model predictions.
- Gravity-based acceleration features were among the most important predictors.

---

## Feature Importance

Feature importance analysis from the Gradient Boosting model revealed that:

- A limited number of features account for most predictive power.
- The most influential feature contributed over 25 percent of total importance.
- Acceleration and gravity-related signals were the most informative.

This suggests that activity recognition can be performed effectively using a reduced feature set.

---

## Saved Models

The following trained models are saved for reuse:

- Gradient Boosting Classifier (`gradient_boosting.pkl`)
- Random Forest Classifier (`random_forest.pkl`)

Models were saved using joblib and can be reloaded for inference without retraining.

---

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Joblib

---

## How to Run

Clone the repository:

git clone <repository-url>
cd human-activity-recognition

Install dependencies:

pip install -r requirements.txt

Run notebooks in order:

- 01_exploration.ipynb
- 02_model_training.ipynb

---

## Future Improvements

### Feature Reduction
- Evaluate performance using only top features
- Analyse trade-off between accuracy and model complexity

### Hyperparameter Tuning
- Use GridSearchCV or RandomizedSearchCV
- Improve Gradient Boosting performance

### Real-Time Prediction System
- Build a simple interface for live predictions
- Use Streamlit or similar framework

### Deep Learning Models
- Experiment with neural networks for sequence classification
- Compare with classical machine learning models

### Deployment
- Deploy model as a web app or API

---

## Conclusion

This project demonstrates that machine learning models can accurately classify human activities using smartphone sensor data. Gradient Boosting achieved the highest performance, highlighting the effectiveness of ensemble methods for structured sensor-based datasets.
