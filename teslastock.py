import streamlit as st
import pandas as pd
from datetime import datetime

# Load the dataset
df = pd.read_csv(r"complete.csv")

# Convert the 'date' column to datetime
df['date'] = pd.to_datetime(df['date'])

# Streamlit App
st.title('Headline Sentiment Analyzer')

# Get the minimum and maximum dates from the dataset
min_date = df['date'].min().date()
max_date = df['date'].max().date()

# Set the default value to the minimum date
selected_date = st.sidebar.date_input('Select Date', min_value=min_date, max_value=max_date, value=min_date)

# Get the unique times for the selected date
available_times = df[df['date'].dt.date == selected_date]['time'].unique()

# Set the default value to the first available time
default_time = available_times[0] if available_times.any() else None

# Allow selection of time
selected_time = st.sidebar.selectbox('Select Time', options=available_times, index=0)

# Filter the dataset based on selected date and time
filtered_df = df[(df['date'].dt.date == selected_date) & (df['time'] == selected_time)]

# Display the first headline if available
if not filtered_df.empty:
    for index, row in filtered_df.iterrows():
        st.write('Headline:', row['headline'])
        st.write('Sentiment:', row['sentiment'])
else:
    st.write('No headlines available for the selected date and time.')







