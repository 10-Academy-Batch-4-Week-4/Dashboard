# import the child scripts
import streamlit as st
import awesome_streamlit as ast
import src.pages.home
import src.pages.EDA 
import src.pages.aboutUs
#import src.pages.transcribe
import src.pages.pred

ast.core.services.other.set_logging_format()

# create the pages
PAGES = {
    "Home": src.pages.home,
    "Data visualisations":src.pages.EDA,
    #"Predictions": src.pages.transcribe,
    "Prediction demo":src.pages.pred,
    "About Us": src.pages.aboutUs,
}


# render the pages
def main():
   
    st.sidebar.title("Transcription")
    selection = st.sidebar.selectbox("Select", list(PAGES.keys()))

    page = PAGES[selection]

    with st.spinner(f"Loading {selection} ..."):
        ast.shared.components.write_page(page)
    if selection =="Home":
        st.sidebar.title("INFORMATION")
        st.sidebar.info(
        """
        This App is created for The World Food Program to 
        transcribe the speech-to-text of Swahili Language. 
        """
    )
    elif selection=="Predictions":
        st.sidebar.title("")


if __name__ == "__main__":
    main()

