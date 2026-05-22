import streamlit as st
import pandas as pd

st.set_page_config(page_title='SWAST - Handover Delays',  layout='wide', page_icon=':compass:')
t1, t2 = st.columns((0.15,1)) 

t1.image('images/logo_kmu.png', width = 250)
t2.title("Dashboard Monitoring Kepatuhan Presensi")
t2.markdown(" **tel:** 01392 451192 **|  Presnewebsite:** https://www.swast.nhs.uk **| email:** rahmat@rspkt.id")
 
st.write("""
## Data Kehadiran karyawan
""")
 
df = pd.read_csv("ceklok.csv")
# =========================
# Filter berdasarkan Tahun, Bulan, Kategori, Nama 
# =========================
st.subheader("Filter Data Berdasarkan Tahun, Bulan, Kategori, dan Nama")

g1, g2= st.columns((1,1))

with g1:
    nama = st.selectbox(
        "Pilih Nama",
        df['Nama'].unique()
    )

with g2:
    kategori = st.selectbox(
        "Pilih Kategori",
        df['Kategori'].unique()
    )


filtered_data = df[
    
    (df['Nama'] == nama) &
    (df['Kategori'] == kategori)
]

st.write(f"Data Kehadiran untuk Nama: {nama}, Kategori: {kategori}")

st.dataframe(filtered_data)


## Grafik Kehadiran Karyawan
g1, g2 = st.columns((1,1))
with g1:
    st.subheader("Grafik Kehadiran per Karyawan")
    
    fgdf = pd.read_csv('ceklok.csv')

    kehadiran_count = filtered_data['Nama'].value_counts()

    # Mengubah ke DataFrame agar line chart lebih rapi
    kehadiran_count = kehadiran_count.reset_index()
    kehadiran_count.columns = ['Nama', 'Jumlah Kehadiran']

    st.line_chart(
        kehadiran_count.set_index('Nama')
    )

with g2:
    st.subheader("Grafik Kehadiran per Bulan")

    bulanan = filtered_data.groupby('Bulan')['Nama'].count()

    # Mengubah ke DataFrame
    bulanan = bulanan.reset_index()
    bulanan.columns = ['Bulan', 'Jumlah Kehadiran']

    st.line_chart(
        bulanan.set_index('Bulan')
    )

st.write("""
## Data Klaim BPJS Kesehatan
""")

df = pd.read_csv("Klaim.csv")
# =========================
# Filter berdasarkan Tahun, Bulan dan Jenisklaim
# =========================
st.subheader("Filter Data Berdasarkan Tahun, Bulan dan Jenisklaim")

g1, g2, g3 = st.columns((1,1,1))

with g1:
    tahun = st.selectbox(
        "Pilih Tahun",
        df['Tahun'].unique()
    )

with g2:
    bulan = st.selectbox(
        "Pilih Bulan",
        df['Bulan'].unique()
    )

with g3:
    Jenisklaim = st.selectbox(
        "Pilih Jenisklaim",
        df['Jenisklaim'].unique()
    )

filtered_data = df[
    (df['Tahun'] == tahun) &
    (df['Bulan'] == bulan) &
    (df['Jenisklaim'] == Jenisklaim)
]

st.write(f"Data Klaim untuk Tahun: {tahun}, Bulan: {bulan}, Jenisklaim: {Jenisklaim}")

st.dataframe(filtered_data)

## Grafik jumlah data Klaim
g1, g2, g3 = st.columns((1,1,1))

with g1:
    st.subheader("Grafik Jumlah Klaim")
    fgdf = pd.read_csv('Klaim.csv')

    klaim_count = filtered_data['Jenisklaim'].value_counts()
    st.bar_chart(klaim_count)

with g2:
    st.subheader("Grafik Total SEP per Jenisklaim")
    st.bar_chart(filtered_data.groupby('Jenisklaim')['SEP'].sum())
    
with g3:
    st.subheader("Grafik Total Rupiah per Jenisklaim")
    st.bar_chart(filtered_data.groupby('Jenisklaim')['Rupiah'].sum())


st.write("""
## Data Lembur Karyawan
""")

df = pd.read_csv("Lembur.csv")

st.write(df)


## Grafik Lembur Karyawan
g1, g2 = st.columns((1,1))

with g1:
    st.subheader("Grafik Jumlah Lembur")
    fgdf = pd.read_csv('lembur.csv')

    lembur_count = fgdf['Rupiah'].value_counts()
    st.bar_chart(lembur_count)

with g2:
    st.subheader("Grafik Total Lembur per Bulan")
    st.bar_chart(fgdf.groupby('Bulan')['Rupiah'].sum())


