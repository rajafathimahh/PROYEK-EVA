import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

sns.set(style='dark')

@st.cache
def load_data():
    return pd.read_csv('/Users/smapd/Documents/dashboard/day.csv')

day_df = load_data()

st.title("Dashboard Penyewaan Sepeda")

# Analisis Berdasarkan Musim
st.header("Analisis Penggunaan Sepeda Berdasarkan Musim")
season_casual_registered = day_df.groupby(by="season").agg({
    "casual": ["mean", "max", "min"],
    "registered": ["mean", "max", "min"]
})

st.write(season_casual_registered)

# Visualisasi dengan Line Chart
season_labels = {1: "Spring", 2: "Summer", 3: "Fall", 4: "Winter"}
day_df["season_label"] = day_df["season"].map(season_labels)

# Mengelompokkan data berdasarkan musim dan menghitung rata-rata jumlah casual dan registered
seasonal_trend = day_df.groupby("season_label")[["casual", "registered"]].mean()

plt.figure(figsize=(8, 5))
plt.plot(seasonal_trend.index, seasonal_trend["casual"], marker="o", label="Casual Users", color="blue")
plt.plot(seasonal_trend.index, seasonal_trend["registered"], marker="o", label="Registered Users", color="red")
plt.title("Tren Rerata Penyewaan Sepeda oleh Pengguna 'Casual' dan 'Registered' Berdasarkan Musim dalam 2 Tahun (2011-2012)")
plt.xlabel("Musim")
plt.ylabel("Rata-rata Jumlah Pengguna")
plt.legend(title="Tipe Pengguna")
st.pyplot()  # Menampilkan plot di Streamlit

# Analisis Berdasarkan Faktor Cuaca di Working days
workday_weather_users = day_df.groupby(by="workingday").agg({
    "temp": ["mean", "max", "min", "std"],
    "hum": ["mean", "max", "min", "std"],
    "windspeed": ["mean", "max", "min", "std"],
    "cnt": ["mean", "max", "min", "std"]
})

# Menampilkan hasil
st.write(workday_weather_users)  # Menampilkan DataFrame di Streamlit

# Visualisasi Scatter Plot dan Regression
plt.figure(figsize=(15, 4))

# Scatter plot 'temp' vs 'cnt'
plt.subplot(1, 3, 1)
plt.scatter(day_df['temp'], day_df['cnt'], c=day_df['workingday'], cmap='coolwarm', alpha=0.6)
sns.regplot(x='temp', y='cnt', data=day_df, line_kws={'color': 'red'})
plt.title('Suhu vs Jumlah Penyewa Sepeda')
plt.xlabel('Suhu')
plt.ylabel('Jumlah Penyewa')
plt.colorbar(label='0: Akhir Pekan, 1: Hari Kerja')  
st.pyplot()  # Menampilkan plot di Streamlit

# Scatter plot 'hum' vs 'cnt'
plt.subplot(1, 3, 2)
plt.scatter(day_df['hum'], day_df['cnt'], c=day_df['workingday'], cmap='coolwarm', alpha=0.6)
sns.regplot(x='hum', y='cnt', data=day_df, line_kws={'color': 'red'})
plt.title('Kelembaban vs Jumlah Penyewa Sepeda')
plt.xlabel('Kelembaban')
plt.ylabel('Jumlah Penyewa')
plt.colorbar(label='0: Akhir Pekan, 1: Hari Kerja')  
st.pyplot()  # Menampilkan plot di Streamlit

# Scatter plot 'windspeed' vs 'cnt'
plt.subplot(1, 3, 3)
plt.scatter(day_df['windspeed'], day_df['cnt'], c=day_df['workingday'], cmap='coolwarm', alpha=0.6)
sns.regplot(x='windspeed', y='cnt', data=day_df, line_kws={'color': 'red'})
plt.title('Kecepatan Angin vs Jumlah Penyewa Sepeda')
plt.xlabel('Kecepatan Angin')
plt.ylabel('Jumlah Penyewa')
plt.colorbar(label='0: Akhir Pekan, 1: Hari Kerja') 

plt.suptitle("Pengaruh Faktor Cuaca (Suhu, Kelembapan, Kecepatan Angin) Terhadap Jumlah Total Penyewa Sepeda pada Hari Kerja dan Akhir Pekan selama 2011-2012")
plt.tight_layout()
st.pyplot()  # Menampilkan plot di Streamlit