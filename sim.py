import pandas as pd
import streamlit as st
import os
import random

# Load data from local XLSX file
df = pd.read_excel('data_clean.xlsx')
if os.path.isfile('data_clean.xlsx'):
    with open('data_clean.xlsx', 'rb') as f:
        data = f.read()
        st.download_button(label='Download cleaned data', data=data, file_name='data_clean.xlsx', mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

# Select text column where sarcasm is NaN
dfkosong = len(df.loc[df['sarcasm'].isna(), ['text']])
st.write(str(len(df) - dfkosong) + " / " + str(len(df)))
random_index = 0
# st.write(df.iloc[random_index]['sarcasm'].isnull())
while(not(pd.isna((df.iloc[random_index]['sarcasm'])))):
    random_index = random_index + 1
# Define label buttons
labels = ['Non-sarcasm', 'Sarcasm', 'Noise']

st.header(df.iloc[random_index]['text'])

col1, col2, col3 = st.columns([1,1,1])

with col1:
    if(st.button("Sarcasm")):
        df.loc[random_index, 'sarcasm'] = 1
        df.to_excel("data_clean.xlsx", index=False)
        st.experimental_rerun()
with col2:
    if(st.button("Non-Sarcasm")):
        df.loc[random_index, 'sarcasm'] = 0
        df.to_excel("data_clean.xlsx", index=False)
        st.experimental_rerun()
with col3:
    if(st.button("Non-Clean")):
        df.loc[random_index, 'sarcasm'] = 2
        df.to_excel("data_clean.xlsx", index=False)
        st.experimental_rerun()

