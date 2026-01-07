import streamlit as st
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split


# Load & train model (lightweight)

@st.cache_data
def train_model():
    # Load data
    df = pd.read_csv("student-mat.csv", sep=";")

    # Feature engineering
    df["avg_internal"] = (df["G1"] + df["G2"]) / 2
    df["attendance_risk"] = (df["absences"] > 10).astype(int)
    df["high_risk"] = (df["G3"] < 10).astype(int)

    features = ["avg_internal", "attendance_risk", "failures"]
    X = df[features]
    y = df["high_risk"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)

    return model, features

model, FEATURES = train_model()

# UI

st.title("🎓 Student Academic Risk Predictor")
st.write("Predicts academic risk and explains the key reasons.")

st.sidebar.header("Enter Student Details")

avg_internal = st.sidebar.slider(
    "Average Internal Score (0–20)", 0.0, 20.0, 10.0
)

absences = st.sidebar.number_input(
    "Number of Absences", min_value=0, max_value=100, value=5
)

failures = st.sidebar.number_input(
    "Past Failures", min_value=0, max_value=5, value=0
)

attendance_risk = 1 if absences > 10 else 0

# Prediction

if st.sidebar.button("Predict Risk"):
    student_df = pd.DataFrame([{
        "avg_internal": avg_internal,
        "attendance_risk": attendance_risk,
        "failures": failures
    }])

    prediction = model.predict(student_df)[0]

    st.subheader("📊 Prediction Result")
    if prediction == 1:
        st.error("High Academic Risk")
    else:
        st.success("Not High Risk")


    # Explanation

    contributions = student_df.iloc[0] * model.coef_[0]
    explanation_df = pd.DataFrame({
        "feature": FEATURES,
        "contribution": contributions
    }).sort_values(by="contribution", ascending=False)

    st.subheader(" Explanation")

    # Attendance explanation
    if attendance_risk == 1:
       st.write("• Poor attendance increases academic risk")
    else:
       st.write("• Regular attendance reduces academic risk")

    # Internal score explanation (VALUE-BASED, not coefficient-based)
    if avg_internal < 10:
       st.write("• Low internal scores increase academic risk")
    else:
       st.write("• Strong internal performance reduces academic risk")
