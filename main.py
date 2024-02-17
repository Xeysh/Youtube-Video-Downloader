import streamlit as st
import pytube

url = st.text_input("Please input your video URL to download.")

try:
    if len(url) > 0:

        s = st.info("Please wait until process completed...")

        video = pytube.YouTube(url)
        stream = video.streams.get_highest_resolution()

        download = stream.download()

        with open(download,"rb") as f:
            btn = st.download_button(
                label="Download the video.",
                data=f,
                file_name="video.3gpp",
                mime="video/3gpp",
                key="download_button"
            )

        s.empty()

    else:
        st.info("Input your URL to box.")
except:
    s.empty()
    st.warning("Please enter a valid URL.")
