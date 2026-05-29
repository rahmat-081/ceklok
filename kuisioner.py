'''
Aplikasi Streamlit untuk menampilkan hasil survey. 
Survey atas Pengaruh Penerapan Reward dan Punishment
Terhadap kepatuhan Presensi Digital di Unit Casemix RSPKT Bontang.

Pertanyaan atas survey: pertanyaan_kuisioner.csv
Hasil survey: kuisioner.csv

Hasil pengolahan yang diharapkan:
1. Tampilan tabel dari hasil survey 

'''
import streamlit as st
import pandas as pd
from scipy.stats import t, pearsonr, kstest, f as f_dist
import numpy as np
import matplotlib.pyplot as plt

from r_tabel import df as r_tabel_df

st.set_page_config(layout="wide")

st.title("Hasil Survey Pengaruh Penerapan Reward dan Punishment Terhadap Kepatuhan Presensi Digital di Unit Casemix RSPKT Bontang")

# Membaca data hasil survey dan pertanyaan survey
data_kuisioner = None
data_pertanyaan = None

# Menampilkan informasi tentang aplikasi
st.write("Aplikasi ini menampilkan hasil survey yang dilakukan untuk mengetahui pengaruh penerapan reward dan punishment terhadap kepatuhan presensi digital di Unit Casemix RSPKT Bontang. Data hasil survey dan pertanyaan survey ditampilkan dalam bentuk tabel di bawah ini.")

# menerima upload data berupa csv untuk hasil survey dan pertanyaan survey
g1, g2 = st.columns(2)
with g1:
    uploaded_file_kuisioner = st.file_uploader("Unggah file hasil survey (CSV)", type="csv")
    if uploaded_file_kuisioner is not None:
        data_kuisioner = pd.read_csv(uploaded_file_kuisioner)
        st.write("Data hasil survey berhasil diunggah.")
with g2:
    uploaded_file_pertanyaan = st.file_uploader("Unggah file pertanyaan survey (CSV)", type="csv")
    if uploaded_file_pertanyaan is not None:
        data_pertanyaan = pd.read_csv(uploaded_file_pertanyaan)
        st.write("Data pertanyaan survey berhasil diunggah.")
    
# if data_kuisioner is not None and data_pertanyaan is not None:
    
# Menampilkan distribusi frekuensi dan presentase menurut usia
st.subheader("4.2.1 Tabel Distribusi Frekuensi Karakteristik Karyawan")
g1, g2 = st.columns((1,0.6))
with g1:
    st.write("a. Distribusi Frekuensi dan Presentase Menurut Usia:")
    usia_counts = data_kuisioner['usia'].value_counts().sort_index()
    usia_percentages = data_kuisioner['usia'].value_counts(normalize=True).sort_index() * 100
    usia_df = pd.DataFrame({'Usia': usia_counts.index, 'N': usia_counts.values, 'Persen(%)': usia_percentages.values})
    usia_df['Persen(%)'] = usia_df['Persen(%)'].apply(lambda x: f"{x:.1f}%")
    st.dataframe(usia_df)

