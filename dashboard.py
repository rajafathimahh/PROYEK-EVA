import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Judul dashboard
st.title("Dashboard Penyewaan Sepeda")

# Sidebar untuk input user
st.sidebar.header('Input Parameter Pengguna')

@st.cache
def load_data():
    data = pd.read_csv('https://raw.githubusercontent.com/rajafathimahh/PROYEK-EVA/refs/heads/main/day.csv')  # Adjust the path as needed
    return data

data = load_data()

day_df = pd.DataFrame(data)
st.subheader('Dashboard ini menampilkan hasil visualisasi data yang menjawab dua pertanyaan bisnis:')
st.markdown("""
- 1. Bagaimana rata-rata jumlah penyewaan sepeda oleh pengguna casual dan pengguna registered selama 4 musim dalam dua tahun (2011-2012)?
- 2. Apakah faktor cuaca seperti temp, hum, dan windspeed mempengaruhi jumlah total penyewaan sepeda pada hari kerja (working days) dibandingkan dengan akhir pekan (weekends) selama periode 2011-2012?
""")

# Menunjukkan raw data jika di'select'
if st.sidebar.checkbox("Perlihatkan data mentah (raw)", False):
    st.subheader('Raw Dataset')
    st.write(data)


# Plot: LINE CHART 'Tren Rerata Penyewaan Sepeda Berdasarkan Musim selama 2011-2012'
seasonal_trend = day_df.groupby("season")[["casual", "registered"]].mean()
st.title("Tren Penyewaan Sepeda Berdasarkan Musim")
st.write("Visualisasi tren rerata penyewaan sepeda oleh pengguna 'Casual' dan 'Registered' dalam 2 tahun (2011-2012).")
fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(seasonal_trend.index, seasonal_trend["casual"], marker="o", label="Casual Users", color="blue")
ax.plot(seasonal_trend.index, seasonal_trend["registered"], marker="o", label="Registered Users", color="red")
ax.set_title("Tren Rerata Penyewaan Sepeda oleh Pengguna 'Casual' dan 'Registered' Berdasarkan Musim")
ax.set_xlabel("Season (1=Spring, 2=Summer, 3=Fall, 4=Winter)")
ax.set_ylabel("Rata-rata Jumlah Pengguna")
ax.legend(title="Tipe Pengguna")
st.pyplot(fig) 
st.markdown("""
- Line chart di atas menunjukkan tren rata-rata penyewaan sepeda oleh pengguna 'casual' dan 'registered' selama 4 musim dalam 2 tahun, dari 2011-2012.
- Pengguna 'casual' direpresentasikan oleh garis biru dan pengguna 'registered direpresentasikan oleh garis merah.
- Terlihat bahwa rata-rata pengguna 'registered' selalu di atas pengguna 'casual' dan keduanya memiliki titik tertinggi di saat musim gugur atau 'fall', dan titik terendah saat musim semi atau 'spring.
""")


# Plot: BAR CHART 'Perbandingan Rerata Penggunaan Sepeda: Casual vs Registered Users di Setiap Musim'
x = np.arange(len(seasonal_trend))
width = 0.35
fig, ax = plt.subplots(figsize=(8, 5))
ax.bar(x - width/2, seasonal_trend["casual"], width, label="Casual Users", color="blue")
ax.bar(x + width/2, seasonal_trend["registered"], width, label="Registered Users", color="red")
ax.set_title("Perbandingan Rerata Penggunaan Sepeda: Casual vs Registered Users di Setiap Musim")
ax.set_xlabel("Season (1=Spring, 2=Summer, 3=Fall, 4=Winter)")
ax.set_xticks(x)
ax.set_xticklabels(seasonal_trend.index)
ax.set_ylabel("Rata-rata Jumlah Pengguna")
ax.legend(title="Tipe Pengguna")
st.pyplot(fig)
st.markdown("""
- Bar chart di atas menunjukkan perbandingan rata-rata penyewaan sepeda oleh pengguna 'casual' dan 'registered' selama 4 musim dalam 2 tahun, dari 2011-2012. 
- Pengguna 'casual' direpresentasikan oleh batang biru dan pengguna 'registered direpresentasikan oleh batang merah. 
- Terlihat bahwa rata-rata pengguna 'registered' selalu di atas pengguna 'casual' dan keduanya memiliki nilai tertinggi di saat musim gugur atau 'fall', dan nilai terendah saat musim semi atau 'spring.
""")

# Filter interaktif kondisi cuaca 'weather'
selected_weather = st.sidebar.selectbox('Pilih Kondisi Cuaca', data['weathersit'].unique())

