from datetime import timedelta
from pathlib import Path
from time import sleep

import numpy as np
import pandas as pd
import plotly_express as px
import streamlit as st

# set the app's title
st.title("Text Elements")
 
# header
st.header("Header in Streamlit")
 
# subheader
st.subheader("Subheader in Streamlit")
 
# markdown
# display text in bold formatting
st.markdown("**AskPython** is an awesome website!")
# display text in italic formatting
st.markdown("Visit _askpython.com_ to learn from various Python tutorials.")
 
# code block
code = '''
def add(a, b):
    print("a+b = ", a+b)
'''
st.code(code, language='python')
 
# latex
st.latex('''
(a+b)^2 = a^2 + b^2 + 2*a*b
''')

#button
if st.button('Click here', help="Click to see the text change"):
    st.write('Hi there!')
else:
    st.write('Goodbye')
 
# check box
checked = st.checkbox('Click here')
if checked:
    st.write('Good job!')

# radio button
lang = st.radio(
    "What's your favorite programming language?",
    ('C++', 'Python'))
 
if lang == 'C++':
    st.write('You selected C++.')
else:
    st.write('You selected Python.')

# slider
score = st.slider('Please specify your test score', 
                   min_value=0, max_value=100, value=10)
st.write("My test score is ", score)


DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = load_data(10000)
# Notify the reader that the data was successfully loaded.
data_load_state.text("Done! (using st.cache)")

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

st.subheader('Number of pickups by hour')

hist_values = np.histogram(
    data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]

st.bar_chart(hist_values)

st.subheader('Map of all pickups')
st.map(data)

hour_to_filter = st.slider('hour', 0, 23, 17)  # min: 0h, max: 23h, default: 17h

filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
st.subheader(f'Map of all pickups at {hour_to_filter}:00')
st.map(filtered_data)