with g2:
    fig, ax = plt.subplots()
    ax.pie(usia_counts.values, labels=usia_counts.index, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')
    st.pyplot(fig)

# Menampilkan distribusi frekuensi dan presentase menurut gender
g1, g2 = st.columns((1,0.6))
with g1:
    st.write("b. Distribusi Frekuensi dan Presentase Menurut Gender:")
    gender_counts = data_kuisioner['gender'].value_counts()
    gender_percentages = data_kuisioner['gender'].value_counts(normalize=True) * 100
    gender_df = pd.DataFrame({'Gender': gender_counts.index, 'Frekuensi': gender_counts.values, 'Persen(%)': gender_percentages.values})
    gender_df['Persen(%)'] = gender_df['Persen(%)'].apply(lambda x: f"{x:.1f}%")
    st.dataframe(gender_df)

with g2:
    fig, ax = plt.subplots()
    ax.pie(gender_counts.values, labels=gender_counts.index, autopct='%1.1f%%', startangle=80)
    ax.axis('equal')
    st.pyplot(fig)

# Menampilkan distribusi frekuensi dan presentase menurut pendidikan
g1, g2 = st.columns((1,0.6))
with g1:
    st.write("c. Distribusi Frekuensi dan Presentase Menurut Pendidikan:")
    pendidikan_counts = data_kuisioner['pendidikan'].value_counts()
    pendidikan_percentages = data_kuisioner['pendidikan'].value_counts(normalize=True) * 100
    pendidikan_df = pd.DataFrame({'Pendidikan': pendidikan_counts.index, 'Frekuensi': pendidikan_counts.values, 'Persen(%)': pendidikan_percentages.values})
    pendidikan_df['Persen(%)'] = pendidikan_df['Persen(%)'].apply(lambda x: f"{x:.1f}%")
    st.dataframe(pendidikan_df)

with g2:
    fig, ax = plt.subplots()
    ax.pie(pendidikan_counts.values, labels=pendidikan_counts.index, autopct='%1.1f%%', startangle=80)
    ax.axis('equal')
    st.pyplot(fig)


# Menampilkan distribusi frekuensi dan presentase menurut jabatan
g1, g2 = st.columns((1,0.6))
with g1:
    st.write("d. Distribusi Frekuensi dan Presentase Menurut Jabatan:")
    jabatan_counts = data_kuisioner['jabatan'].value_counts()
    jabatan_percentages = data_kuisioner['jabatan'].value_counts(normalize=True) * 100
    jabatan_df = pd.DataFrame({'Jabatan': jabatan_counts.index, 'Frekuensi': jabatan_counts.values, 'Persen(%)': jabatan_percentages.values})
    jabatan_df['Persen(%)'] = jabatan_df['Persen(%)'].apply(lambda x: f"{x:.1f}%")
    st.dataframe(jabatan_df)

with g2:
    fig, ax = plt.subplots()
    ax.pie(jabatan_counts.values, labels=jabatan_counts.index, autopct='%1.1f%%', startangle=80)
    ax.axis('equal')
    st.pyplot(fig)


# Menampilkan distribusi frekuensi dan presentase menurut pekerjaan
g1, g2 = st.columns((1,0.6))
with g1:
    st.write("e. Distribusi Frekuensi dan Presentase Menurut Pekerjaan:")
    pekerjaan_counts = data_kuisioner['pekerjaan'].value_counts()
    pekerjaan_percentages = data_kuisioner['pekerjaan'].value_counts(normalize=True) * 100
    pekerjaan_df = pd.DataFrame({'Pekerjaan': pekerjaan_counts.index, 'Frekuensi': pekerjaan_counts.values, 'Persen(%)': pekerjaan_percentages.values})
    pekerjaan_df['Persen(%)'] = pekerjaan_df['Persen(%)'].apply(lambda x: f"{x:.1f}%")
    st.dataframe(pekerjaan_df)

with g2:
    fig, ax = plt.subplots()
    ax.pie(pekerjaan_counts.values, labels=pekerjaan_counts.index, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')
    st.pyplot(fig)


# Menampilkan distribusi frekuensi dan presentase menurut masa kerja
g1, g2 = st.columns((1,0.6))
with g1:
    st.write("f. Distribusi Frekuensi dan Presentase Menurut Masa Kerja:")
    masa_kerja_counts = data_kuisioner['masa_kerja'].value_counts()
    masa_kerja_percentages = data_kuisioner['masa_kerja'].value_counts(normalize=True) * 100
    masa_kerja_df = pd.DataFrame({'Masa Kerja': masa_kerja_counts.index, 'Frekuensi': masa_kerja_counts.values, 'Persen(%)': masa_kerja_percentages.values})
    masa_kerja_df['Persen(%)'] = masa_kerja_df['Persen(%)'].apply(lambda x: f"{x:.1f}%")
    st.dataframe(masa_kerja_df)
    
with g2:
    fig, ax = plt.subplots()
    ax.pie(masa_kerja_counts.values, labels=masa_kerja_counts.index, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')
    st.pyplot(fig)


# Menampilkan uji validitas dan reliabilitas untuk setiap pertanyaan survey
st.subheader("4.2.2 Uji Validitas dan Reliabilitas untuk Setiap Pertanyaan Survey:")

n = len(data_kuisioner)
alpha = 0.05
r_tabel = t.ppf(1 - alpha / 2, df=n - 2) / np.sqrt(n - 2 + t.ppf(1 - alpha / 2, df=n - 2) ** 2) 


# Kolom yang dipertahankan dari kuisioner
cols_to_keep = []
cols_to_keep.extend([col for col in data_kuisioner.columns if col.startswith(('X1.', 'X2.', 'Y'))])

merged_data = data_kuisioner[cols_to_keep]



# =========================
# KONVERSI KE NUMERIK
# =========================
item_columns = [col for col in merged_data.columns 
                if col.startswith(('X1.', 'X2.', 'Y'))]

for col in item_columns:
    merged_data[col] = pd.to_numeric(
        merged_data[col],
        errors='coerce'
    )

            
# Fungsi untuk menguji validitas
def uji_validitas(data, variable_group):

    results = []

    # Ambil item sesuai variabel
    item_cols = [
        col for col in data.columns
        if col.startswith(variable_group)
    ]

    # Pastikan numerik
    data_items = data[item_cols].apply(
        pd.to_numeric,
        errors='coerce'
    )
    # Hitung skor total untuk grup variabel
    skor_total = data_items.sum(axis=1)
    # Uji validitas untuk setiap item
    for item in item_cols:
        # Hitung korelasi Pearson antara item dan skor total
        validitas, _ = pearsonr(data_items[item].dropna(), skor_total.dropna())
        keterangan = "Valid" if abs(validitas) > r_tabel else "Tidak Valid"
        results.append({
            'Item': item,
            'r_hitung': round(validitas, 3), 
            'r_tabel': round(r_tabel, 3),
            'Validitas': keterangan
        })
        
    return pd.DataFrame(results)

# Uji validitas X1
g1, g2 = st.columns((1,0.6))
with g1:
    st.write("a. Uji Validitas X1 (Reward):")
    validitas_x1 = uji_validitas(merged_data, 'X1')
    st.dataframe(validitas_x1, use_container_width=True)
with g2:
    fig, ax = plt.subplots()
    ax.pie(validitas_x1['Validitas'].value_counts().values, labels=validitas_x1['Validitas'].value_counts().index, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')
    st.pyplot(fig)

# Uji validitas X2
g1, g2 = st.columns((1,0.6))
with g1:
    st.write("b. Uji Validitas X2 (Punishment):")
    validitas_x2 = uji_validitas(merged_data, 'X2')
    st.dataframe(validitas_x2, use_container_width=True)
with g2:
    fig, ax = plt.subplots()
    ax.pie(validitas_x2['Validitas'].value_counts().values, labels=validitas_x2['Validitas'].value_counts().index, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')
    st.pyplot(fig)

# Uji validitas Y
g1, g2 = st.columns((1,0.6))
with g1:
    st.write("c. Uji Validitas Y (Kepatuhan Presensi Digital):")
    validitas_y = uji_validitas(merged_data, 'Y')
    st.dataframe(validitas_y, use_container_width=True)

with g2:
    fig, ax = plt.subplots()
    ax.pie(validitas_y['Validitas'].value_counts().values, labels=validitas_y['Validitas'].value_counts().index, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')
    st.pyplot(fig)

# Uji reliabilitas untuk seluruh grup variabel
st.write("Uji Reliabilitas (Gabungan X1, X2, dan Y):")

def uji_reliabilitas(data, variable_groups):
    """
    Menguji reliabilitas menggunakan Cronbach's Alpha untuk gabungan grup variabel
    """
    item_cols = []
    for var_group in variable_groups:
        item_cols.extend([col for col in data.columns if col.startswith(var_group)])
    
    data_items = data[item_cols].apply(
        pd.to_numeric,
        errors='coerce'
    )
    
    # Hitung skor total
    skor_total = data_items.sum(axis=1)
    
    # Hitung varians total dan varians item
    var_total = skor_total.var()
    var_items = data_items.var()
    
    # Hitung Cronbach's Alpha
    n_items = len(item_cols)
    alpha = (n_items / (n_items - 1)) * (1 - var_items.sum() / var_total) if var_total > 0 else 0
    
    keterangan = "Reliabel" if alpha >= 0.6 else "Tidak Reliabel"
    
    return {
        'Variabel': 'Gabungan X1, X2, Y',
        'Cronbach\'s Alpha': round(alpha, 3),
        'Keterangan': keterangan
    }

reliabilitas_result = uji_reliabilitas(merged_data, ['X1', 'X2', 'Y'])
reliabilitas_df = pd.DataFrame([reliabilitas_result])
st.dataframe(reliabilitas_df, use_container_width=True)

# Uji normalitas menggunakan kolmogorov-smirnov untuk seluruh variabel
st.subheader("4.2.3 Hasil Uji Asumsi Klasik:")
st.write("4.2.3.1 Uji Normalitas:")
st.write("Dasar Pengambilan Keputusan:") 
st.write("• Jika Sig. > 0,05 → data berdistribusi normal:")
st.write("• Jika Sig. ≤ 0,05 → data tidak normal:")

def uji_normalitas(data, variable_group, label):
    """
    Menguji normalitas menggunakan Kolmogorov-Smirnov untuk grup variabel tertentu
    """
    item_cols = [col for col in data.columns if col.startswith(variable_group)]
    skor_total = data[item_cols].sum(axis=1).dropna()
        
    # Uji Kolmogorov-Smirnov
    statistic, p_value = kstest(skor_total, 'norm', args=(skor_total.mean(), skor_total.std()))
    
    # Tentukan keterangan
    keterangan = "Normal" if p_value > 0.05 else "Tidak normal"
    
    return {
        'Mean': round(skor_total.mean(), 3),
        'Std Dev': round(skor_total.std(), 3),
        'Statistic': round(statistic, 3),
        "p_value": round(p_value, 3),
        'Variabel': label,
        'N': len(data),
        'Sig. (K-S)': round(p_value, 3),
        'Keterangan': keterangan
    }

# Uji normalitas untuk X1, X2, Y
normalitas_results = [
    uji_normalitas(merged_data, 'X1', 'Reward (X1)'),
    uji_normalitas(merged_data, 'X2', 'Sanksi (X2)'),
    uji_normalitas(merged_data, 'Y', 'Kepatuhan Presensi (Y)')
]

normalitas_df = pd.DataFrame(normalitas_results)
st.dataframe(normalitas_df, use_container_width=True)

# uji normalitas menggunakan kolmogorov smirnov untuk semua variabel secara total
st.write("Uji Normalitas Menggunakan Kolmogorov-Smirnov untuk Semua Variabel Secara Total:")
merged_data['Total_Skor'] = merged_data[[col for col in merged_data.columns if col.startswith(('X1.', 'X2.', 'Y'))]].sum(axis=1)
statistic, p_value = kstest(merged_data['Total_Skor'].dropna(), 'norm', args=(merged_data['Total_Skor'].mean(), merged_data['Total_Skor'].std()))
keterangan = "Normal" if p_value > 0.05 else "Tidak normal"
normalitas_total_df = pd.DataFrame([{
    'Mean': round(merged_data['Total_Skor'].mean(), 3),
    'Std Dev': round(merged_data['Total_Skor'].std(), 3),
    'Statistic': round(statistic, 3),
    "p_value": round(p_value, 3),
    'Variabel': 'Total Skor',
    'N': len(merged_data),
    'Sig. (K-S)': round(p_value, 3),
    'Keterangan': keterangan
}])
st.dataframe(normalitas_total_df, use_container_width=True)

# Uji normalitas menggunakan kolmogorov smirnov untuk satu sampel dengan dasar penentuan: Sig. > 0,05 → data berdistribusi normal dan jika Sig. ≤ 0,05 → data tidak normal
st.write("Uji Normalitas Menggunakan Kolmogorov-Smirnov untuk Satu Sampel dengan Dasar Penentuan:")
st.write("• Sig. > 0,05 → data berdistribusi normal:")
st.write("• Sig. ≤ 0,05 → data tidak normal:")
statistic, p_value = kstest(merged_data['Total_Skor'].dropna(), 'norm', args=(merged_data['Total_Skor'].mean(), merged_data['Total_Skor'].std()))
keterangan = "Normal" if p_value > 0.05 else "Tidak normal"
normalitas_satu_sampel_df = pd.DataFrame([{
    'Mean': round(merged_data['Total_Skor'].mean(), 3),
    'Std Dev': round(merged_data['Total_Skor'].std(), 3),
    'Statistic': round(statistic, 3),
    "p_value": round(p_value, 3),
    'Variabel': 'Total Skor',
    'N': len(merged_data),
    'Sig. (K-S)': round(p_value, 3),
    'Keterangan': keterangan
}])
st.dataframe(normalitas_satu_sampel_df, use_container_width=True)

# uji multikolinearitas menggunakan korelasi Pearson untuk variabel reward (X1) dan variabel sanksi (X2)
st.write("4.2.3.2 Uji Multikolinearitas untuk Variabel X1 (Reward) dan X2 (Sanksi):")
st.write("Dasar Pengambilan Keputusan:") 
st.write("• Tolerance > 0,10 → tidak terjadi multikolinearitas:")
st.write("• VIF < 10 → tidak terjadi multikolinearitas:")

def uji_multikolinearitas(data, variable_groups):
    """
    Menguji multikolinearitas menggunakan korelasi Pearson dan VIF
    """
    results = []
    
    # Hitung skor total untuk setiap grup variabel
    skor_groups = {}
    for var_group, label in variable_groups:
        item_cols = [col for col in data.columns if col.startswith(var_group)]
        skor_groups[var_group] = data[item_cols].sum(axis=1)
    
    # Hitung korelasi Pearson antar variabel
    var_list = list(skor_groups.keys())
    correlation_matrix = np.corrcoef([skor_groups[var] for var in var_list])[0, 1]
    
    # Hitung VIF dan Tolerance untuk setiap variabel
    for i, (var_group, label) in enumerate(variable_groups):
        # VIF = 1 / (1 - R²)
        # R² adalah korelasi Pearson kuadrat
        r_squared = correlation_matrix ** 2
        tolerance = 1 - r_squared
        vif = 1 / tolerance if tolerance != 0 else float('inf')
        
        keterangan = "Tidak terjadi multikolinearitas" if vif < 10 else "Terjadi multikolinearitas"
        
        results.append({
            'Variabel': label,
            'Tolerance': round(tolerance, 3),
            'VIF': round(vif, 3),
            'Keterangan': keterangan
        })
    
    return pd.DataFrame(results)

multikolinearitas_df = uji_multikolinearitas(merged_data, [('X1', 'Reward (X1)'), ('X2', 'Sanksi (X2)')])
st.dataframe(multikolinearitas_df, use_container_width=True)

# Uji Regresi Linear Berganda

from scipy import stats

def uji_regresi_linear_berganda(X, y):
    """
    Menguji regresi linear berganda dengan perhitungan koefisien, t hitung, dan signifikansi
    """
    # Tambahkan kolom konstanta
    X_with_const = np.column_stack([np.ones(len(X)), X])
    
    # Hitung koefisien regresi
    beta = np.linalg.lstsq(X_with_const, y, rcond=None)[0]
    
    # Hitung prediksi
    y_pred = X_with_const @ beta
    
    # Hitung residual
    residual = y - y_pred
    
    # Hitung SSR, SSE, SST
    sse = np.sum(residual ** 2)
    ssr = np.sum((y_pred - np.mean(y)) ** 2)
    sst = np.sum((y - np.mean(y)) ** 2)
    
    # Hitung MSE
    n = len(y)
    k = X.shape[1]
    mse = sse / (n - k - 1)
    
    # Hitung standard error untuk setiap koefisien
    var_covar = mse * np.linalg.inv(X_with_const.T @ X_with_const)
    se = np.sqrt(np.diag(var_covar))
    
    # Hitung t hitung
    t_hitung = beta / se
    
    # Hitung p-value (signifikansi)
    p_values = [2 * (1 - stats.t.cdf(abs(t), n - k - 1)) for t in t_hitung]
    
    results = []
    
    # Konstanta
    keterangan = "-"
    results.append({
        'Variabel': 'Konstanta',
        'Koefisien (B)': round(beta[0], 3),
        't hitung': round(t_hitung[0], 3),
        'Sig.': round(p_values[0], 3),
        'Keterangan': keterangan
    })
    
    # Variabel independen
    var_names = ['Reward (X1)', 'Sanksi (X2)']
    for i, var_name in enumerate(var_names):
        sig = p_values[i + 1]
        keterangan = "Signifikan" if sig < 0.05 else "Tidak Signifikan"
        results.append({
            'Variabel': var_name,
            'Koefisien (B)': round(beta[i + 1], 3),
            't hitung': round(t_hitung[i + 1], 3),
            'Sig.': round(sig, 3),
            'Keterangan': keterangan
        })
    
    return pd.DataFrame(results)

# Persiapkan data untuk regresi
X1_cols = [col for col in merged_data.columns if col.startswith('X1')]
X2_cols = [col for col in merged_data.columns if col.startswith('X2')]
Y_cols = [col for col in merged_data.columns if col.startswith('Y')]

X1_scores = merged_data[X1_cols].sum(axis=1).values
X2_scores = merged_data[X2_cols].sum(axis=1).values
Y_scores = merged_data[Y_cols].sum(axis=1).values

X = np.column_stack([X1_scores, X2_scores])
y = Y_scores

# Jalankan uji regresi
regresi_df = uji_regresi_linear_berganda(X, y)
st.subheader("4.2.4 Uji Regresi Linear Berganda:")
st.write("Dasar Penentuan:", "Sig. < 0,05 → Signifikan" " dan jika Sig. > 0,05 → Tidak signifikan")
st.dataframe(regresi_df, use_container_width=True)

# Pengujian hipotesis untuk uji t dengan dasar penentuan: Sig. < 0,05 → Tolak H0 (Signifikan) dan jika Sig. > 0,05 → Gagal Tolak H0 (Tidak signifikan)
st.subheader("4.2.5 Pengujian Hipotesis:")
st.write("1. Uji t:")
st.write("Dasar Penentuan:", "Sig. < 0,05 → Signifikan" " atau jika thitung > ttabel (ttabel 52 sampel = 2,020)")

# Format hasil pengujian hipotesis
hipotesis_results = []
var_names = ['Reward (X1)', 'Sanksi (X2)']
for i, var_name in enumerate(var_names):
    sig = regresi_df.loc[i + 1, 'Sig.']
    t_value = regresi_df.loc[i + 1, 't hitung']
    keterangan = "Berpengaruh signifikan" if sig < 0.05 else "Tidak Berpengaruh signifikan"
    hipotesis_results.append({
        'Variabel': var_name,
        'Sig.': sig,
        'T': t_value,
        'Keterangan': keterangan
    })

hipotesis_df = pd.DataFrame(hipotesis_results)
st.dataframe(hipotesis_df, use_container_width=True)

# pengujian hipotesis untuk uji F dengan dasar penentuan: Sig. < 0,05 → Tolak H0 (Signifikan) dan jika Sig. > 0,05 → Gagal Tolak H0 (Tidak signifikan)
st.write("2. Uji F:")
st.write("Dasar Penentuan:", "Sig. < 0,05 → Signifikan" " atau jika fhitung> ftabel (ftabel 52 sampel = 3,187)")
# Hitung F hitung dan signifikansi
X_with_const = np.column_stack([np.ones(len(X)), X])
beta = np.linalg.lstsq(X_with_const, y, rcond=None)[0]
y_pred = X_with_const @ beta
residual = y - y_pred

sse = np.sum(residual ** 2)
ssr = np.sum((y_pred - np.mean(y)) ** 2)
sst = np.sum((y - np.mean(y)) ** 2)

n = len(y)
k = X.shape[1]

msr = ssr / k
mse = sse / (n - k - 1)
f_hitung = msr / mse

p_value_f = 1 - stats.f.cdf(f_hitung, k, n - k - 1)
keterangan_f = "Signifikan" if p_value_f < 0.05 else "Tidak signifikan"

uji_f_df = pd.DataFrame([{
    'F hitung': round(f_hitung, 3),
    'Sig.': f"<{p_value_f:.3f}" if p_value_f < 0.001 else round(p_value_f, 3),
    'Keterangan': keterangan_f
}])

st.dataframe(uji_f_df, use_container_width=True)

# Uji Koefisien Determinasi (R²)
st.subheader("4.2.6 Uji Koefisien Determinasi (R²):")

r_square = ssr / sst
r_square_percent = r_square * 100

koef_det_df = pd.DataFrame([{
    'R Square': round(r_square, 3),
    'Keterangan': f"{round(r_square_percent, 1)}%"
}])

st.dataframe(koef_det_df)

# Menampilkan data hasil survey
st.write("Data Hasil Survey:")
st.dataframe(data_kuisioner, use_container_width=True)

# Menampilkan data pertanyaan survey
st.write("Data Pertanyaan Survey:")
st.dataframe(data_pertanyaan, use_container_width=True)

# menampilkan r_tabel
st.write("Tabel R Tabel untuk Uji Validitas:")
st.dataframe(r_tabel_df, use_container_width=True)