st.subheader(f'Analisis Kondisi Cuaca: {selected_weather}')
filtered_data = data[data['weathersit'] == selected_weather]
st.write(filtered_data.describe())

# SCATTER PLOT
# Plot Suhu vs Total Pengguna
st.subheader('Pengaruh Suhu terhadap Total Pengguna')
fig, ax = plt.subplots()
sns.scatterplot(data=data, x='temp', y='cnt', ax=ax)
sns.regplot(x='temp', y='cnt', data=day_df, line_kws={'color': 'red'}, ax=ax)
ax.set_title('Suhu vs Jumlah Penyewa Sepeda')
st.pyplot(fig)

# Plot Kelembapan vs Total Pengguna
st.subheader('Pengaruh Kelembapan terhadap Total Pengguna')
fig, ax = plt.subplots()
sns.scatterplot(data=data, x='hum', y='cnt', ax=ax)
sns.regplot(x='hum', y='cnt', data=day_df, line_kws={'color': 'red'}, ax=ax)
ax.set_title('Kelembapan vs Jumlah Penyewa Sepeda')
st.pyplot(fig)

# Plot Kecepatan Angin vs Total Pengguna
st.subheader('Pengaruh Kecepatan Angin terhadap Total Pengguna')
fig, ax = plt.subplots()
sns.scatterplot(data=data, x='windspeed', y='cnt', ax=ax)
sns.regplot(x='windspeed', y='cnt', data=day_df, line_kws={'color': 'red'}, ax=ax)
ax.set_title('Kecepatan Angin vs Jumlah Penyewa Sepeda')
st.pyplot(fig)
st.markdown("""
- Scatter plot pada masing-masing faktor cuaca terhadap jumlah penyewa/pengguna memperlihatkan bahwa titik-titik data tersebar luas, dan dengan hasil plot regresi linear, titik-titik data baik pada suhu, kelembapan, maupun kecepatan angin terlihat tidak mendekati garis regresi. 
""")

# Conclusion
st.subheader('Kesimpulan')
st.markdown("""
- Conclution pertanyaan 1: 

Rata-rata jumlah penyewaan sepeda oleh pengguna 'casual' selalu lebih rendah daripada pengguna 'registered' selama 4 musim pada 2011-2012, dengan musim yang memiliki rata-rata pengguna tertinggi baik 'casual' maupun 'registered' adalah musim gugur, dan musim dengan rata-rata terendah adalah musim semi. Terlihat bahwa pengguna 'registered' lebih sering menyewa sepeda dibandingkan pengguna 'casual'. 

Lebih jelasnya, pada musim semi (spring), rata-rata pengguna 'casual' hanya sebesar 335, sedangkan pengguna 'registered' sebesar 2269 pengguna. Pada musim panas (summer), rata-rata pengguna 'casual' sebesar 1106, sedangkan pengguna 'registered' sebesar 3886 pengguna. Pada musim gugur (fall), rata-rata pengguna 'casual' sebesar 1203, sedangkan pengguna 'registered' sebesar 4442 pengguna. Terakhir, pada musim dingin (winter), rata-rata pengguna 'casual' sebesar 729, sedangkan pengguna 'registered' sebesar 3999 pengguna.

- Conclution pertanyaan 2: 

Faktor cuaca seperti suhu, kelembapan, dan kecepatan angin ('tempt', 'hum', dan 'windspeed') terhadap jumlah total penyewaan sepeda baik pada hari kerja dan akhir pekan selama 2011-2012 memiliki pengaruh yang sangat kecil karena nilai rata-rata setiap faktor cuaca tersebut tidak memiliki perbedaan yang cukup signifikan pada saat akhir pekan maupun hari kerja. 

Selain itu, jumlah pengguna pada akhir pekan sebanyak 4330, jauh lebih tinggi dibandingkan dengan hari kerja yang sebanyak 1878. Meskipun faktor cuaca tidak menunjukkan perbedaan yang signifikan, hasil ini menunjukkan bahwa ada faktor lain yang mendorong lebih banyak orang untuk menggunakan sepeda pada akhir pekan, seperti waktu luang pada hari libur.

- Conclution RFM Analysis:

Selain jawaban 2 pertanyaan bisnis, juga dilakukan analisis lanjutan dengan teknik RFM Analysis. Diperoleh hasil bahwa pengguna 'registered' cenderung berkontribusi lebih banyak dibandingkan pengguna 'casual' dalam hal frekuensi dan jumlah penyewaan sepeda dengan total sewa 2672662 banding 620017, serta jumlah hari terakhir sejak penyewaan sepeda untuk keduanya adalah 366 hari. 
""")
