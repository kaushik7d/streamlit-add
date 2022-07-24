import streamlit as st

st.title('Addition of 2 given numbers')
a = st.number_input('Enter first number')
b = st.number_input('Enter second number')
result = a + b
st.write(a, ' + ', b , '= ', result)
