import streamlit as st

st.write("""
# This app will check whether the number given by user is even or odd
""")
#Get Input

st.header('Enter your number')

num  = st.number_input("Number")

