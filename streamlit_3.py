import streamlit as st

if "counter" not in st.session_state:
    st.session_state.counter = 0

button = st.button(label="Click me!")

# add interactivity
if button:
    st.session_state.counter += 1

st.text(f"Clicks: {st.session_state.counter}")
