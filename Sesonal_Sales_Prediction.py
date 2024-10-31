import streamlit as st
import pickle
import pandas as pd
import datetime
from datetime import date,timedelta

loaded_model = pickle.load(open('D:/Monthly_Sales_Prediction/seasonalpklt5.sav', 'rb'))

Start_Date = st.date_input("Start Date", date(2025, 1, 1))
End_Date = st.date_input("End Date", date(2025, 5, 1))
button = st.button("Predict")

if button:
    prediction = loaded_model.predict(Start_Date, End_Date)
    st.write("Seasonal Sales Forecust :", prediction)
