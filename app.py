import streamlit as st

# Add a title to your app
st.title("Travel Cost Optimization Tool")
x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)
st.text_input("Your name", key="name")

# You can access the value at any point with:
st.session_state.name
y = st.slider('y')  # 👈 this is a widget
st.write('Your age is', y)
z = x+y
st.write(' ans:', z)
