import streamlit as st
st.checkbox('Yes')
st.button('Click Me')
id = st.radio('Pick your image id', ['Doraemon', 'Baki'])
fruit = st.selectbox('Pick a fruit', ['Apple', 'Banana', 'Orange'])
planets = st.multiselect('Choose a planet', ['Jupiter', 'Mars', 'Neptune'])
mark = st.select_slider('Pick a mark', ['Bad', 'Good', 'Excellent'])
number = st.slider('Pick a number', 0, 50)


st.write(f"id: {id}")
st.write(f"fruit: {fruit}")
st.write(f"planets: {planets}")
st.write(f"mark: {mark}")
st.write(f"number: {number}")   

if id == 'Doraemon':
    st.image("frieren+doraemon.png", caption="Frieren Dancing with Doraemon")
elif id == 'Baki':
    st.image("frieren+baki.png", caption="Frieren Dancing with Baki")