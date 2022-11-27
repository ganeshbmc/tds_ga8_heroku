import streamlit as st

st.write("""
# Subtracting two numbers
This app takes two numbers as input, subtracts the second number from the first number and outputs the result
""")

#Get Input

st.header('Input Parameters')


num_1 = st.number_input('Enter first number')
num_2 = st.number_input('Enter second number')
    

data = {'First_Number': num_1,
        'Second_Number': num_2,
        }


st.subheader('User input parameters')
st.write(data)

# Subtraction

result = data['First_Number'] - data['Second_Number']

#Output

st.subheader('Result of subtraction is:')
st.write(result)