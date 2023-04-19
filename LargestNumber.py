import streamlit as st

a = st.numberinput('Enter first number  : ')
b = st.numberinput('Enter second number : ')
c = st.numberinput('Enter third number  : ')

largest = 0

if a > b and a > c:
    largest = a
if b > a and b > c:
    largest = b
if c > a and c > b:
    largest = c

st.write(largest, "is the largest of three numbers.")
