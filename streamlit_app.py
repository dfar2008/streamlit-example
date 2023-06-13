import streamlit as st
import pandas as pd
import numpy as np

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])
df = pd.read_csv('https://testnewoky.crm123.cn/8d862b2a-9b63-4b9a-b375-10d4138f130a.csv')

st.line_chart(df)
