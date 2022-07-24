import streamlit as st


st.title('Odd-Even Finder')

st.write("""
# This app will check whether the number given by user is even or odd
""")
#Get Input


num  = st.number_input("Enter a Number")

op = ""

if num ==0 :
  op= "your number is even."
if num%2 == 1:
  op= "your number is odd."
elif num%2 == 0 :
  op= "your number is even." 
else:
  op= "Please enter an integer" 
  
st.write(op)
