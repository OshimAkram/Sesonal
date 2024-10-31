import streamlit as st
import pickle
import pandas as pd
import datetime
from datetime import date,timedelta




st.title("Seasonal Sales Data")
excel_file='Hot_Winter_Sales.xlsx'
sheet_name='Sheet1'

df = pd.read_excel(excel_file,
                  sheet_name=sheet_name,
                   usecols='B:C',
                   header=1)
st.dataframe(df)
st.title("Seasonal Sales Prediction")
loaded_model = pickle.load(open('D:/Monthly_Sales_Prediction/seasonalpklt5.sav', 'rb'))

Start_Date = st.date_input("Start Date", date(2025, 1, 1))
End_Date = st.date_input("End Date", date(2025, 5, 1))
button = st.button("Predict")

if button:
    prediction = loaded_model.predict(Start_Date, End_Date)
    st.write("Seasonal Sales Forecust :", prediction)
