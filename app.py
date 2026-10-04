import streamlit as st
import pandas as pd
import joblib

# -----------------------------------
# Page Configuration
# -----------------------------------
st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="🏦",
    layout="centered"
)

# -----------------------------------
# Load Model and Feature Columns
# -----------------------------------
@st.cache_resource
def load_model():
    return joblib.load("../model/best_churn_model.pkl")


@st.cache_resource
def load_features():
    return joblib.load("../model/feature_columns.pkl")


model = load_model()
feature_columns = load_features()

# -----------------------------------
# Title
# -----------------------------------
st.title("🏦 Customer Churn Prediction")
st.write(
    "Enter the customer information below to predict whether "
    "the customer is likely to churn."
)

st.divider()

# -----------------------------------
# User Inputs
# -----------------------------------
age = st.number_input(
    "Age",
    min_value=18,
    max_value=100,
    value=30
)

total_spent = st.number_input(
    "Total Spent",
    min_value=0.0,
    value=1000.0,
    step=100.0
)

login_frequency = st.number_input(
    "Login Frequency",
    min_value=0,
    value=10,
    step=1
)

income_level = st.selectbox(
    "Income Level",
    ["Low", "Medium", "High"]
)

marital_status = st.selectbox(
    "Marital Status",
    ["Single", "Married"]
)

gender = st.selectbox(
    "Gender",
    ["F", "M"]
)

service_usage = st.selectbox(
    "Service Usage",
    ["Website", "Online Banking"]
)

st.divider()

# -----------------------------------
# Prediction
# -----------------------------------
if st.button("🔍 Predict Churn", use_container_width=True):

    # Create raw input
    input_data = pd.DataFrame({
        "Age": [age],
        "TotalSpent": [total_spent],
        "LoginFrequency": [login_frequency],
        "IncomeLevel": [income_level],
        "MaritalStatus": [marital_status],
        "Gender": [gender],
        "ServiceUsage": [service_usage]
    })

    # One-hot encode categorical features
    input_data = pd.get_dummies(
        input_data,
        columns=[
            "IncomeLevel",
            "MaritalStatus",
            "Gender",
            "ServiceUsage"
        ],
        drop_first=True,
        dtype=int
    )

    # Match the exact training features
    input_data = input_data.reindex(
        columns=feature_columns,
        fill_value=0
    )

    # Prediction
    prediction = model.predict(input_data)[0]

    # Churn probability
    probability = model.predict_proba(input_data)[0][1]

    # -----------------------------------
    # Result
    # -----------------------------------
    if prediction == 1:

        st.error("⚠️ Customer is likely to churn.")

        st.metric(
            "Churn Probability",
            f"{probability:.2%}"
        )

        st.info(
            "Consider a low-cost retention campaign, "
            "personalized communication, or a small incentive."
        )

    else:

        st.success("✅ Customer is likely to stay.")

        st.metric(
            "Churn Probability",
            f"{probability:.2%}"
        )