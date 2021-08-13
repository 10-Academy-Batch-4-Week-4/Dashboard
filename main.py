import aboutUs
import EDA
import home
import streamlit as st

PAGES = {
    "Home":home,
    "Exploring the Data" : EDA,
    "About Us": aboutUs
}

st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()