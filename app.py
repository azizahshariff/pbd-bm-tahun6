import streamlit as st
import pandas as pd
import google.generativeai as genai

# Konfigurasi Paparan Web
st.set_page_config(page_title="PBD BM Tahun 6 - SK Simpang Rengam", page_icon="📚", layout="wide")

st.title("🇲🇾 Dashboard PBD Bahasa Melayu Tahun 6")
st.subheader("SK Simpang Rengam | Sesi Akademik 2026/2027")
st.markdown("---")

# Ambil API Key daripada Vercel Secrets
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# Tetapan Menu Pilihan
st.sidebar.header("Tetapan Menu Guru")
pilih_kelas = st.sidebar.selectbox("Pilih Kelas", ["6 Setia", "6 Mulia"])
nama_murid = st.sidebar.text_input("Nama Murid", "Aariz Farhad Bin Joffry")
tahap_tp = st.sidebar.slider("Tahap Penguasaan (TP) Semasa", 1, 6, 3)

st.write("### Paparan Profil Pentaksiran Murid")
st.info(f"Murid: **{nama_murid}** | Kelas: **{pilih_kelas}** | Tahap Penguasaan Semasa: **TP {tahap_tp}**")

# Integrasi Google AI untuk Ulasan / Intervensi
if st.button("Jana Cadangan Ulasan & Intervensi (AI)"):
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        prompt = f"Berdasarkan murid Tahun 6 di SK Simpang Rengam yang mendapat Tahap Penguasaan TP{tahap_tp} dalam subjek Bahasa Melayu, berikan ulasan prestasi ringkas dan satu strategi intervensi pemulihan yang sesuai untuk guru."
        response = model.generate_content(prompt)

        st.success("Analisis AI Berjaya Dijana:")
        st.write(response.text)
    except Exception as e:
        st.error(f"Sila pastikan Gemini API Key telah disetkan dengan betul di Vercel. Ralat: {e}")
