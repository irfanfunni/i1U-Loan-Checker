import streamlit as st
import time
import random

#To input function for data analysis here. 

#Configure and Style Page
st.set_page_config(
    page_title="Homepage",
    page_icon="🌈",
)

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{

background: #030303;
background: linear-gradient(135deg, #030303, #302F2F);
}}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

#Create Functions
# #Insert border between Rows
def border():
    with st.container():
        st.write("")
        st.divider()
        st.write("")

#First Row
left_co, cent_co,last_co = st.columns([1,3,1])
with cent_co:
    st.image("./images/logo_dark.png")
    
st.title("Loan Eligibility Calculator")
st.markdown("Disclaimer: The data provided will not be recorded. If a report is requested, the generated report will not be saved either.")


#Variables needed: zipcodes/postalcode, amount_requested, loan_amount, business info location etc. 
#Meant for individual businesses 
#Confirmed variables : Zip, NAICS(),DisbursementGross,NewExist,SBA_Appv - abit like guarantor, current employee size , expected employee size after loan?
#Outcome will be: Yes and No
#Chances: default 
#Another outcome: Previous businesses closest to your company have loaned of a certain amount. Based on yr requested loan details, similar businesses have received up to $xxxxxx amount. 

#Transparency for the loan processes. 
#Accessibility to quality data and insights. 

# Connect LLM to Streamlit 


border()

#Second Row
# Initialize the dictionary in session state if it doesn't exist
if "user_data" not in st.session_state:
    st.session_state["user_data"] = {}

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

            with st.spinner("Checking"):
                time.sleep(5)
            st.success(":white_check_mark: Output Generated Successfully!")
            print(st.session_state["user_data"])
            #Execute ML and Analysis Component

    return st.session_state["user_data"]

get_user_details()
print(st.session_state["user_data"])

#Output
output = f"""
You are __________ for a bank loan with a ____% chance of success. 

Companies of Similar Profile like yours have borrowed a loan of about $______________ in the past. 
"""

border()

#Third Row - Output
@st.experimental_fragment
def generate_output():
    with st.container():
        st.subheader("Generated Output")
        #Generate Report in txt file
        #Pass Generated Output to report_generator()
        with st.container(border = True):
            if st.session_state["user_data"]:
                st.write(output)
            else: 
                st.write("")
        text_contents = "noseyy"
        id = str(random.randint(0,100001))
        file_name = f"i1UniversityEligibilityCHecker_{id}.txt"
        # st.download_button("Download Report", text_contents, file_name=file_name)
        if st.download_button("Download Report", text_contents, file_name = file_name ,disabled = not None):   
            st.success("Output Generated Successfully! :smile:")
            print()
        
generate_output()
