import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Assume 'day_df' is already loaded, modify the path or loading method accordingly
# day_df = pd.read_csv('path_to_your_day.csv')

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

# Membuat plot tren pengguna casual dan registered
fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(seasonal_trend.index, seasonal_trend["casual"], marker="o", label="Casual Users", color="blue")
ax.plot(seasonal_trend.index, seasonal_trend["registered"], marker="o", label="Registered Users", color="red")
ax.set_title("Tren Rerata Penyewaan Sepeda oleh Pengguna 'Casual' dan 'Registered' Berdasarkan Musim dalam 2 Tahun (2011-2012)")
ax.set_xlabel("Musim")
ax.set_ylabel("Rata-rata Jumlah Pengguna")
ax.legend(title="Tipe Pengguna")
st.pyplot(fig)  # Menampilkan plot di Streamlit

# Analisis Berdasarkan Faktor Cuaca di Working days
st.header("Analisis Berdasarkan Faktor Cuaca di Hari Kerja dan Akhir Pekan")
workday_weather_users = day_df.groupby(by="workingday").agg({
    "temp": ["mean", "max", "min", "std"],
    "hum": ["mean", "max", "min", "std"],
    "windspeed": ["mean", "max", "min", "std"],
    "cnt": ["mean", "max", "min", "std"]
})

# Menampilkan hasil
st.write(workday_weather_users)

# Visualisasi Scatter Plot dan Regression
fig, axes = plt.subplots(1, 3, figsize=(15, 4))

# Scatter plot 'temp' vs 'cnt'
axes[0].scatter(day_df['temp'], day_df['cnt'], c=day_df['workingday'], cmap='coolwarm', alpha=0.6)
sns.regplot(x='temp', y='cnt', data=day_df, ax=axes[0], line_kws={'color': 'red'})
axes[0].set_title('Suhu vs Jumlah Penyewa Sepeda')
axes[0].set_xlabel('Suhu')
axes[0].set_ylabel('Jumlah Penyewa')
axes[0].colorbar = plt.colorbar(ax=axes[0], label='0: Akhir Pekan, 1: Hari Kerja')

# Scatter plot 'hum' vs 'cnt'
axes[1].scatter(day_df['hum'], day_df['cnt'], c=day_df['workingday'], cmap='coolwarm', alpha=0.6)
sns.regplot(x='hum', y='cnt', data=day_df, ax=axes[1], line_kws={'color': 'red'})
axes[1].set_title('Kelembaban vs Jumlah Penyewa Sepeda')
axes[1].set_xlabel('Kelembaban')
axes[1].set_ylabel('Jumlah Penyewa')
axes[1].colorbar = plt.colorbar(ax=axes[1], label='0: Akhir Pekan, 1: Hari Kerja')

# Scatter plot 'windspeed' vs 'cnt'
axes[2].scatter(day_df['windspeed'], day_df['cnt'], c=day_df['workingday'], cmap='coolwarm', alpha=0.6)
sns.regplot(x='windspeed', y='cnt', data=day_df, ax=axes[2], line_kws={'color': 'red'})
axes[2].set_title('Kecepatan Angin vs Jumlah Penyewa Sepeda')
axes[2].set_xlabel('Kecepatan Angin')
axes[2].set_ylabel('Jumlah Penyewa')
axes[2].colorbar = plt.colorbar(ax=axes[2], label='0: Akhir Pekan, 1: Hari Kerja')

fig.suptitle("Pengaruh Faktor Cuaca (Suhu, Kelembapan, Kecepatan Angin) Terhadap Jumlah Total Penyewa Sepeda pada Hari Kerja dan Akhir Pekan selama 2011-2012")
fig.tight_layout()
st.pyplot(fig)  # Menampilkan plot di Streamlit

# streamlit run dashboard.py