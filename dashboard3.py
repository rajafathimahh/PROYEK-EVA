import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Judul dashboard
st.title("Dashboard Penyewaan Sepeda")

# Sidebar untuk input user
st.sidebar.header('User Input Parameters')

@st.cache
def load_data():
    data = pd.read_csv('https://raw.githubusercontent.com/rajafathimahh/PROYEK-EVA/refs/heads/main/day.csv')  # Adjust the path as needed
    return data

data = load_data()

# Menunjukkan raw data jika di'select'
if st.sidebar.checkbox("Perlihatkan data mentah (raw)", False):
    st.subheader('Raw Dataset')
    st.write(data)

# Plot: Tren Rerata Penyewaan Sepeda Berdasarkan Musim selama 2011-2012
st.subheader('Tren Rerata Penyewaan Sepeda Berdasarkan Musim selama 2011-2012')
season_labels = {1: "Spring", 2: "Summer", 3: "Fall", 4: "Winter"}
day_df["season_label"] = day_df["season"].map(season_labels)
seasonal_trend = day_df.groupby("season_label")[["casual", "registered"]].mean()
fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(seasonal_trend.index, seasonal_trend["casual"], marker="o", label="Casual Users", color="blue")
ax.plot(seasonal_trend.index, seasonal_trend["registered"], marker="o", label="Registered Users", color="red")
ax.set_title("Tren Rerata Penyewaan Sepeda oleh Pengguna 'Casual' dan 'Registered' Berdasarkan Musim dalam 2 Tahun (2011-2012)")
ax.set_xlabel("Musim")
ax.set_ylabel("Rata-rata Jumlah Pengguna")
ax.legend(title="Tipe Pengguna")

# Menampilkan plot di Streamlit
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
