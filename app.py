import streamlit as st

st.title('testumair2')
st.write('Welcome to testumair!')
email = st.context.headers["x-email"]
st.write(f'User2: {email}')
