#Import Modules
import streamlit as st
import time
import random
from datetime import datetime

#Configure Page
st.set_page_config(
    page_title="Homepage",
    page_icon="💵",
)

#Create Functions
#Border Function to Create Borders
def border():
    with st.container():
        st.write("")
        st.divider()
        st.write("")

#***************************************************************************************#
#First Row
left_co, cent_co,last_co = st.columns([1,3,1])
with cent_co:
    st.image("./images/main_logo.png")
    
st.title("Loan Eligibility Calculator")
st.markdown("Disclaimer: The data provided will not be recorded. If a report is requested, the generated report will not be saved either.")

border()

#***************************************************************************************#
#Second Row
# Initialize the dictionary in session state if it doesn't exist
if "user_data" not in st.session_state:
    st.session_state["user_data"] = {}

if 'data_filled' not in st.session_state:
    st.session_state['data_filled'] = False

@st.experimental_fragment
def get_user_details():
    with st.container():
        st.subheader("Please enter your organisation details")

        #North American Industry Classification System (NAICS) Code
        NAICS = st.text_input("Enter NAICS code", placeholder="e.g. 451120")
        
        #change to statecode 
        #ZipCode
        State = st.selectbox("Select state code",('IN', 'OK', 'FL', 'CT', 'NJ', 'NC', 'IL', 'RI', 'TX', 'VA', 'TN', 'AR', 'MN', 'MO','MA', 'CA', 'SC', 'LA', 'IA', 'OH', 'KY', 'MS', 'NY', 'MD', 'PA', 'OR', 'ME', 'KS','MI', 'AK', 'WA', 'CO', 'MT', 'WY', 'UT', 'NH', 'WV', 'ID', 'AZ', 'NV', 'WI', 'NM','GA', 'ND', 'VT', 'AL', 'NE', 'SD', 'HI', 'DE', 'DC'))       

        #Number of Employees
        NoEmp = st.number_input("Enter number of employees",min_value = 0, step = 1)

        #Loan Term in Months
        Term = st.number_input("Enter loan term in months",min_value = 0, step = 1)

        #Company Age
        company_age = st.radio("Is your company more than 2 years old?",("No","Yes"))

        if company_age == "No":
            NewExist = 2 #New Business
        elif company_age == "Yes":
            NewExist = 1 #Existing Business

        #PDPA Agreement
        is_pdpa_agreed = st.checkbox(":red[*]I have read and agree with the data privacy policy as referenced by the Personal Data Protection Act (PDPA)") 
        
        #Have all fields been field? 
        can_submit = NAICS and State and NoEmp and Term and NewExist and is_pdpa_agreed

        if st.button("Check Eligibility", type = "primary", disabled = not can_submit): 
            # Update the session state dictionary with user inputs
            st.session_state["user_data"] = {
                "NAICS": NAICS,
                "State": State,
                "NoEmp": NoEmp,
                "Term" : Term,
                "NewExist": NewExist
            }
            st.session_state['data_filled'] = True
            with st.spinner("Checking"):
                time.sleep(5)
            st.success(":white_check_mark: Output Generated Successfully!")
            st.experimental_rerun()
            #Execute ML and Analysis Component

    return st.session_state["user_data"]

get_user_details()
#Execute ML and Analysis Component
# st.write("Debug: Data filled status:", st.session_state['data_filled'])
# st.write("Debug: Current user data:", st.session_state['user_data'])
output = ""
if st.session_state['data_filled'] and st.session_state['user_data']:
    st.write("Ok can run ML liao")
    report_date_time = f"{datetime.now():%d-%b-%Y %I:%M:%S %p}"
    output = f"""
You are __________ for a bank loan with a ____% chance of success. 

Companies of Similar Profile like yours have borrowed a loan of about $______________ in the past. 

Date: {report_date_time.split(" ")[0]}  
Time: {report_date_time.split(" ")[1]}
"""

border()
#***************************************************************************************#
#Third Row - Output
@st.experimental_fragment
def generate_output():
    with st.container():
        st.subheader("Generated Output")
        #Generate Report in txt file
        #Pass Generated Output to report_generator()
        with st.container(border = True):
            if st.session_state['data_filled']:
                st.write(output)  
            else: 
                st.write("")
        id = str(random.randint(0,100001))
        file_name = f"i1LoanEligibilityChecker_{id}.txt"
        if st.download_button("Download Report", output, file_name = file_name ,disabled = not st.session_state['data_filled']):   
            st.success("Report Generated Successfully! :smile:")
            
   
generate_output()

