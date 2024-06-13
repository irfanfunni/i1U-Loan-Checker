#Import Modules
import streamlit as st
import time
import random
from datetime import datetime
import joblib

#Configure Page
st.set_page_config(
    page_title="Homepage",
    page_icon="💵",
)

#Load the model 
model = joblib.load('best_model_pipeline_random.pkl')

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
    
st.title("Loan Eligibility Checker")
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

        #Industry
        Industry = st.selectbox("Enter your Industry", ("",set(['Ag/For/Fish/Hunt','Min/Quar/Oil_Gas_ext','Utilities','Construction','Manufacturing','Manufacturing','Manufacturing','Wholesale_trade','Retail_trade','Retail_trade','Trans/Ware','Trans/Ware','Information','Finance/Insurance','RE/Rental/Lease','Prof/Science/Tech','Mgmt_comp','Admin_sup/Waste_Mgmt_Rem','Educational','Healthcare/Social_assist','Arts/Entertain/Rec','Accom/Food_serv','Other_no_pub','Public_Admin'])))
        
        #ZipCode
        State = st.selectbox("Select state code",("",'IN', 'OK', 'FL', 'CT', 'NJ', 'NC', 'IL', 'RI', 'TX', 'VA', 'TN', 'AR', 'MN', 'MO','MA', 'CA', 'SC', 'LA', 'IA', 'OH', 'KY', 'MS', 'NY', 'MD', 'PA', 'OR', 'ME', 'KS','MI', 'AK', 'WA', 'CO', 'MT', 'WY', 'UT', 'NH', 'WV', 'ID', 'AZ', 'NV', 'WI', 'NM','GA', 'ND', 'VT', 'AL', 'NE', 'SD', 'HI', 'DE', 'DC'))       

        #Number of Employees
        NoEmp = st.number_input("Enter number of employees",min_value = 0, step = 1)
        
        #Loan Amount
        GrAppv = st.number_input("Enter loan amount",min_value = 0.0)
        
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
                "Industry": Industry,
                "State": State,
                "NoEmp": NoEmp,
                "GrAppv": GrAppv,
                "Term" : Term,
                "NewExist": NewExist
            }
            st.session_state['data_filled'] = True
            with st.spinner("Checking"):
                time.sleep(5)
            st.success(":white_check_mark: Output Generated Successfully!")
            st.experimental_rerun()
           
    return st.session_state["user_data"]

get_user_details()
#Execute ML and Analysis Component
predictions = {}

#Initialise output message
output = ""
if st.session_state['data_filled'] and st.session_state['user_data']:
    st.write("Ok can run ML liao")
    now = datetime.now()
    report_date_time = now.strftime("%d-%b-%Y %H:%M:%S")
    output = f"""
You are {predictions} for a bank loan with a {predictions}% chance of success. 

Companies of similar profile like yours have borrowed a loan of about ${predictions} in the past. 

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

