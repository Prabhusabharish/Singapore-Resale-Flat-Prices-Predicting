impoer pandas as pd
import streamlit as st 





# - - - - - - - - - - - - - - -set st addbar page - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

icon = Image.open("C:/Users/prabh/Downloads/Datascience/Project/Copper/1.png")
st.set_page_config(page_title= "BizCardX: Extracting Business Card Data with OCR",
                   page_icon= icon,
                   layout= "wide",
                   initial_sidebar_state= "expanded")

# - - - - - - - - - - - - - - -set bg image - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

def setting_bg():
    st.markdown(f""" <style>.stApp {{
                        background: url("https://cutewallpaper.org/28/copper-hd-wallpaper/16624879.jpg");
                        background-size: cover}}
                     </style>""",unsafe_allow_html=True) 
setting_bg()



# - - - - - - - - - - - - - - -sidebar - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

st.sidebar.title("Navigation")
select_page = st.sidebar.radio("", ["Home", "Application"])

# - - - - - - - - - - - - - - -Home page - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# Home page creation
if select_page == "Home":
    st.title("Home Page")

    st.markdown("""
            Technologies Used:
            - Python
            - Pandas
            - Numpy
            - Seaborn
            - sklearn
            - Pickle
            - Regression or Classification
            - Streamlit
            
            Features:
            - xxx
            """)


# ------------------------------ Explore Data Page ----------------------#
elif select_page == "Application":
    st.title("Industrial Copper Modeling Application")
