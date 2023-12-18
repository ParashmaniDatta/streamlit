import streamlit as st
st.title('Welcome to find largest of 3 numbers')
num1=st.number_input('Enter First number')
num2=st.number_input('Enter Second number')
num3=st.number_input('Enter Third number')
if (num1 > num2) and (num1 > num3):
   largest = num1
elif (num2 > num1) and (num2 > num3):
   largest = num2
else:
   largest = num3
st.title("The largest number is:")
st.write(largest)