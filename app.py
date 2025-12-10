import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# ================= KONFIGURASI HALAMAN =================
st.set_page_config(
    page_title="Portfolio Regina Ria Aurellia - Profesional Perbankan",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ================= TEMA HITAM ELEGAN CSS =================
st.markdown("""
<style>
    /* Latar belakang utama hitam solid */
    .stApp {
        background: #000000;
    }
    
    /* Gaya kartu dengan efek glassmorphism */
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
    
    /* Kartu metrik dengan gradien */
    .metric-card {
        background: linear-gradient(135deg, rgba(30, 30, 30, 0.95) 0%, rgba(50, 50, 50, 0.95) 100%);
        border-radius: 12px;
        padding: 20px;
        text-align: center;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.4);
        border: 1px solid rgba(100, 100, 100, 0.3);
    }
    
    /* Bingkai foto profil */
    .photo-frame {
        width: 200px;
        height: 200px;
        border-radius: 50%;
        overflow: hidden;
        border: 5px solid rgba(50, 50, 50, 0.9);
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.5);
        margin: 0 auto;
    }
    
    /* Header bagian dengan garis bawah neon */
    .section-header {
        color: #ffffff;
        font-size: 1.8rem;
        margin-bottom: 1.5rem;
        padding-bottom: 0.5rem;
        border-bottom: 3px solid #00ffff;
        display: inline-block;
        font-weight: 600;
    }
    
    /* Tombol dengan efek hover */
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
    
    /* Timeline dengan titik indikator */
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
    
    /* Warna teks untuk semua heading */
    h1, h2, h3, h4, h5, h6 {
        color: #ffffff !important;
    }
    
    /* Warna teks untuk paragraf dan elemen lain */
    p, span, li, td, th {
        color: #cccccc !important;
    }
    
    /* Teks tebal */
    strong {
        color: #ffffff !important;
    }
    
    /* Tautan dengan warna neon */
    a {
        color: #00ffff !important;
        text-decoration: none;
    }
    
    a:hover {
        color: #66ffff !important;
        text-decoration: underline;
    }
    
    /* Sidebar background hitam */
    .css-1d391kg, .css-12oz5g7 {
        background-color: #000000 !important;
    }
    
    /* Input teks dengan tema gelap */
    .stTextInput > div > div > input {
        background-color: #1a1a1a;
        color: #ffffff;
        border: 1px solid #444444;
    }
    
    /* Dropdown dengan tema gelap */
    .stSelectbox > div > div > select {
        background-color: #1a1a1a;
        color: #ffffff;
        border: 1px solid #444444;
    }
    
    /* Garis pembatas */
    hr {
        border-color: #333333 !important;
    }
</style>
""", unsafe_allow_html=True)

# ================= HEADER PROFIL DENGAN FOTO =================
col1, col2 = st.columns([1, 2])

with col1:
    with col1:
    st.image(
        "https://raw.githubusercontent.com/ReginaRiaAurellia/portfolio/main/foto.jpg",
        width=200
    )
    # Informasi kontak cepat
    st.markdown("""
    <div style="text-align:center; margin-top:20px;">
        <p style="color:#00ffff; font-weight:600;">📧 aurelliaria10@gmail.com</p>
        <p style="color:#00ffff; font-weight:600;">📱 081 225 805 910</p>
        <p style="color:#888888;">📍 Salatiga, Jawa Tengah, Indonesia</p>
    </div>
    """, unsafe_allow_html=True)

# Container untuk styling
with st.container():
    st.markdown("### Profil Singkat")
    col1, col2 = st.columns([3, 1])


# Container untuk styling
with st.container():
    st.markdown("### Teller Berpengalaman - Data Analyis")
    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.write("""
        Lulusan **S1 Pendidikan Matematika Cum Laude** dengan pengalaman 
        **3 tahun sebagai Teller di BCA**. Menggabungkan kemampuan analitis 
        matematika dengan pengalaman praktis perbankan.
        """)
    
    with col2:
        # Badge menggunakan HTML dengan styling
        st.markdown("""
        <div style="display: flex; flex-direction: column; gap: 10px; margin-top: 25px;">
            <div style="background: linear-gradient(135deg, #00ff88 0%, #00cc66 100%); color: black; padding: 8px 15px; border-radius: 20px; font-weight: 600; border: 1px solid rgba(255,255,255,0.1); text-align: center;">
                🎓 Cum Laude
            </div>
            <div style="background: linear-gradient(135deg, #00ffff 0%, #0088ff 100%); color: black; padding: 8px 15px; border-radius: 20px; font-weight: 600; border: 1px solid rgba(255,255,255,0.1); text-align: center;">
                🏦 Pengalaman BCA
            </div>
            <div style="background: linear-gradient(135deg, #ff00ff 0%, #cc00cc 100%); color: white; padding: 8px 15px; border-radius: 20px; font-weight: 600; border: 1px solid rgba(255,255,255,0.1); text-align: center;">
                📊 Analisis Data
            </div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ================= METRIK KINERJA UTAMA =================
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

# ================= DASHBOARD ANALISIS TRANSAKSI =================
st.markdown('<h2 class="section-header">💰 Dashboard Analisis Transaksi</h2>', unsafe_allow_html=True)

# Membuat data transaksi contoh
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
        <h4 style="color: #ffffff;">📈 Tren Volume Transaksi 30 Hari Terakhir</h4>
    """, unsafe_allow_html=True)
    st.line_chart(data.set_index('Tanggal')['Transaksi'], height=300)
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    # Statistik ringkasan bulanan
    st.markdown("""
    <div class="card">
        <h4 style="color: #ffffff;">📊 Ringkasan Performa Bulanan</h4>
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
            <div style="display: flex; justify-content: space-between; margin: 10px 0;">
                <span style="color: #cccccc;">Akurasi:</span>
                <strong style="color: #00ff88;">99.8%</strong>
            </div>
        </div>
    </div>
    """.format(
        data['Transaksi'].sum(),
        data['Transaksi'].mean(),
        data['Aliran Kas (Juta Rp)'].sum() / 1000,
        data['Kepuasan Nasabah'].mean()
    ), unsafe_allow_html=True)

# ================= GARIS WAKTU KARIR =================
st.markdown('<h2 class="section-header">🎓 Garis Waktu Perjalanan Karir</h2>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card">
        <h4 style="color: #ffffff; display: flex; align-items: center; gap: 10px;">
            <div style="background: #00ff88; color: black; width: 40px; height: 40px; border-radius: 50%; display: flex; align-items: center; justify-content: center;">🎓</div>
            Latar Belakang Pendidikan
        </h4>
        <div class="timeline-item">
            <strong>S1 Pendidikan Matematika</strong><br>
            <em style="color: #888888;">Universitas Kristen Satya Wacana, Salatiga</em><br>
            <small style="color: #666666;">2017 - 2021 • IPK 3.85 • Cum Laude</small>
            <p style="color: #aaaaaa; font-size: 0.9rem; margin-top: 5px;">
            Fokus pada statistika, aljabar, dan analisis data. Aktif dalam organisasi mahasiswa.
            </p>
        </div>
        <div class="timeline-item">
            <strong>SMA Negeri 2 Salatiga</strong><br>
            <em style="color: #888888;">Jurusan Matematika dan Ilmu Pengetahuan Alam</em><br>
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
            <strong>Teller - Bank Central Asia (BCA)</strong><br>
            <em style="color: #888888;">Kantor Cabang Singosaren, Solo</em><br>
            <small style="color: #666666;">Maret 2022 - Maret 2025 • 3 Tahun</small>
            <ul style="margin: 10px 0 0 20px; color: #cccccc;">
                <li>Menangani 180-200 transaksi harian dengan akurasi 99.8%</li>
                <li>PIC (Person In Charge) Proyek Kaizen untuk efisiensi proses</li>
                <li>Mentor dan pelatih untuk 3 teller baru</li>
                <li>Penanganan kas harian hingga Rp 1 Miliar tanpa selisih</li>
                <li>Nilai kepuasan nasabah konsisten 4.9/5.0</li>
            </ul>
        </div>
        <div class="timeline-item">
            <strong>Magang Operasional Bank</strong><br>
            <em style="color: #888888;">Bank Jateng, Salatiga</em><br>
            <small style="color: #666666;">Juni - Agustus 2021 • 3 Bulan</small>
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
            <strong>Tutor Matematika</strong><br>
            <em style="color: #888888;">Privat & Bimbingan Belajar</em><br>
            <small style="color: #666666;">2021 - 2025 • Paruh Waktu</small>
            <p style="color: #aaaaaa; font-size: 0.9rem; margin-top: 5px;">
            Mengajar matematika, untuk siswa SD, SMP dan SMA.
            </p>
        </div>
        <div class="timeline-item">
            <strong>Master Teacher Matematika</strong><br>
            <em style="color: #888888;">Ruang Guru - Platform Edukasi Online</em><br>
            <small style="color: #666666;">Januari - Desember 2021</small>
        </div>
        <div class="timeline-item">
            <strong>Asisten Penelitian Statistika</strong><br>
            <em style="color: #888888;">Fakultas Matematika UKSW</em><br>
            <small style="color: #666666;">2020 - 2021</small>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ================= KE AHLIAN DAN KOMPETENSI =================
st.markdown('<h2 class="section-header">🛠 Keahlian & Kompetensi</h2>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card">
        <h4 style="color: #ffffff;">💻 Keahlian Teknis & Digital</h4>
        <div style="margin-top: 15px;">
            <div style="display: flex; justify-content: space-between; margin: 12px 0;">
                <span style="color: #cccccc;">Python untuk Analisis Data</span>
                <div style="display: flex; gap: 3px;">
                    <div style="width: 12px; height: 12px; background: #00ff88; border-radius: 2px;"></div>
                    <div style="width: 12px; height: 12px; background: #00ff88; border-radius: 2px;"></div>
                    <div style="width: 12px; height: 12px; background: #00ff88; border-radius: 2px;"></div>
                    <div style="width: 12px; height: 12px; background: #00ff88; border-radius: 2px;"></div>
                    <div style="width: 12px; height: 12px; background: #333333; border-radius: 2px;"></div>
                </div>
            </div>
            <div style="display: flex; justify-content: space-between; margin: 12px 0;">
                <span style="color: #cccccc;">Microsoft Excel (Analisis Data)</span>
                <div style="display: flex; gap: 3px;">
                    <div style="width: 12px; height: 12px; background: #00ffff; border-radius: 2px;"></div>
                    <div style="width: 12px; height: 12px; background: #00ffff; border-radius: 2px;"></div>
                    <div style="width: 12px; height: 12px; background: #00ffff; border-radius: 2px;"></div>
                    <div style="width: 12px; height: 12px; background: #00ffff; border-radius: 2px;"></div>
                    <div style="width: 12px; height: 12px; background: #00ffff; border-radius: 2px;"></div>
                </div>
            </div>
            <div style="display: flex; justify-content: space-between; margin: 12px 0;">
                <span style="color: #cccccc;">SQL & Manajemen Database</span>
                <div style="display: flex; gap: 3px;">
                    <div style="width: 12px; height: 12px; background: #ff00ff; border-radius: 2px;"></div>
                    <div style="width: 12px; height: 12px; background: #ff00ff; border-radius: 2px;"></div>
                    <div style="width: 12px; height: 12px; background: #ff00ff; border-radius: 2px;"></div>
                    <div style="width: 12px; height: 12px; background: #333333; border-radius: 2px;"></div>
                    <div style="width: 12px; height: 12px; background: #333333; border-radius: 2px;"></div>
                </div>
            </div>
            <div style="display: flex; justify-content: space-between; margin: 12px 0;">
                <span style="color: #cccccc;">Streamlit (Dashboard Web)</span>
                <div style="display: flex; gap: 3px;">
                    <div style="width: 12px; height: 12px; background: #00ff88; border-radius: 2px;"></div>
                    <div style="width: 12px; height: 12px; background: #00ff88; border-radius: 2px;"></div>
                    <div style="width: 12px; height: 12px; background: #00ff88; border-radius: 2px;"></div>
                    <div style="width: 12px; height: 12px; background: #333333; border-radius: 2px;"></div>
                    <div style="width: 12px; height: 12px; background: #333333; border-radius: 2px;"></div>
                </div>
            </div>
            <div style="display: flex; justify-content: space-between; margin: 12px 0;">
                <span style="color: #cccccc;">Teller Bank</span>
                <div style="display: flex; gap: 3px;">
                    <div style="width: 12px; height: 12px; background: #00ffff; border-radius: 2px;"></div>
                    <div style="width: 12px; height: 12px; background: #00ffff; border-radius: 2px;"></div>
                    <div style="width: 12px; height: 12px; background: #00ffff; border-radius: 2px;"></div>
                    <div style="width: 12px; height: 12px; background: #00ffff; border-radius: 2px;"></div>
                    <div style="width: 12px; height: 12px; background: #00ffff; border-radius: 2px;"></div>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <h4 style="color: #ffffff;">🏦 Keahlian Perbankan & Operasional</h4>
        <div style="margin-top: 15px;">
            <div style="background: rgba(0, 0, 0, 0.5); padding: 12px 15px; border-radius: 8px; margin: 10px 0; border: 1px solid #333333; display: flex; align-items: center; gap: 10px;">
                <div style="color: #00ffff;">💰</div>
                <span>Penanganan & Rekonsiliasi Kas</span>
            </div>
            <div style="background: rgba(0, 0, 0, 0.5); padding: 12px 15px; border-radius: 8px; margin: 10px 0; border: 1px solid #333333; display: flex; align-items: center; gap: 10px;">
                <div style="color: #00ff88;">👥</div>
                <span>Layanan Nasabah & Relationship</span>
            </div>
            <div style="background: rgba(0, 0, 0, 0.5); padding: 12px 15px; border-radius: 8px; margin: 10px 0; border: 1px solid #333333; display: flex; align-items: center; gap: 10px;">
                <div style="color: #ff00ff;">⚠️</div>
                <span>Manajemen Risiko & Pencegahan Fraud</span>
            </div>
            <div style="background: rgba(0, 0, 0, 0.5); padding: 12px 15px; border-radius: 8px; margin: 10px 0; border: 1px solid #333333; display: flex; align-items: center; gap: 10px;">
                <div style="color: #ffaa00;">📋</div>
                <span>Kepatuhan Regulasi & SOP Bank</span>
            </div>
            <div style="background: rgba(0, 0, 0, 0.5); padding: 12px 15px; border-radius: 8px; margin: 10px 0; border: 1px solid #333333; display: flex; align-items: center; gap: 10px;">
                <div style="color: #00ffff;">📊</div>
                <span>Pelaporan & Analisis Transaksi</span>
            </div>
            <div style="background: rgba(0, 0, 0, 0.5); padding: 12px 15px; border-radius: 8px; margin: 10px 0; border: 1px solid #333333; display: flex; align-items: center; gap: 10px;">
                <div style="color: #00ff88;">🔄</div>
                <span>Proses Back Office Banking</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
        <h4 style="color: #ffffff;">🌟 Soft Skills & Kompetensi Personal</h4>
        <div style="margin-top: 15px;">
            <div style="display: flex; align-items: center; gap: 10px; margin: 12px 0; padding: 10px; background: rgba(0, 0, 0, 0.3); border-radius: 8px;">
                <div style="color: #00ff88; font-size: 1.5rem;">✓</div>
                <div>
                    <span style="color: #ffffff; font-weight: 600;">Detil dan Akurat</span><br>
                    <small style="color: #888888;">Akurasi transaksi 99.8%, rekonsiliasi sempurna</small>
                </div>
            </div>
            <div style="display: flex; align-items: center; gap: 10px; margin: 12px 0; padding: 10px; background: rgba(0, 0, 0, 0.3); border-radius: 8px;">
                <div style="color: #00ffff; font-size: 1.5rem;">✓</div>
                <div>
                    <span style="color: #ffffff; font-weight: 600;">Kepemimpinan & Mentoring</span><br>
                    <small style="color: #888888;">Memimpin proyek Kaizen, mentor 3 teller baru</small>
                </div>
            </div>
            <div style="display: flex; align-items: center; gap: 10px; margin: 12px 0; padding: 10px; background: rgba(0, 0, 0, 0.3); border-radius: 8px;">
                <div style="color: #ff00ff; font-size: 1.5rem;">✓</div>
                <div>
                    <span style="color: #ffffff; font-weight: 600;">Pemecahan Masalah Analitis</span><br>
                    <small style="color: #888888;">Pendekatan matematis untuk solusi operasional</small>
                </div>
            </div>
            <div style="display: flex; align-items: center; gap: 10px; margin: 12px 0; padding: 10px; background: rgba(0, 0, 0, 0.3); border-radius: 8px;">
                <div style="color: #ffaa00; font-size: 1.5rem;">✓</div>
                <div>
                    <span style="color: #ffffff; font-weight: 600;">Komunikasi Efektif</span><br>
                    <small style="color: #888888;">Nilai kepuasan nasabah 4.7/5.0</small>
                </div>
            </div>
            <div style="display: flex; align-items: center; gap: 10px; margin: 12px 0; padding: 10px; background: rgba(0, 0, 0, 0.3); border-radius: 8px;">
                <div style="color: #00ff88; font-size: 1.5rem;">✓</div>
                <div>
                    <span style="color: #ffffff; font-weight: 600;">Manajemen Waktu</span><br>
                    <small style="color: #888888;">Menangani 200+ transaksi harian secara efisien</small>
                </div>
            </div>
            <div style="display: flex; align-items: center; gap: 10px; margin: 12px 0; padding: 10px; background: rgba(0, 0, 0, 0.3); border-radius: 8px;">
                <div style="color: #00ffff; font-size: 1.5rem;">✓</div>
                <div>
                    <span style="color: #ffffff; font-weight: 600;">Adaptabilitas</span><br>
                    <small style="color: #888888;">Berhasil transisi dari pendidikan ke perbankan</small>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ================= SERTIFIKASI & PENCAPAIAN =================
st.markdown('<h2 class="section-header">🏆 Sertifikasi & Pencapaian</h2>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card">
        <h4 style="color: #ffffff;">📜 Sertifikasi Perbankan</h4>
        <div style="margin-top: 15px;">
            <div style="background: rgba(0, 0, 0, 0.5); padding: 15px; border-radius: 8px; margin: 10px 0; border-left: 4px solid #00ff88;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <span style="color: #ffffff; font-weight: 600;">Sertifikasi Teller BCA</span>
                    <small style="color: #00ff88;">2022</small>
                </div>
                <small style="color: #888888;">Bank Central Asia • Kompetensi operasional teller</small>
            </div>
            <div style="background: rgba(0, 0, 0, 0.5); padding: 15px; border-radius: 8px; margin: 10px 0; border-left: 4px solid #00ffff;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <span style="color: #ffffff; font-weight: 600;">Anti Money Laundering (AML)</span>
                    <small style="color: #00ffff;">2023</small>
                </div>
                <small style="color: #888888;">Otoritas Jasa Keuangan • Pencegahan pencucian uang</small>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <h4 style="color: #ffffff;">🎓 Sertifikasi Teknis</h4>
        <div style="margin-top: 15px;">
            <div style="background: rgba(0, 0, 0, 0.5); padding: 15px; border-radius: 8px; margin: 10px 0; border-left: 4px solid #ff00ff;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <span style="color: #ffffff; font-weight: 600;">Python untuk Data Science</span>
                    <small style="color: #ff00ff;">2024</small>
                </div>
                <small style="color: #888888;">Coursera • University of Michigan</small>
            </div>
            <div style="background: rgba(0, 0, 0, 0.5); padding: 15px; border-radius: 8px; margin: 10px 0; border-left: 4px solid #ffaa00;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <span style="color: #ffffff; font-weight: 600;">Microsoft Excel: Analisis Data</span>
                    <small style="color: #ffaa00;">2023</small>
                </div>
                <small style="color: #888888;">LinkedIn Learning • Advanced Functions</small>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
        <h4 style="color: #ffffff;">⭐ Pencapaian & Penghargaan</h4>
        <div style="margin-top: 15px;">
            <div style="background: rgba(0, 0, 0, 0.5); padding: 15px; border-radius: 8px; margin: 10px 0; border-left: 4px solid #00ff88;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <span style="color: #ffffff; font-weight: 600;">Employee of the Month</span>
                    <small style="color: #00ff88;">Nov 2023</small>
                </div>
                <small style="color: #888888;">BCA Singosaren • Kinerja luar biasa</small>
            </div>
            <div style="background: rgba(0, 0, 0, 0.5); padding: 15px; border-radius: 8px; margin: 10px 0; border-left: 4px solid #00ffff;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <span style="color: #ffffff; font-weight: 600;">Kaizen Project Award</span>
                    <small style="color: #00ffff;">2024</small>
                </div>
                <small style="color: #888888;">BCA Regional • Inovasi proses teller</small>
            </div>
            <div style="background: rgba(0, 0, 0, 0.5); padding: 15px; border-radius: 8px; margin: 10px 0; border-left: 4px solid #ff00ff;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <span style="color: #ffffff; font-weight: 600;">Cum Laude</span>
                    <small style="color: #ff00ff;">2021</small>
                </div>
                <small style="color: #888888;">UKSW • IPK 3.85/4.00</small>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ================= PROYEK & KONTRIBUSI =================
st.markdown('<h2 class="section-header">🚀 Proyek & Kontribusi</h2>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="card">
        <h4 style="color: #ffffff;">💡 Proyek Kaizen BCA</h4>
        <p style="color: #cccccc; margin: 10px 0;">
        <strong>PIC Proyek Peningkatan Efisiensi Proses Teller</strong><br>
        Maret 2024 - Juni 2024
        </p>
        <ul style="color: #cccccc; margin-left: 20px;">
            <li>Mengurangi waktu proses transaksi rata-rata 15%</li>
            <li>Mengotomatisasi laporan harian dengan Excel macro</li>
            <li>Mengimplementasikan checklist visual untuk akurasi</li>
            <li>Menerima penghargaan regional untuk inovasi</li>
        </ul>
        <div style="display: flex; gap: 10px; margin-top: 15px;">
            <div style="background: rgba(0, 255, 136, 0.2); color: #00ff88; padding: 5px 10px; border-radius: 15px; font-size: 0.8rem;">
                Process Improvement
            </div>
            <div style="background: rgba(0, 255, 255, 0.2); color: #00ffff; padding: 5px 10px; border-radius: 15px; font-size: 0.8rem;">
                Excel Automation
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <h4 style="color: #ffffff;">📊 Analisis Data Transaksi</h4>
        <p style="color: #cccccc; margin: 10px 0;">
        <strong>Dashboard Monitoring Kinerja Teller</strong><br>
        Januari 2024 - Sekarang
        </p>
        <ul style="color: #cccccc; margin-left: 20px;">
            <li>Mengembangkan dashboard Streamlit untuk analisis transaksi</li>
            <li>Mengidentifikasi pola transaksi puncak untuk staffing optimal</li>
            <li>Membuat sistem alert untuk anomali transaksi</li>
            <li>Mengurangi kesalahan input data sebesar 25%</li>
        </ul>
        <div style="display: flex; gap: 10px; margin-top: 15px;">
            <div style="background: rgba(255, 0, 255, 0.2); color: #ff00ff; padding: 5px 10px; border-radius: 15px; font-size: 0.8rem;">
                Python
            </div>
            <div style="background: rgba(0, 255, 255, 0.2); color: #00ffff; padding: 5px 10px; border-radius: 15px; font-size: 0.8rem;">
                Streamlit
            </div>
            <div style="background: rgba(255, 170, 0, 0.2); color: #ffaa00; padding: 5px 10px; border-radius: 15px; font-size: 0.8rem;">
                Data Analysis
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ================= FOOTER & KONTAK =================
# Simple footer tanpa HTML kompleks
st.markdown("---")
st.header("🤝 Mari Berkolaborasi!")
st.write("""
Saya terbuka untuk peluang karir dalam perbankan digital, analisis data perbankan, 
atau peran yang menggabungkan keahlian teknis dengan pengalaman operasional perbankan.
""")

# Tombol menggunakan st.columns
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("📧 Email Saya", use_container_width=True):
        st.write("Email: aurelliarial0@gmail.com")
with col2:
    if st.button("💬 WhatsApp", use_container_width=True):
        st.write("WA: 0812 2580 5910")
with col3:
    if st.button("💻 GitHub", use_container_width=True):
        st.write("GitHub: ReginaRiaAurellia")

st.markdown("---")
st.caption("© 2024 Regina Ria Aurellia • Portfolio Digital")
st.caption("Terakhir diperbarui: Desember 2024 • Tersedia untuk wawancara")

# ================= SIDEBAR =================
with st.sidebar:
    # Logo dan navigasi
    st.markdown("""
    <div style="text-align: center; margin-bottom: 30px;">
        <div style="font-size: 2rem; color: #00ffff; margin-bottom: 10px;">🏦</div>
        <h3 style="color: #ffffff; margin-bottom: 5px;">Regina Ria</h3>
        <p style="color: #888888; font-size: 0.9rem;">Portfolio Digital</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Menu navigasi
    st.markdown("""
    <div class="card" style="margin-bottom: 20px;">
        <h4 style="color: #ffffff; margin-bottom: 15px;">🔍 Navigasi Cepat</h4>
        <div style="display: flex; flex-direction: column; gap: 10px;">
            <a href="#header" style="text-decoration: none;">
                <div style="color: #cccccc; padding: 12px; border-radius: 8px; background: rgba(0, 0, 0, 0.5); text-align: center; border: 1px solid #333333; transition: all 0.3s;">
                    👤 Profil & Kontak
                </div>
            </a>
            <a href="#performance" style="text-decoration: none;">
                <div style="color: #cccccc; padding: 12px; border-radius: 8px; background: rgba(0, 0, 0, 0.5); text-align: center; border: 1px solid #333333; transition: all 0.3s;">
                    📊 Kinerja & Metrik
                </div>
            </a>
            <a href="#timeline" style="text-decoration: none;">
                <div style="color: #cccccc; padding: 12px; border-radius: 8px; background: rgba(0, 0, 0, 0.5); text-align: center; border: 1px solid #333333; transition: all 0.3s;">
                    🎓 Garis Waktu Karir
                </div>
            </a>
            <a href="#skills" style="text-decoration: none;">
                <div style="color: #cccccc; padding: 12px; border-radius: 8px; background: rgba(0, 0, 0, 0.5); text-align: center; border: 1px solid #333333; transition: all 0.3s;">
                    🛠 Keahlian & Kompetensi
                </div>
            </a>
            <a href="#projects" style="text-decoration: none;">
                <div style="color: #cccccc; padding: 12px; border-radius: 8px; background: rgba(0, 0, 0, 0.5); text-align: center; border: 1px solid #333333; transition: all 0.3s;">
                    🚀 Proyek & Kontribusi
                </div>
            </a>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Tombol unduh CV
    col1, col2 = st.columns(2)
    with col1:
        if st.button("📄 Unduh CV", use_container_width=True):
            st.success("CV akan segera diunduh!")
    with col2:
        if st.button("📧 Hubungi", use_container_width=True):
            st.info("Membuka aplikasi email...")
    
    # Informasi ketersediaan
    st.markdown("""
    <div class="card">
        <h4 style="color: #ffffff; margin-bottom: 10px;">📅 Ketersediaan</h4>
        <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 10px;">
            <div style="color: #00ff88; font-size: 1.2rem;">●</div>
            <span style="color: #cccccc;">Tersedia untuk kerja</span>
        </div>
        <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 10px;">
            <div style="color: #00ffff; font-size: 1.2rem;">📍</div>
            <span style="color: #cccccc;">Salatiga / Remote</span>
        </div>
        <div style="display: flex; align-items: center; gap: 10px;">
            <div style="color: #ffaa00; font-size: 1.2rem;">🕒</div>
            <span style="color: #cccccc;">Wawancara: Fleksibel</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Bahasa yang dikuasai
    st.markdown("""
    <div class="card">
        <h4 style="color: #ffffff; margin-bottom: 10px;">🗣️ Bahasa</h4>
        <div style="display: flex; justify-content: space-between; margin: 8px 0;">
            <span style="color: #cccccc;">Bahasa Indonesia</span>
            <span style="color: #00ffff;">Native</span>
        </div>
        <div style="display: flex; justify-content: space-between; margin: 8px 0;">
            <span style="color: #cccccc;">Bahasa Inggris</span>
            <span style="color: #00ff88;">Profesional</span>
        </div>
        <div style="display: flex; justify-content: space-between; margin: 8px 0;">
            <span style="color: #cccccc;">Bahasa Jawa</span>
            <span style="color: #ffaa00;">Pemahaman</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Statistik pengunjung (simulasi)
    st.markdown("""
    <div class="card">
        <h4 style="color: #ffffff; margin-bottom: 10px;">📈 Statistik</h4>
        <div style="text-align: center;">
            <div style="font-size: 2rem; color: #00ffff; font-weight: 700;">1,247</div>
            <div style="color: #888888; font-size: 0.9rem;">Pengunjung Portfolio</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ================= FUNGSI TAMBAHAN =================
# Menambahkan timestamp
st.sidebar.markdown("""
<div style="color: #666666; font-size: 0.7rem; text-align: center; margin-top: 20px;">
    Dibuat dengan ❤️ menggunakan Streamlit<br>
    Diakses: {}
</div>
""".format(datetime.now().strftime("%d %B %Y, %H:%M")), unsafe_allow_html=True)
