import streamlit as st

#Streamlit UI
st.title('Power Calculator')
st.write('Enter a number to calculate its square , cube and fifth power')

n=st.number_input('Enter a number',value=1,step=1)

#calculate results
sq=n**2
cu=n**3
fi=n**5

#Display results
st.write(f'The square of {n} is {sq}')
st.write(f'The cube of {n} is {cu}')
st.write(f'The fifth power of {n} is {fi}')