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
        
#Generate report
def generate_report (user_details,output):
    report_date_time = f"{datetime.now():%d-%b-%Y %H:%M}"
    #Check company age
    if user_details["NewExist"] == 2: 
        company_age = "Less than or equal to 2 years old"
    elif user_details["NewExist"] == 1: 
        company_age = "Greater than 2 years old"
    #This is the overall report that will be generated. 
    report = f"""\
____________________________________________________________________________________________________
*********************************i1Loan Loan Eligibility Checker************************************

Group : i1
____________________________________________________________________________________________________
***************************************Report Details***********************************************

Date: {report_date_time.split(" ")[0]}
Time: {report_date_time.split(" ")[1]}

____________________________________________________________________________________________________
****************************************User Details************************************************

NAICS: {user_details["NAICS"]}
ZipCode: {user_details["Zip"]}
Number of Employees: {user_details["NoEmp"]}
Loan Term (in months): {user_details["Term"]}
Company age: {company_age}

___________________________________________________________________________________________________
********************************************Outcome*************************************************

{output}

____________________________________________________________________________________________________

Thank you for using i1's University Eligibility Checker! See you again!


*****************************************End of Report**********************************************
"""
    return report

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
        st.subheader("Please enter your details")

        #North American Industry Classification System (NAICS) Code
        NAICS = st.text_input("Enter NAICS Code", placeholder="e.g. 451120")

        #ZipCode
        Zip = st.text_input("Enter ZipCode",placeholder="e.g. 47711")       

        #Number of Employees
        NoEmp = st.number_input("Enter Number of Employees",min_value = 0, step = 1)

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
        can_submit = NAICS and Zip and NoEmp and Term and NewExist and is_pdpa_agreed

        if st.button("Check Eligibility", type = "primary", disabled = not can_submit): 
            # Update the session state dictionary with user inputs
            st.session_state["user_data"] = {
                "NAICS": NAICS,
                "Zip": Zip,
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

if st.session_state['data_filled'] and st.session_state['user_data']:
    st.write("Ok can run ML liao")
    output = f"""
You are __________ for a bank loan with a ____% chance of success. 

Companies of Similar Profile like yours have borrowed a loan of about $______________ in the past. 
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
  
        text_contents = generate_report(st.session_state["user_data"],output)
        id = str(random.randint(0,100001))
        file_name = f"i1LoanEligibilityChecker_{id}.txt"
        if st.download_button("Download Report", text_contents, file_name = file_name ,disabled = not st.session_state['data_filled']):   
            st.success("Report Generated Successfully! :smile:")
            
   
generate_output()

