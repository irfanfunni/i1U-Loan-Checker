import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Data Analysis",
    page_icon="🌈",
)

parameter_dict = dict(delimiter=",",
                      dtype=[('Loan_ID', 'i8'),('Gender','U8'),('Married', 'bool'),('Dependent_No', 'i8'),('Education', 'U16'),('Self_Employed', 'bool'),('Applicant_Income', 'i8'),('CoApplicant_Income','i8'),('Loan_Amount','i8'),('Loan_Amount_Term','i8'),('Credit History','i8'),('Property_District','U8'),('Loan_Status','i8')],
                      names=True)
raw_data = np.genfromtxt('./datasets/partial_loan_dataset.csv', **parameter_dict)
filtered_data = np.array([row for row in raw_data if row[0] != -1 and row[1] != -1 and row[2] != -1 and row[3] != -1 and row[4] != -1 and row[5] != -1 and row[6] != -1 and row[7] != -1 and row[8] != -1 and row[9] != -1 and row[10] != -1 and row[11] != -1 ])
genders = np.array([row[1] for row in filtered_data])
birth_rates = np.array([row[1] for row in filtered_data])
print(genders)
print(len(genders))