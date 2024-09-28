import streamlit as st

picture=st.camera_input("Take a Picture")
if picture is not None:
    st.image(picture)