import streamlit as st
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

from babel.numbers import format_currency
sns.set(style="dark")



all_df = pd.read_csv("main_data.csv")

all_df['dteday'] = pd.to_datetime(all_df['dteday'])
# Mengonversi nilai untuk kolom 'season' menjadi musim: 1:Winter, 2:Spring, 3:Summer, 4:Fall
all_df['season'].replace({1: 'Winter', 2: 'Spring', 3: 'Summer', 4: 'Fall'}, inplace=True)
# Mengonversi nilai untuk kolom 'yr' menjadi tahun: 0:2011, 1:2012
all_df['yr'].replace({0: 2011, 1: 2012}, inplace=True)
# Mengonversi nilai untuk kolom 'mnth' menjadi bulan: 1:Jan, 2:Feb, 3:Mar, 4:Apr, 5:May, 6:Jun, 7:Jul, 8:Aug, 9:Sep, 10:Oct, 11:Nov, 12:Dec
all_df['mnth'].replace({1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun', 7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'}, inplace=True)
# Mengonversi nilai untuk kolom 'weathersit' menjadi kondisi cuaca: 1:Clear, 2:Misty, 3:Light_RainSnow, 4:Heavy_RainSnow
all_df['weathersit'].replace({1: 'Clear', 2: 'Misty', 3: 'Light_RainSnow', 4: 'Heavy_RainSnow'}, inplace=True)
# Mengonversi nilai untuk kolom 'weekday' menjadi hari: 0:Sun, 1:Mon, 2:Tue, 3:Wed, 4:Thu, 5:Fri, 6:Sat
all_df['weekday'].replace({0: 'Sunday', 1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday'}, inplace=True)
# Mengonversi nilai untuk kolom 'workingday' menjadi status kerja: 0:No, 1:Yes
all_df['workingday'].replace({0: 'No', 1: 'Yes'}, inplace=True)


min_date = all_df["dteday"].min()
max_date = all_df["dteday"].max()

with st.sidebar:

    st.image("https://images.unsplash.com/photo-1455641374154-422f32e234cd?q=80&w=1932&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D")
    # Mengambil start_date & end_date dari date_input
    start_date, end_date = st.date_input(
        label='Rentang Waktu', min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )


main_df = all_df[(all_df["dteday"] >= str(start_date)) &
                (all_df["dteday"] <= str(end_date))]


# Judul
st.title("Data Rental Sepeda Harian")

st.subheader("Penyewaan Sepeda Terbanyak berdasarkan Musim")
fig, ax = plt.subplots(figsize=(20, 10))

colors = ["#D3D3D3", "#D3D3D3","#90CAF9", "#D3D3D3"]

sns.barplot(
    y="cnt",
    x="season",
    data=main_df,
    palette=colors,
    ax=ax
)
ax.set_title("Jumlah Sewa Berdasarkan Musim", loc="center", fontsize=35, pad=30)
ax.set_ylabel("Jumlah Sewa Sepeda Harian", fontsize=20, labelpad=20)
ax.set_xlabel("Musim", fontsize= 20, labelpad=20)
ax.tick_params(axis='x', labelsize=30)
ax.tick_params(axis='y', labelsize=30)
st.pyplot(fig)

st.subheader("Grafik Penyewaan Sepeda dalam Beberapa Bulan Terakhir")
fig, ax = plt.subplots(figsize=(20, 10))

sns.lineplot(
    y="cnt",
    x="mnth",
    data=main_df,
    ax=ax
)
ax.set_title("Jumlah Sewa Berdasarkan Bulan", loc="center", fontsize=35, pad=30)
ax.set_ylabel("Jumlah Sewa Sepeda Harian", fontsize=20, labelpad=20)
ax.set_xlabel("Bulan", fontsize= 20, labelpad=20)
ax.tick_params(axis='x', labelsize=30)
ax.tick_params(axis='y', labelsize=30)
st.pyplot(fig)
