import pandas as pd
import streamlit as st
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


df = pd.DataFrame({
    "season" : ["Springer","Summer", "Fall", "Winter"],
    "total penyewaan" : [471348, 918589, 1061129, 841613]
})

springer_df = pd.DataFrame({
    "User type" : ["Casual","Registered"],
    "Rental amount" : [60622, 410726]
})

summer_df = pd.DataFrame({
    "User type" : ["Casual","Registered"],
    "Rental amount" : [203522, 715067]
})

fall_df = pd.DataFrame({
    "User type" : ["Casual","Registered"],
    "Rental amount" : [226091, 835038]
})

winter_df = pd.DataFrame({
    "User type" : ["Casual","Registered"],
    "Rental amount" : [129782, 711831],
})


st.title('Bike Sharing Dashboard')

st.metric(label="Total bike rental", value="3292679")
st.write ("The number of rentals based on the weather status")
weather_df = pd.DataFrame({
    "level" : ["1","2","3"] ,
    "total" : [2257952,996858,37869],
})

st.bar_chart (weather_df,x='level', color='#ff4500',y='total' )

img = Image.open ('assets/yelow 2.png')
new_size = img.resize ((250,250))
st.sidebar.image(new_size)

gk=pd.DataFrame({'musim':["category...","Springer","Summer", "Fall", "Winter"]})

cfd=st.sidebar.selectbox('Please select season:', gk['musim'])
if cfd == "Springer":
    st.write ("The number of rentals based on the Season")
    st.bar_chart(springer_df, x="User type",color="#e6cc00", y="Rental amount")
if cfd == "Summer":
    st.write ("The number of rentals based on the Season")
    st.bar_chart (summer_df, x="User type",color="#e47200", y="Rental amount")
if cfd == "Fall" :
   st.write ("The number of rentals based on the Season")
   st.bar_chart (fall_df,x="User type", color="#f7f5bc", y="Rental amount")
if cfd == "Winter" :
   st.write ("The number of rentals based on the Season")
   st.bar_chart (winter_df,x="User type", y="Rental amount")  











