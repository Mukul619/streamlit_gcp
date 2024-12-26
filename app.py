import os
import streamlit as st
import streamlit.web.cli as stcli

# Retrieve the port from the environment variable
port = int(os.environ.get("PORT", 8080))

# Start the Streamlit app on the specified port
st.title("My Streamlit App")
st.write("Welcome to my Streamlit app deployed on Google Cloud Run!")


