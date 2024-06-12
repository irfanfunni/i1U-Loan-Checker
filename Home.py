import streamlit as st
import time
import random

#To input function for data analysis here. 

st.set_page_config(
    page_title="Homepage",
    page_icon="🌈",
)
left_co, cent_co,last_co = st.columns(3)
with cent_co:
    st.image("./images/logo_dark.png")

st.title("Loan Eligibility Calculator")
st.markdown("Disclaimer: The data provided will not be recorded")

#First Row
@st.experimental_fragment
def get_user_details():
    user_details = {}
    with st.container():
        st.subheader("Please enter your details")
        #Gender
        gender = st.selectbox("Gender",("","Male","Female","Others"),placeholder = "Select Gender")
        user_details["gender"] = gender
        
        #Marriage Status
        marriage_status = st.selectbox("Marriage Status",("","Married","Single","Widowed"), placeholder = "Select Marriage Status")
        user_details["marriage_status"] = marriage_status

        #Number of Dependents
        
        dependent_num = st.number_input("Dependent Number",placeholder= "Select Dependant Number",step = 1,min_value = 0)
        st.write("*Dependants refer to the number of people who rely on you for money*") #To change this
        user_details["dependent_num"] = dependent_num
        
        #Education
        education_level = st.selectbox("Education Level",("","Olevel","Alevel","Diploma","Masters","phd"), placeholder = "Select Education Level")
        user_details["education_level"] = education_level
        
        #Self-employed
        is_self_employed = st.radio("Are you self-employed",("No","Yes"))
        user_details["is_self_employed"] = is_self_employed
        
        #Applicant_Income
        applicant_income = st.number_input("Enter Income",placeholder="Income",min_value = 0.0)
        user_details["applicant_income"] = applicant_income
        
        #CoApplicant_income
        coApplicant_income = 0
        have_coApplicant = st.radio("Do you have a Co-Applicant",("No","Yes"))
        if have_coApplicant == "Yes": 
            coApplicant_income = st.number_input("Enter your co-applicant income",min_value = 0.0)
            user_details["coApplicant_income"] = coApplicant_income
        
        #Loan Amount
        loan_amount = st.number_input("Enter your loan Amount", min_value = 0.0)
        user_details["loan_amount"] = loan_amount
        
        #Loan Amount Term
        loan_term = st.number_input("Enter loan term in months",min_value = 0, step = 1)
        user_details["loan_term"] = loan_term
        
        #Credit History
        credit_history = st.radio("Enter your credit history",("No","Yes"))
        if credit_history == "No":
            user_details["credit_history"] = 0
        elif credit_history == "Yes":
            user_details["credit_history"] = 1
        
        #Property District
        #CCR - Core Central Region
        core_central_region_districtcode = ["09","10","11"]
        core_central__region_postalcode = ["22","23","24","25","26","27","28","29","30"]
        
        #RCR - Remaining Central Region 
        remaining_central_region_districtcode = ["01","02","03","04","06","07","12","13","14","21","26"]
        remaining_central_region_postalcode = ["01","02","03","04","05","06","07","08","14","15","16","09","10","17","18","19","20","21","31","32","33","34","35","36","37","38","39","40","41","58","59","77","78"]
        #OCR - Outside Central Region
        outside_central_region_districtcode = ["05","22","23","24","25","27","19","20","28","15","16","17","18"]
        outside_central_region_postalcode = ["11","12","13","60","61","62","63","64","65","66","67","68","69","70","71","72","73","75","76","53","54","55","82","56","57","79","80","42","43","44","45","46","47","48","49","50","81","51","52"]
 
        postal_code = st.text_input("Enter your postal code")[0:2]
        
        if postal_code in core_central__region_postalcode:
            user_details["property_district"] = "CCR"
        elif postal_code in remaining_central_region_postalcode:
            user_details["property_district"] = "RCR"
        elif postal_code in outside_central_region_postalcode:
            user_details["property_district"] = "OCR"

        #PDPA Agreement
        is_pdpa_agreed = st.checkbox(":red[*]I have read and agree with the data privacy policy as referenced by the Personal Data Protection Act (PDPA)") 
        
        #Have all fields been field? 
        can_submit = gender and marriage_status and credit_history and applicant_income and loan_amount and have_coApplicant and loan_term and postal_code and is_pdpa_agreed
   
        #     st.warning("All fields must be filled!")
        if st.button("Generate Report", type = "primary", disabled = not can_submit):   
            st.success("Output Generated Successfully! :smile:")
            st.rerun()
        
    return user_details
user_details = get_user_details()

print(user_details)

#Set Divider
st.divider()

#Second Row - Output
@st.experimental_fragment
def generate_report():
    with st.container(border = True):
        st.write("Generated Output")
        #Generate Report in txt file
        #Pass Generated Output to report_generator()
        text_contents = "noseyy"
        id = str(random.randint(0,100001))
        file_name = f"i1UniversityEligibilityCHecker_{id}.txt"
        # st.download_button("Download Report", text_contents, file_name=file_name)
        if st.download_button("Download Report", text_contents, file_name = file_name ,disabled = not None):   
            st.success("Output Generated Successfully! :smile:")
            print()
        
generate_report()