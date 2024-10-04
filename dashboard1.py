import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Title of the dashboard
st.title('Data Analysis Dashboard')

# Sidebar for user input
st.sidebar.header('User Input Parameters')

# Load the dataset
@st.cache
def load_data():
    data = pd.read_csv('https://raw.githubusercontent.com/rajafathimahh/PROYEK-EVA/refs/heads/main/day.csv')  # Adjust the path as needed
    return data

data = load_data()

# Show raw data if selected
if st.sidebar.checkbox("Show raw data", False):
    st.subheader('Raw Dataset')
    st.write(data)

# Plot: Distribution of users by season
st.subheader('Distribution of Users by Season')
season_counts = data['season'].value_counts()
fig, ax = plt.subplots()
season_counts.plot(kind='bar', ax=ax)
ax.set_title('Distribution of Users by Season')
ax.set_xlabel('Season')
ax.set_ylabel('Count')
st.pyplot(fig)

# Interactive filter by weather condition
selected_weather = st.sidebar.selectbox('Select Weather Condition', data['weathersit'].unique())

st.subheader(f'Analysis for Weather Condition: {selected_weather}')
filtered_data = data[data['weathersit'] == selected_weather]
st.write(filtered_data.describe())

# Additional plot: Temperature vs. User Count
st.subheader('Temperature vs. Count of Users')
fig, ax = plt.subplots()
sns.scatterplot(data=data, x='temp', y='cnt', ax=ax)
ax.set_title('Temperature vs. Count of Users')
st.pyplot(fig)

# Conclusion
st.subheader('Conclusions')
st.markdown("""
- The distribution of users changes depending on the season and weather.
- Higher temperatures generally lead to more bicycle rentals.
""")
