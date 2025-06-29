import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

st.markdown("""
    <style>
    /* Ganti background utama */
    html, body, [data-testid="stApp"] {
        background:  linear-gradient(to bottom right,#130F5E, #090979, #0B6ED9);
        color: white;
    }

    /* Judul besar */
    h1, h2, h3, h4 {
        color:#aee1f9;
    }

    /* Tombol */
    .stButton > button {
        background-color: #30D14E;
        color: white;
        border-radius: 8px;
        padding: 0.5em 1em;
        font-weight: bold;
    }
    .stButton > button:hover {
        background-color: #2AD485;
        color: white;
    }
    
    .stSlider > label {
        color: white;           
        font-size: 16px;
        font-weight: 600;
    }
            
    .stDataFrame, .stTable {
        background-color: #051C05;  /* putih transparan */
        color: #002b36;
        border-radius: 10px;
        padding: 12px;
        }
            
        
    div[data-testid="stMetric"] > div > div:nth-child(1) {
        color: #ffffff !important;  /* teks angka putih */
        font-size: 28px;
        font-weight: bold;
    }
            
    div[data-testid="stMetric"] > label {
        color: #ffffff !important;  /* teks label putih */
        font-size: 16px;
        font-weight: 600;
    /* Tabel */
    .css-1d391kg p {
        color: #003049;
    }
    </style>
""", unsafe_allow_html=True)
st.set_page_config(page_title="Prediksi Rank Mobile Legends", layout="centered")



# ------------------ Judul ------------------
st.title("📈 Prediksi Tingkat Kesulitan Menaikkan Rank di Mobile Legends")


st.subheader("ANGGOTA KELOMPOK")
st.write("1. Hadi Permana (312210445)")
st.write("2. Ahmad Yuda (312210650)")
st.write("3. Muhamad Rizky Raka Pratama (312210397)")

st.subheader("🧠 Tentang Model Prediksi")
st.write("""
Model yang digunakan untuk memprediksi tingkat kesulitan dalam menaikkan rank di Mobile Legends adalah *Regresi Linear*.
Model ini bekerja dengan cara menganalisis pengaruh berbagai faktor karakteristik pemain, seperti waktu bermain, hero di kuasai,match perminggu, jumlah hero, winrate, teman mabar .
""")
st.write("""
         Semua faktor tersebut akan diolah untuk menghasilkan prediksi tingkat kesulitan dalam menaikkan rank, berdasarkan pola yang dipelajari dari dataset. Semakin besar nilai koefisien dari suatu faktor, maka faktor tersebut dianggap lebih berkontribusi terhadap peningkatan atau penurunan kesulitan menaikkan rank.

        """)

st.subheader("📌 Faktor yang Paling Mempengaruhi Kesulitan (berdasarkan data rata-rata)")
st.write(""" Tabel dan visualisasi di bawah menampilkan sejauh mana masing-masing faktor memiliki kontribusi terhadap prediksi kesulitan berdasarkan bobot model dan data rata-rata pengguna.

 """)

df = pd.read_csv("Dataset.csv")

st.dataframe(df)

# ------------------ Training Model ------------------
X = df.drop("Tingkat_Kesulitan", axis=1)
y = df["Tingkat_Kesulitan"]
model = LinearRegression()
model.fit(X, y)

# ------------------ Input User ------------------
st.subheader("🎮 Masukkan Karakteristik Bermain Kamu")

waktu = st.slider("⏱️ Waktu Main per Hari (jam)", 0, 12, 2)
hero = st.slider("🦸 Jumlah Hero yang Dikuasai", 0, 120, 10)
match = st.slider("🏆 Jumlah Match per Minggu", 0, 100, 20)
winrate = st.slider("⚔️ Winrate (%)", 0, 100, 50)
teman = st.slider("👥 Jumlah Teman Mabar", 0, 5, 2)


# ------------------ Prediksi ------------------
if st.button("🔮 Prediksi Tingkat Kesulitan"):
    input_data = np.array([[waktu, hero, match, winrate, teman]])
    pred = model.predict(input_data)[0]

    st.subheader("📊 Hasil Prediksi")
    st.metric("Nilai Kesulitan", f"{pred:.2f}")

    if pred < 4:
        tingkat = "Mudah"
        warna = "🟢"
        deskripsi = "Rank mudah dinaikkan, cocok untuk pemain aktif dan berpengalaman."
    elif 4 <= pred <= 7:
        tingkat = "Sedang"
        warna = "🟡"
        deskripsi = "Kesulitan sedang, kamu perlu konsistensi dan kerja sama tim."
    else:
        tingkat = "Sulit"
        warna = "🔴"
        deskripsi = "Rank akan sulit dinaikkan, perlu latihan, strategi, dan squad solid."

        st.markdown(f"""
<div style="
    background-color: {warna};
    padding: 1rem;
    border-radius: 10px;
    text-align: center;
    font-weight: bold;
    font-size: 18px;
    color: white;
    margin-bottom: 1rem;
">
    Tingkat Kesulitan: {tingkat}
</div>
""", unsafe_allow_html=True)

        

    (f"{warna} **Tingkat Kesulitan: {tingkat}**")
    st.markdown(f"🧠 {deskripsi}")
