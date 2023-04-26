import time
import streamlit as st

with st.expander("Expand", expanded=True):
    button = st.button("Click me")
    placeholder = st.empty()
    placeholder.text("Waiting to be deleted.")
    if button:
        time.sleep(3)
        placeholder.empty()
    st.text_input("Just to show I'm dimmed.")