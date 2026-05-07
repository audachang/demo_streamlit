import streamlit as st

num = st.number_input('Pick a number', 0, 10)
email = st.text_input('Email address')
travel_date = st.date_input('Traveling date')
school_time = st.time_input('School time')
description = st.text_area('Description')
photo = st.file_uploader('Upload a photo')
color = st.color_picker('Choose your favorite color')


st.write(f"number: {num}")
st.write(f"email: {email}")
st.write(f"travel_date: {travel_date}")
st.write(f"school_time: {school_time}")
st.write(f"description: {description}")
st.image(photo)
#st.write(f"color: {color}")
