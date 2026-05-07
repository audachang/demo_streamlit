import streamlit as st
import time

st.pills()
progress_bar = st.progress(0)
for percent in range(100):
    time.sleep(0.05)
    progress_bar.progress(percent + 1)
with st.spinner('Wait for it...'):
    time.sleep(2)
st.success("You did it!")
st.error("Error occurred")
st.warning("This is a warning")
st.info("It's easy to build a Streamlit app")
st.exception(RuntimeError("RuntimeError exception"))
