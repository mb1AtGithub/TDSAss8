import streamlit as st

st.write("""
# This app will check whether the number given by user is even or odd
""")
#Get Input

st.header('Enter your number')

num  = st.number_input("Number")

op = ""

if num ==0 :
  op= "your number is even."
if num%2 == 1:
  op= "your number is even."
else:
  op= "your number is odd." 

st.write(op)
