# app.py
import streamlit as st
import pandas as pd
import joblib

# Load the model
model = joblib.load('best_model_pipeline.pkl')

# Define the input format
input_format = {
    "Industry": 'NAICS',
    "State": 'State',
    "Company Size": 'NoEmp',
    "Term": 'Term',
    "New Business": 'NewExist'
}

# Define a function to take user input and return a DataFrame
def user_input_features():
    Industry = st.selectbox('Industry', ['Technology', 'Finance', 'Healthcare', 'Education'])
    State = st.selectbox('State', ['CA', 'TX', 'NY', 'FL'])
    Company_Size = st.slider('Company Size', 1, 1000, 50)
    Term = st.slider('Term', 1, 60, 36)
    New_Business = st.selectbox('New Business', [1, 0])
    
    data = {
        'Industry': Industry,
        'State': State,
        'NoEmp': Company_Size,
        'Term': Term,
        'NewBusiness': New_Business
    }
    features = pd.DataFrame(data, index=[0])
    return features

# Title
st.title('Business Loan Approval Prediction')

# Sidebar for user input
st.sidebar.header('User Input Features')
df = user_input_features()

# Display user input
st.subheader('User Input Features')
st.write(df)

# Make predictions
prediction_proba = model.predict_proba(df)[:, 1]
st.subheader('Prediction')
st.write(f'Approval Probability: {prediction_proba[0]:.2f}')

if __name__ == '__main__':
    st.run()
