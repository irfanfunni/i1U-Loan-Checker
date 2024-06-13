from datetime import datetime

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
