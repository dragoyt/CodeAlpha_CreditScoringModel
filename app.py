import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
import joblib

# Load the pre-trained model and preprocessor
@st.cache_resource
def load_model():
    preprocessor = joblib.load('preprocessor.joblib')
    model = joblib.load('credit_scoring_model.joblib')
    return preprocessor, model

preprocessor, model = load_model()

# Streamlit app
st.title("Credit Scoring Model (INR)")
st.write("Predict the creditworthiness of applicants based on income, debt, and credit history. All values are in INR.")

# Input fields
st.sidebar.header("Input Features")
income = st.sidebar.number_input("Annual Income (INR)", min_value=200000, max_value=10000000, value=500000)
debt = st.sidebar.number_input("Total Debt (INR)", min_value=50000, max_value=4000000, value=200000)
credit_history = st.sidebar.selectbox("Credit History", ["poor", "fair", "good", "excellent"])

# Create a DataFrame from inputs
input_data = pd.DataFrame({
    'income': [income],
    'debt': [debt],
    'credit_history': [credit_history],
    'debt_to_income': [debt / (income + 1e-6)]  # Avoid division by zero
})

# Display input data
st.subheader("Input Data")
st.write(input_data)

# Preprocess input data
input_processed = preprocessor.transform(input_data)

# Make prediction
prediction = model.predict(input_processed)
prediction_proba = model.predict_proba(input_processed)

# Display prediction
st.subheader("Prediction")
if prediction[0] == 1:
    st.success("Creditworthy ✅")
else:
    st.error("Not Creditworthy ❌")

st.write(f"Probability of being creditworthy: {prediction_proba[0][1]:.2f}")

# Explanation
st.subheader("How It Works")
st.write("""
This app uses a pre-trained machine learning model to predict the creditworthiness of applicants based on the following features:
- **Annual Income**: The applicant's yearly income in Indian Rupees (INR).
- **Total Debt**: The applicant's total debt in Indian Rupees (INR).
- **Credit History**: The applicant's credit history, categorized as 'poor', 'fair', 'good', or 'excellent'.
- **Debt-to-Income Ratio**: Calculated as `Total Debt / Annual Income`.

The model outputs whether the applicant is likely to be creditworthy and the probability of that prediction.
""")
# Footer
st.markdown("---")
st.markdown("Developed by **Piyush Kr. Mahato**")