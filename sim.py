import pandas as pd
import streamlit as st
import os
import random

# Load data from local XLSX file
df = pd.read_excel('data_clean.xlsx')

# Select text column where sarcasm is NaN
# df = df.loc[df['sarcasm'].isna(), ['text']]
random_index = random.randint(0, len(df) - 1)
# st.write(df.iloc[random_index]['sarcasm'].isnull())
while(not(pd.isna((df.iloc[random_index]['sarcasm'])))):
    random_index = random.randint(0, len(df) - 1)
# Define label buttons
labels = ['Non-sarcasm', 'Sarcasm', 'Noise']

st.title(df.iloc[random_index]['text'])

if(st.button("Sarcasm")):
    df.loc[random_index, 'sarcasm'] = 1
    df.to_excel("data_clean.xlsx", index=False)
if(st.button("Non-Sarcasm")):
    df.loc[random_index, 'sarcasm'] = 0
    df.to_excel("data_clean.xlsx", index=False)
if(st.button("Non-Clean")):
    df.loc[random_index, 'sarcasm'] = 2
    df.to_excel("data_clean.xlsx", index=False)

if os.path.isfile('data_clean.xlsx'):
    with open('data_clean.xlsx', 'rb') as f:
        data = f.read()
        st.download_button(label='Download cleaned data', data=data, file_name='data_clean.xlsx', mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
