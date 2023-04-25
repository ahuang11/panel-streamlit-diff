import streamlit as st

# set package value
st.session_state.package = "Streamlit"

package = st.selectbox("Package", ["Panel", "Streamlit"], key="package")

# get package value
st.write(f"Selected package: {package}")