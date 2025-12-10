import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# ================= KONFIGURASI HALAMAN =================
st.set_page_config(
    page_title="Portfolio Regina Ria Aurellia",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ================= TEMA HITAM CSS =================
st.markdown("""
<style>
    /* Latar belakang utama */
    .stApp {
        background: #000000;
    }
    
    /* Styling kartu */
    .card {
        background: rgba(20, 20, 20, 0.95);
        border-radius: 15px;
        padding: 25px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
        margin-bottom: 20px;
        border-left: 5px solid #00ffff;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(100, 100, 100, 0.3);
    }
    
    /* Kartu metrik */
    .metric-card {
        background: linear-gradient(135deg, rgba(30, 30, 30, 0.95) 0%, rgba(50, 50, 50, 0.95) 100%);
        border-radius: 12px;
        padding: 20px;
        text-align: center;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.4);
        border: 1px solid rgba(100, 100, 100, 0.3);
    }
    
    /* Bingkai foto */
    .photo-frame {
        width: 200px;
        height: 200px;
        border-radius: 50%;
        overflow: hidden;
        border: 5px solid rgba(50, 50, 50, 0.9);
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.5);
        margin: 0 auto;
    }
    
    /* Header kustom */
    .section-header {
        color: #ffffff;
        font-size: 1.8rem;
        margin-bottom: 1.5rem;
        padding-bottom: 0.5rem;
        border-bottom: 3px solid #00ffff;
        display: inline-block;
        font-weight: 600;
    }
    
    /* Styling tombol */
    .stButton > button {
        background: linear-gradient(135deg, #00ffff 0%, #0088ff 100%);
        color: black;
        border: none;
        padding: 12px 25px;
        border-radius: 25px;
        font-weight: 600;
        transition: all 0.3s;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 7px 20px rgba(0, 255, 255, 0.4);
        background: linear-gradient(135deg, #00cccc 0%, #0066cc 100%);
    }
    
    /* Styling timeline */
    .timeline-item {
        padding-left: 25px;
        border-left: 3px solid #00ffff;
        margin-bottom: 20px;
        position: relative;
    }
    
    .timeline-item:before {
        content: "●";
        position: absolute;
        left: -10px;
        color: #00ffff;
        font-size: 20px;
        background: #000000;
        border-radius: 50%;
        width: 20px;
        height: 20px;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    
    /* Warna teks kustom */
    h1, h2, h3, h4, h5, h6 {
        color: #ffffff !important;
    }
    
    p, span, li, td, th {
        color: #cccccc !important;
    }
    
    strong {
        color: #ffffff !important;
    }
    
    /* Styling tautan */
    a {
        color: #00ffff !important;
        text-decoration: none;
    }
    
    a:hover {
        color: #66ffff !important;
        text-decoration: underline;
    }
    
    /* Styling sidebar */
    .css-1d391kg, .css-12oz5g7 {
        background-color: #000000 !important;
    }
    
    /* Styling input teks */
    .stTextInput > div > div > input {
        background-color: #1a1a1a;
        color: #ffffff;
        border: 1px solid #444444;
    }
    
    /* Styling kotak pilih */
    .stSelectbox > div > div > select {
        background-color: #1a1a1a;
        color: #ffffff;
        border: 1px solid #444444;
    }
    
    /* Pembatas */
    hr {
        border-color: #333333 !important;
    }
</style>
""", unsafe_allow_html=True)

# ================= HEADER DENGAN FOTO =================
col1, col2 = st.columns([1, 2])

with col1:
    st.markdown("""
    <div class="photo-frame">
        <img src="https://images.unsplash.com/photo-1580489944761-15a19d654956?ixlib=rb-4.0.3&auto=format&fit=crop&w=500&q=80" 
             style="width:100%; height:100%; object-fit:cover;">
    </div>
    """, unsafe_allow_html=True)
    
    # Kontak cepat
    st.markdown("""
    <div style="text-align:center; margin-top:20px;">
        <p style="color:#00ffff; font-weight:600;">📧 aurelliarial0@gmail.com</p>
        <p style="color:#00ffff; font-weight:600;">📱 081 225 805 910</p>
        <p style="color:#888888;">📍 Salatiga, Jawa Tengah</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <h1 style="color: #ffffff; margin-bottom: 10px;">🏦 Regina Ria Aurellia</h1>
        <h3 style="color: #00ffff; margin-bottom: 20px;">Profesional Perbankan | Peminat Data</h3>
        
        <p style="font-size: 1.1rem; color: #cccccc; line-height: 1.6;">
        Lulusan <strong>S1 Pendidikan Matematika Cum Laude</strong> dengan pengalaman 
        <strong>3 tahun sebagai Teller di BCA</strong>. Menggabungkan kemampuan analitis 
        matematika dengan pengalaman praktis perbankan untuk menciptakan solusi berbasis data.
        </p>
        
        <div style="display: flex; gap: 15px; margin-top: 25px;">
            <div style="background: linear-gradient(135deg, #00ff88 0%, #00cc66 100%); color: black; padding: 8px 15px; border-radius: 20px; font-weight: 600; border: 1px solid rgba(255,255,255,0.1);">
                🎓 Cum Laude
            </div>
            <div style="background: linear-gradient(135deg, #00ffff 0%, #0088ff 100%); color: black; padding: 8px 15px; border-radius: 20px; font-weight: 600; border: 1px solid rgba(255,255,255,0.1);">
                🏦 Pengalaman BCA
            </div>
            <div style="background: linear-gradient(135deg, #ff00ff 0%, #cc00cc 100%); color: white; padding: 8px 15px; border-radius: 20px; font-weight: 600; border: 1px solid rgba(255,255,255,0.1);">
                📊 Analisis Data
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ================= METRIK KINERJA =================
st.markdown('<h2 class="section-header">📊 Sorotan Kinerja di BCA</h2>', unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="metric-card">
        <div style="font-size: 2.5rem; color: #00ff88; font-weight: 700;">99.8%</div>
        <div style="color: #cccccc; font-size: 0.9rem;">AKURASI TRANSAKSI</div>
        <div style="color: #00ff88; font-size: 0.8rem; margin-top: 5px;">↑ +1.8% di atas target</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="metric-card">
        <div style="font-size: 2.5rem; color: #00ffff; font-weight: 700;">4.7/5.0</div>
        <div style="color: #cccccc; font-size: 0.9rem;">KEPUASAN NASABAH</div>
        <div style="color: #00ffff; font-size: 0.8rem; margin-top: 5px;">↑ +0.4 di atas target</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="metric-card">
        <div style="font-size: 2.5rem; color: #ff00ff; font-weight: 700;">180-200</div>
        <div style="color: #cccccc; font-size: 0.9rem;">TRANSAKSI HARIAN</div>
        <div style="color: #ff00ff; font-size: 0.8rem; margin-top: 5px;">↑ 20% di atas rata-rata</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="metric-card">
        <div style="font-size: 2.5rem; color: #ffaa00; font-weight: 700;">Rp 1M</div>
        <div style="color: #cccccc; font-size: 0.9rem;">PENANGANAN KAS HARIAN</div>
        <div style="color: #ffaa00; font-size: 0.8rem; margin-top: 5px;">↓ 0% perbedaan</div>
    </div>
    """, unsafe_allow_html=True)

# ================= ANALISIS TRANSAKSI =================
st.markdown('<h2 class="section-header">💰 Dashboard Analisis Transaksi</h2>', unsafe_allow_html=True)

# Generate data contoh
np.random.seed(42)
dates = pd.date_range('2024-01-01', periods=30, freq='D')
data = pd.DataFrame({
    'Tanggal': dates,
    'Transaksi': np.random.randint(150, 220, 30),
    'Aliran Kas (Juta Rp)': np.random.randint(500, 1200, 30),
    'Kepuasan Nasabah': np.round(np.random.uniform(4.3, 5.0, 30), 2),
    'Kesalahan': np.random.randint(0, 2, 30)
})

col1, col2 = st.columns([2, 1])

with col1:
    # Grafik tren transaksi
    st.markdown("""
    <div class="card">
        <h4 style="color: #ffffff;">📈 Tren Volume Transaksi</h4>
    """, unsafe_allow_html=True)
    st.line_chart(data.set_index('Tanggal')['Transaksi'], height=300)
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    # Ringkasan statistik
    st.markdown("""
    <div class="card">
        <h4 style="color: #ffffff;">📊 Ringkasan Bulanan</h4>
        <div style="margin: 15px 0;">
            <div style="display: flex; justify-content: space-between; margin: 10px 0;">
                <span style="color: #cccccc;">Total Transaksi:</span>
                <strong style="color: #00ffff;">{:,}</strong>
            </div>
            <div style="display: flex; justify-content: space-between; margin: 10px 0;">
                <span style="color: #cccccc;">Rata-rata Harian:</span>
                <strong style="color: #00ffff;">{:.0f}</strong>
            </div>
            <div style="display: flex; justify-content: space-between; margin: 10px 0;">
                <span style="color: #cccccc;">Total Aliran Kas:</span>
                <strong style="color: #00ffff;">Rp {:.1f} M</strong>
            </div>
            <div style="display: flex; justify-content: space-between; margin: 10px 0;">
                <span style="color: #cccccc;">Rata-rata Kepuasan:</span>
                <strong style="color: #00ffff;">{:.2f}/5.0</strong>
            </div>
        </div>
    </div>
    """.format(
        data['Transaksi'].sum(),
        data['Transaksi'].mean(),
        data['Aliran Kas (Juta Rp)'].sum() / 1000,
        data['Kepuasan Nasabah'].mean()
    ), unsafe_allow_html=True)

# ================= TIMELINE PENGALAMAN =================
st.markdown('<h2 class="section-header">🎓 Garis Waktu Karir</h2>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card">
        <h4 style="color: #ffffff; display: flex; align-items: center; gap: 10px;">
            <div style="background: #00ff88; color: black; width: 40px; height: 40px; border-radius: 50%; display: flex; align-items: center; justify-content: center;">🎓</div>
            Pendidikan
        </h4>
        <div class="timeline-item">
            <strong>S1 Pendidikan Matematika</strong><br>
            <em style="color: #888888;">Universitas Kristen Satya Wacana</em><br>
            <small style="color: #666666;">2017 - 2021 • Cum Laude</small>
        </div>
        <div class="timeline-item">
            <strong>SMA Negeri 2 Salatiga</strong><br>
            <em style="color: #888888;">Jurusan MIPA</em><br>
            <small style="color: #666666;">2014 - 2017</small>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <h4 style="color: #ffffff; display: flex; align-items: center; gap: 10px;">
            <div style="background: #00ffff; color: black; width: 40px; height: 40px; border-radius: 50%; display: flex; align-items: center; justify-content: center;">🏦</div>
            Pengalaman Perbankan
        </h4>
        <div class="timeline-item">
            <strong>Teller - BCA Singosaren Solo</strong><br>
            <em style="color: #888888;">Penuh Waktu • Operasional Perbankan</em><br>
            <small style="color: #666666;">Maret 2022 - Maret 2025</small>
            <ul style="margin: 10px 0 0 20px; color: #cccccc;">
                <li>Akurasi transaksi 99.8%</li>
                <li>PIC Proyek Kaizen</li>
                <li>Mentor 3 teller baru</li>
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
        <h4 style="color: #ffffff; display: flex; align-items: center; gap: 10px;">
            <div style="background: #ff00ff; color: white; width: 40px; height: 40px; border-radius: 50%; display: flex; align-items: center; justify-content: center;">💼</div>
            Pengalaman Lainnya
        </h4>
        <div class="timeline-item">
            <strong>Tutor Keuangan</strong><br>
            <em style="color: #888888;">Privat & Bimbingan Belajar</em><br>
            <small style="color: #666666;">2021 - 2023</small>
        </div>
        <div class="timeline-item">
            <strong>Master Teacher</strong><br>
            <em style="color: #888888;">Ruang Guru</em><br>
            <small style="color: #666666;">2021</small>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ================= KE AHLIAN =================
st.markdown('<h2 class="section-header">🛠 Keahlian & Kompetensi</h2>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card">
        <h4 style="color: #ffffff;">💻 Keahlian Teknis</h4>
        <div style="margin-top: 15px;">
            <div style="display: flex; justify-content: space-between; margin: 8px 0;">
                <span style="color: #cccccc;">Python & Analisis Data</span>
                <div style="display: flex; gap: 3px;">
                    <div style="width: 12px; height: 12px; background: #00ff88; border-radius: 2px;"></div>
                    <div style="width: 12px; height: 12px; background: #00ff88; border-radius: 2px;"></div>
                    <div style="width: 12px; height: 12px; background: #00ff88; border-radius: 2px;"></div>
                    <div style="width: 12px; height: 12px; background: #00ff88; border-radius: 2px;"></div>
                    <div style="width: 12px; height: 12px; background: #333333; border-radius: 2px;"></div>
                </div>
            </div>
            <div style="display: flex; justify-content: space-between; margin: 8px 0;">
                <span style="color: #cccccc;">Microsoft Office Suite</span>
                <div style="display: flex; gap: 3px;">
                    <div style="width: 12px; height: 12px; background: #00ffff; border-radius: 2px;"></div>
                    <div style="width: 12px; height: 12px; background: #00ffff; border-radius: 2px;"></div>
                    <div style="width: 12px; height: 12px; background: #00ffff; border-radius: 2px;"></div>
                    <div style="width: 12px; height: 12px; background: #00ffff; border-radius: 2px;"></div>
                    <div style="width: 12px; height: 12px; background: #00ffff; border-radius: 2px;"></div>
                </div>
            </div>
            <div style="display: flex; justify-content: space-between; margin: 8px 0;">
                <span style="color: #cccccc;">SQL & Database</span>
                <div style="display: flex; gap: 3px;">
                    <div style="width: 12px; height: 12px; background: #ff00ff; border-radius: 2px;"></div>
                    <div style="width: 12px; height: 12px; background: #ff00ff; border-radius: 2px;"></div>
                    <div style="width: 12px; height: 12px; background: #ff00ff; border-radius: 2px;"></div>
                    <div style="width: 12px; height: 12px; background: #333333; border-radius: 2px;"></div>
                    <div style="width: 12px; height: 12px; background: #333333; border-radius: 2px;"></div>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <h4 style="color: #ffffff;">🏦 Keahlian Perbankan</h4>
        <div style="margin-top: 15px;">
            <div style="background: rgba(0, 0, 0, 0.5); padding: 10px 15px; border-radius: 8px; margin: 8px 0; border: 1px solid #333333;">
                💰 Penanganan & Pemrosesan Kas
            </div>
            <div style="background: rgba(0, 0, 0, 0.5); padding: 10px 15px; border-radius: 8px; margin: 8px 0; border: 1px solid #333333;">
                👥 Layanan Nasabah Unggul
            </div>
            <div style="background: rgba(0, 0, 0, 0.5); padding: 10px 15px; border-radius: 8px; margin: 8px 0; border: 1px solid #333333;">
                ⚠️ Manajemen Risiko
            </div>
            <div style="background: rgba(0, 0, 0, 0.5); padding: 10px 15px; border-radius: 8px; margin: 8px 0; border: 1px solid #333333;">
                📋 Kepatuhan & SOP
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
        <h4 style="color: #ffffff;">🌟 Soft Skills</h4>
        <div style="margin-top: 15px;">
            <div style="display: flex; align-items: center; gap: 10px; margin: 10px 0;">
                <div style="color: #00ff88; font-size: 1.5rem;">✓</div>
                <span style="color: #cccccc;">Detail-Oriented (akurasi 99.8%)</span>
            </div>
            <div style="display: flex; align-items: center; gap: 10px; margin: 10px 0;">
                <div style="color: #00ffff; font-size: 1.5rem;">✓</div>
                <span style="color: #cccccc;">Kepemimpinan & Mentoring Tim</span>
            </div>
            <div style="display: flex; align-items: center; gap: 10px; margin: 10px 0;">
                <div style="color: #ff00ff; font-size: 1.5rem;">✓</div>
                <span style="color: #cccccc;">Pemecahan Masalah</span>
            </div>
            <div style="display: flex; align-items: center; gap: 10px; margin: 10px 0;">
                <div style="color: #ffaa00; font-size: 1.5rem;">✓</div>
                <span style="color: #cccccc;">Komunikasi</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ================= FOOTER =================
st.markdown("""
<div class="card" style="text-align: center; margin-top: 50px;">
    <h3 style="color: #ffffff;">Mari Terhubung!</h3>
    <p style="color: #cccccc; margin: 20px 0;">
        Tertarik mendiskusikan teknologi perbankan, analisis data, atau peluang karir?
    </p>
    
    <div style="display: flex; justify-content: center; gap: 20px; margin: 30px 0;">
        <a href="mailto:aurelliarial0@gmail.com" style="text-decoration: none;">
            <div style="background: linear-gradient(135deg, #00ffff 0%, #0088ff 100%); color: black; padding: 12px 25px; border-radius: 25px; font-weight: 600; display: flex; align-items: center; gap: 8px; border: 1px solid rgba(255,255,255,0.1);">
                📧 Email Saya
            </div>
        </a>
        <a href="https://wa.me/6281225805910" style="text-decoration: none;">
            <div style="background: linear-gradient(135deg, #00ff88 0%, #00cc66 100%); color: black; padding: 12px 25px; border-radius: 25px; font-weight: 600; display: flex; align-items: center; gap: 8px; border: 1px solid rgba(255,255,255,0.1);">
                💬 WhatsApp
            </div>
        </a>
        <a href="https://github.com/ReginaRiaAurellia" style="text-decoration: none;">
            <div style="background: linear-gradient(135deg, #333333 0%, #000000 100%); color: white; padding: 12px 25px; border-radius: 25px; font-weight: 600; display: flex; align-items: center; gap: 8px; border: 1px solid rgba(255,255,255,0.1);">
                💻 GitHub
            </div>
        </a>
    </div>
    
    <p style="color: #888888; font-size: 0.9rem; margin-top: 20px;">
        <em>"Dari menghitung uang tunai hingga menganalisis data – Mentransformasi perbankan dengan matematika & teknologi"</em><br>
        © 2024 Regina Ria Aurellia • Portfolio Dibuat dengan Streamlit
    </p>
</div>
""", unsafe_allow_html=True)

# ================= KONTEN SIDEBAR =================
with st.sidebar:
    st.markdown("""
    <div class="card" style="margin-bottom: 20px;">
        <h4 style="color: #ffffff; margin-bottom: 15px;">🔗 Tautan Cepat</h4>
        <div style="display: flex; flex-direction: column; gap: 10px;">
            <a href="#performance" style="text-decoration: none;">
                <div style="color: #cccccc; padding: 10px; border-radius: 8px; background: rgba(0, 0, 0, 0.5); text-align: center; border: 1px solid #333333;">
                    📊 Metrik Kinerja
                </div>
            </a>
            <a href="#timeline" style="text-decoration: none;">
                <div style="color: #cccccc; padding: 10px; border-radius: 8px; background: rgba(0, 0, 0, 0.5); text-align: center; border: 1px solid #333333;">
                    🎓 Garis Waktu Karir
                </div>
            </a>
            <a href="#skills" style="text-decoration: none;">
                <div style="color: #cccccc; padding: 10px; border-radius: 8px; background: rgba(0, 0, 0, 0.5); text-align: center; border: 1px solid #333333;">
                    🛠 Keahlian & Kompetensi
                </div>
            </a>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Tombol unduh CV
    if st.button("📄 Unduh CV / Portfolio", use_container_width=True):
        st.success("Tautan unduh CV akan tersedia di sini!")
    
    # Toggle tema (visual saja)
    st.markdown("""
    <div class="card">
        <h4 style="color: #ffffff; margin-bottom: 10px;">🎨 Tema</h4>
        <div style="display: flex; gap: 10px;">
            <div style="width: 30px; height: 30px; background: #000000; border-radius: 5px; cursor: pointer; border: 2px solid #00ffff;"></div>
            <div style="width: 30px; height: 30px; background: #111111; border-radius: 5px; cursor: pointer;"></div>
            <div style="width: 30px; height: 30px; background: #222222; border-radius: 5px; cursor: pointer;"></div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Sertifikasi
    st.markdown("""
    <div class="card">
        <h4 style="color: #ffffff; margin-bottom: 10px;">🏆 Sertifikasi</h4>
        <div style="display: flex; flex-direction: column; gap: 8px;">
            <div style="background: rgba(0, 0, 0, 0.5); padding: 10px; border-radius: 8px; border-left: 3px solid #00ff88;">
                <small style="color: #888888;">BCA</small><br>
                <span style="color: #cccccc; font-size: 0.9rem;">Sertifikasi Teller</span>
            </div>
            <div style="background: rgba(0, 0, 0, 0.5); padding: 10px; border-radius: 8px; border-left: 3px solid #00ffff;">
                <small style="color: #888888;">Coursera</small><br>
                <span style="color: #cccccc; font-size: 0.9rem;">Python untuk Data Science</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Informasi tambahan
    st.markdown("""
    <div class="card">
        <h4 style="color: #ffffff; margin-bottom: 10px;">ℹ️ Informasi</h4>
        <div style="display: flex; flex-direction: column; gap: 8px;">
            <div style="display: flex; align-items: center; gap: 10px;">
                <div style="color: #00ffff;">🌐</div>
                <span style="color: #cccccc; font-size: 0.9rem;">Portfolio Online</span>
            </div>
            <div style="display: flex; align-items: center; gap: 10px;">
                <div style="color: #00ff88;">📅</div>
                <span style="color: #cccccc; font-size: 0.9rem;">Diperbarui: Des 2024</span>
            </div>
            <div style="display: flex; align-items: center; gap: 10px;">
                <div style="color: #ff00ff;">💡</div>
                <span style="color: #cccccc; font-size: 0.9rem;">Tersedia untuk proyek</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
