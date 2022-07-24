import streamlit as st




st.write("""
# This app will check whether the number given by user is even or odd
""")
#Get Input

st.title('Odd-Even Finder')

num  = st.number_input("Enter a Number")

op = ""

if num ==0 :
  op= "your number is even."
if num%2 == 1:
  op= "your number is odd."
else:
  op= "your number is even." 

st.write(op)
