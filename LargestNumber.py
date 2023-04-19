import streamlit as st

a = st.number_input('Enter first number  : ')
b = st.number_input('Enter second number : ')
c = st.number_input('Enter third number  : ')

largest = 0

if a > b and a > c:
    largest = a
if b > a and b > c:
    largest = b
if c > a and c > b:
    largest = c
if st.button('Find Largest'):
    st.write(largest, "is the largest of three numbers.")
