import streamlit as st

def write():
    st.title(" Swahili Speech To Text ")
    st.write("""
    # About Group 5

    ## Team members
    """)

    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.header("Zelalem")

        st.text_area('Zelalem', '''
        ...     It was the best of times, it was the worst of times, it was
        ...     the age of wisdom, it was the age of foolishness, it was
        ...     the epoch of belief, it was the epoch of incredulity, it
        ...     was the season of Light, it was the season of Darkness, it
        ...     was the spring of hope, it was the winter of despair, (...)
        ...     ''')

    with col2:
        st.header("Euel Fantaye")
        st.image("images/Eyuel.jpg")

        st.text_area('Euel Fantaye', '''
        ...    I am an Electrical and Computer Engineering graduate form Addis Ababa University Institute of Technology (AAiT). I live in Addis Ababa, Ethiopia.
        ...     the age of wisdom, it was the age of foolishness, it was
        ...     I helped the project in Setting up team git repository 
        ...     projects assignment,DVC, MLFlow, and CML integration,
        ...     preparing the metadata for easily accessible JSON format, helped(...)
        ...     the team in AWS server setup, and partially helped in the modeling & testing process.
        ...     ''')

    with col3:
        st.header("Bereket")
        st.image("images/beki.jpg")
        st.text_area("La clé du succès est de commencer avant d'être prêt!!!")


    col4, col5, col6 = st.columns(3)
    with col4:
        st.header("Njoki")

    with col5:
        st.header("Bezawit")

    with col6:
        st.header("Leul")

    col7, col8, col9 = st.columns(3)

    with col7:
        st.header("Binyam Sisay")
        st.image("images/binyam.jpg")

        st.text_area('Binyam Sisay', '''
        ...    I am an Electrical and Computer Engineering graduate form Addis Ababa University Institute of Technology (AAiT). I live in Addis Ababa, Ethiopia.
        ...     the age of wisdom, it was the age of foolishness, it was
        ...     I helped the project in Setting up team git repository 
        ...     projects assignment,DVC, MLFlow, and CML integration,
        ...     I also helped the team in providing with building a beautiful dashboard 
        ...     ''')


    with col8:
        st.header("Maelaf Estiphanos")
        st.image("images/mafi.jpg")

        st.text_area('Maelaf', '''
        ...    MLOPS engineer
        ...     ''')

    with col9:
        st.header("Aberaham")


