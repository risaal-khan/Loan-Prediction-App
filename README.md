# Loan Prediction Project

This repository contains a machine learning project for predicting loan approval based on applicant details. The project uses a trained model to classify whether a loan will be approved or not.

## Features Used

The following features are used in the model:
- `Married`
- `ApplicantIncome`
- `CoapplicantIncome`
- `LoanAmount`
- `Loan_Amount_Term`
- `Credit_History`
- `Property_Area`

Additionally, the following engineered features are created:
- `Total_income`
- `EMI`
- `Income_Loan_Ratio`
- `Loan_to_Income`

## Installation

### Clone the Repository
```sh
git clone https://github.com/yourusername/loan-prediction.git
cd loan-prediction
```

### Install Dependencies
```sh
pip install -r requirements.txt
```

## Usage

### Running the Jupyter Notebook
To explore the data and train the model, open the notebook:
```sh
jupyter notebook
```
Then open `Loan Prediction.ipynb`.

### Running the Streamlit App
You can run the web application using Streamlit:
```sh
streamlit run app.py
```

## Deployment

The application is deployed on Streamlit Cloud. To deploy your own version:
1. Push your project to GitHub.
2. Go to [Streamlit Cloud](https://share.streamlit.io/) and sign in.
3. Create a new app and link your GitHub repository.
4. Select `app.py` as the entry point.
5. Deploy and access your app via the provided link.

## Model Training
The model is trained using a machine learning pipeline with preprocessing steps, including encoding categorical variables and feature engineering.

## Author
- **Your Name**  
- LinkedIn: [Your LinkedIn](https://linkedin.com/in/risaalkhan)
- GitHub: [Your GitHub](https://github.com/risaal-khan)

## License
This project is licensed under the MIT License.

