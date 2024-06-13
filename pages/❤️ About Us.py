#Import Modules
import streamlit as st

#Configure Page
st.set_page_config(
    page_title="About Us",
    page_icon="💵",
)


#***************************************************************************************#
#First Row
left_co, cent_co,last_co = st.columns([1,3,1])
with cent_co:
    st.image("./images/main_logo.png")
st.title("About Us")
st.subheader("Sustainability | Accessibility | Inclusivity")
st.write("")
st.write(f"""
Welcome to our loan eligibility checker app! We are a team of passionate developers and data scientists who have come together to create a user-friendly solution to help individuals determine their eligibility for a loan from a bank.

At our core, we believe in leveraging the power of machine learning and advanced analytics to simplify complex financial processes. Through meticulous analysis and utilizing cutting-edge libraries such as scikit-learn and PyTorch, we've developed a robust model that accurately predicts loan eligibility based on various factors.

Our mission is to :orange[empower users with the knowledge they need to make informed financial decisions]. Whether you're looking to fund your dream home, pursue higher education, or expand your business, our app provides you with insights into your loan eligibility quickly and efficiently.

We understand that navigating the loan application process can be daunting, which is why we've designed our :orange[app to be intuitive and user-friendly]. With just a few clicks, you can input your information and receive instant feedback on your eligibility status.

Transparency and accuracy are at the forefront of everything we do. :orange[Our model is built on extensive data analysis and is continuously refined to ensure reliable results]. We are committed to providing you with a trustworthy tool that you can rely on when exploring your loan options.

Thank you for choosing our loan eligibility checker app. We're excited to be part of your financial journey and look forward to helping you achieve your goals.
         """)