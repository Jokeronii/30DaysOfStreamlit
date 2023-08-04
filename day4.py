import streamlit as st

st.header("common slider")

age = st.slider('tes slider',0,200,30)
st.write("the age value is: ",age)

st.header("range slider")

val = st.slider('slide range',0.0,100.0,(2.5,75.5))
st.write("the value is: ",val)

from datetime import datetime, time

st.header("time slider appointment")

timeAppointment = st.slider('time appointment',time(00,00),time(23,59),(time(13,15),time(16,20)))
st.write("the set time is: ",timeAppointment)


st.subheader('date slider')

start_time= st.slider('date slider',
             value = datetime(1970,11 ,1,6,30),
             format = 'MM-DD-YY -HH:mm'
             )
st.write('the set date is: ',start_time)