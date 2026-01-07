## Student Academic Risk Predictor

A deployed machine learning application that predicts whether a student is at high academic risk based on attendance, internal performance, and past failures — and explains the reasons behind each prediction.

#### Live Demo:
https://student-academic-risk-predictor-kuhxhdpikzgjglrvx3z32j.streamlit.app/
### Problem Statement
Educational institutions often struggle to identify students who are academically at risk early enough to intervene.
This project aims to:
Predict whether a student is at high academic risk
Highlight the key factors contributing to that risk
Provide interpretable, human-readable explanations instead of black-box predictions
### Approach
##### 1️. Data Analysis & Feature Engineering
Performed exploratory data analysis (EDA) on student academic records
Identified strong predictors such as:
Attendance patterns
Internal assessment scores
History of academic failures
Removed noisy and redundant features to improve model clarity
##### 2️ Modeling
Formulated the task as a binary classification problem
Trained an interpretable Logistic Regression model
Focused on explainability and reliability rather than model complexity
##### 3 Explainability
Converted model coefficients into clear natural-language explanations
Each prediction answers not just what, but why
Example:
“Poor attendance increases academic risk”
“Strong internal performance reduces academic risk”
##### 4️ Deployment
Built an interactive Streamlit web application
Deployed publicly using GitHub + Streamlit Cloud
Allows real-time user input and instant predictions

### Application Features
 User input for academic details
 Real-time academic risk prediction
 Transparent reasoning for each prediction
 Fully deployed and publicly accessibleApplication Features
 User input for academic details
 Real-time academic risk prediction
 Transparent reasoning for each prediction
 Fully deployed and publicly accessible
 
