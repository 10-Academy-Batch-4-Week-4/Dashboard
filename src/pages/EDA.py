import streamlit as st

def write():
    st.title(" Swahili Speech To Text ")
    st.write("""
    # Exploratory Data Analysis
    """)
    st.header("Analysis of Audio Duration")
    st.subheader("Distribution of Duration")
    st.image('images/distribution_of _duration.png')
    st.write("""
    Most of the audio has a duration of between 2.25sec to 2.6sec.The max duration is 6.1s and the min duration is also 2.1s
    """)

    st.subheader("Outlier Detection for Duration")
    st.image('images/outliner_distribution.png')

    st.write("""
    #### The above plot show us we have no outlier in the audio data duration
    """)

    st.header("Analysis of Audio Transcription")
    st.subheader("Distribution of Transcription Length")
    st.image('images/dist_of_trans_len.png')
    st.write("""
    Most of the audio has a transcription lenght of 40 characters. The max transcription length is 121characters  and the min transcription length is 5 characters
    """)

    st.subheader("Distribution of Character per sec")
    st.image('images\dist_char_per_sec.png')

