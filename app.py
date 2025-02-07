import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Load the trained model
model = joblib.load(r'PycharmProjects\Loan_Prediction\loan_model.pkl')

# Streamlit App Title
st.set_page_config(page_title="Loan Approval Prediction", page_icon="🏦", layout="centered")

st.title("🏦 Loan Approval Prediction App")
st.write("### Predict your loan approval status based on key financial details.")

# Sidebar for Instructions
with st.sidebar:
    st.header("ℹ️ How to Use")
    st.write(
        """
        - **Enter your details** in the provided fields.
        - **Click 'Predict Loan Approval'** to check the result.
        - **The app will tell you whether your loan is likely to be approved or not.**
        """
    )
    st.info("📌 Note: All financial inputs should be **numeric**.")

# Function to preprocess user input
def preprocess_input(data):
    """Function to create new features and preprocess user input."""
    # Feature Engineering
    data['Total_income'] = data['ApplicantIncome'] + data['CoapplicantIncome']
    data['EMI'] = data['LoanAmount'] / data['Loan_Amount_Term']
    data['Income_Loan_Ratio'] = data['Total_income'] / data['LoanAmount']
    data['Loan_to_Income'] = data['LoanAmount'] / data['Total_income']

    # Log Transformation
    data['LoanAmount'] = np.log1p(data['LoanAmount'])
    data['Total_income'] = np.log1p(data['Total_income'])
    data['Income_Loan_Ratio'] = np.log1p(data['Income_Loan_Ratio'])
    data['Loan_to_Income'] = np.log1p(data['Loan_to_Income'])
    data['EMI'] = np.log1p(data['EMI'])

    return data

# User Inputs Section
st.write("## 🔍 Enter Your Loan Details")

col1, col2 = st.columns(2)

with col1:
    Married = st.selectbox("👥 Married", ["Yes", "No"])
    ApplicantIncome = st.number_input("💰 Applicant Income", min_value=0, step=1000)
    CoapplicantIncome = st.number_input("👨‍👩‍👦 Coapplicant Income", min_value=0, step=1000)
    Credit_History = st.selectbox("📊 Credit History", [1.0, 0.0])

with col2:
    LoanAmount = st.number_input("🏦 Loan Amount", min_value=0, step=5000)
    Loan_Amount_Term = st.number_input("📆 Loan Amount Term (Months)", min_value=12, step=12)
    Property_Area = st.selectbox("📍 Property Area", ["Urban", "Rural", "Semiurban"])

# Encoding categorical values
married_map = {"Yes": 1, "No": 0}
property_map = {"Urban": [0, 0, 1], "Semiurban": [0, 1, 0], "Rural": [1, 0, 0]}

# Create input DataFrame
input_data = pd.DataFrame({
    "Married": [married_map[Married]],
    "ApplicantIncome": [ApplicantIncome],
    "CoapplicantIncome": [CoapplicantIncome],
    "LoanAmount": [LoanAmount],
    "Loan_Amount_Term": [Loan_Amount_Term],
    "Credit_History": [Credit_History],
    "Property_Area_Rural": [property_map[Property_Area][0]],
    "Property_Area_Semiurban": [property_map[Property_Area][1]],
    "Property_Area_Urban": [property_map[Property_Area][2]],
})

# Preprocess the input
input_data = preprocess_input(input_data)

# Ensure column order matches the trained model
input_data = input_data.reindex(columns=model.feature_names_in_)

# Prediction Button
if st.button("🚀 Predict Loan Approval", use_container_width=True):
    prediction = model.predict(input_data)
    if prediction[0] == 1:
        st.success("🎉 ✅ Loan Approved! You are eligible for the loan.")
    else:
        st.error("❌ Loan Not Approved. Consider improving your credit score or financial status.")

# Footer
st.write("---")
st.write("💡 **Built with Streamlit & Machine Learning** | Developed by *Risal Khan*")
