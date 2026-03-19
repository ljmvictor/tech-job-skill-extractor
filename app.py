import streamlit as st
import pandas as pd

# 1. Set the title of your web app
st.title("Tech Job Market Skill Extractor 📊")

# 2. Add a welcome message
st.write("Welcome to your first AI data dashboard! Here is a sneak peek at the data we pulled from Hugging Face:")

# 3. Read the CSV file we created earlier
df = pd.read_csv("sample_jobs.csv")

# 4. Display the data as an interactive table!
st.dataframe(df)

# 5. Add a simple bar chart just to show off what Streamlit can do
st.subheader("Top Job Titles in our Sample")
job_counts = df['job_title'].value_counts().head(10)
st.bar_chart(job_counts)