import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# ================= KONFIGURASI HALAMAN =================
st.set_page_config(
    page_title="Regina Ria Aurellia - Portfolio",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ================= TEMA HITAM CSS =================
st.markdown("""
<style>
    .stApp {
        background: #000000;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    /* Judul utama */
    .main-title {
        color: #FFFFFF;
        font-size: 2.8rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }
    
    .subtitle {
        color: #00FFFF;
        font-size: 1.5rem;
        font-weight: 600;
        margin-bottom: 1.5rem;
    }
    
    /* Card styling */
    .profile-card {
        background: rgba(25, 25, 25, 0.95);
        border-radius: 20px;
        padding: 30px;
        margin: 20px 0;
        border-left: 5px solid #00FFFF;
        box-shadow: 0 8px 32px rgba(0, 255, 255, 0.1);
    }
    
    .metric-card {
        background: linear-gradient(135deg, #1a1a1a 0%, #2d2d2d 100%);
        border-radius: 15px;
        padding: 25px 15px;
        text-align: center;
        border: 1px solid #333;
    }
    
    /* Badge styling */
    .badge {
        display: inline-block;
        padding: 10px 20px;
        border-radius: 25px;
        font-weight: 600;
        margin: 5px 10px 5px 0;
        font-size: 0.9rem;
    }
    
    .badge-green {
        background: linear-gradient(135deg, #00FF88, #00CC66);
        color: #000;
    }
    
    .badge-blue {
        background: linear-gradient(135deg, #00FFFF, #0088FF);
        color: #000;
    }
    
    .badge-purple {
        background: linear-gradient(135deg, #FF00FF, #CC00CC);
        color: #FFF;
    }
    
    /* Text styling */
    .description-text {
        color: #CCCCCC;
        font-size: 1.1rem;
        line-height: 1.7;
        margin-bottom: 1.5rem;
    }
    
    .highlight {
        color: #FFFFFF;
        font-weight: 700;
    }
    
    /* Section headers */
    .section-header {
        color: #FFFFFF;
        font-size: 1.8rem;
        font-weight: 600;
        margin: 2rem 0 1.5rem 0;
        padding-bottom: 0.5rem;
        border-bottom: 2px solid #00FFFF;
    }
    
    /* Timeline */
    .timeline-item {
        padding: 1.2rem;
        margin: 1rem 0;
        background: rgba(40, 40, 40, 0.7);
        border-radius: 10px;
        border-left: 4px solid #00FFFF;
    }
    
    /* Skills bars */
    .skill-container {
        margin: 1rem 0;
    }
    
    .skill-name {
        color: #CCCCCC;
        margin-bottom: 0.3rem;
        display: flex;
        justify-content: space-between;
    }
    
    .skill-bar {
        height: 8px;
        background: #333;
        border-radius: 4px;
        overflow: hidden;
    }
    
    .skill-level {
        height: 100%;
        border-radius: 4px;
    }
    
    /* Contact buttons */
    .contact-btn {
        display: inline-block;
        padding: 12px 25px;
        border-radius: 25px;
        font-weight: 600;
        text-decoration: none;
        margin: 5px;
        transition: transform 0.3s;
    }
    
    .contact-btn:hover {
        transform: translateY(-2px);
    }
    
    .btn-email {
        background: linear-gradient(135deg, #00FFFF, #0088FF);
        color: #000;
    }
    
    .btn-whatsapp {
        background: linear-gradient(135deg, #00FF88, #00CC66);
        color: #000;
    }
    
    .btn-github {
        background: linear-gradient(135deg, #333, #000);
        color: #FFF;
    }
</style>
""", unsafe_allow_html=True)

# ================= HEADER & PROFIL =================
st.markdown('<div class="main-title">🏦 Regina Ria Aurellia</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Professional Perbankan | Peminat Data</div>', unsafe_allow_html=True)

st.markdown("""
<div class="profile-card">
    <p class="description-text">
    Lulusan <span class="highlight">S1 Pendidikan Matematika Cum Laude</span> dengan pengalaman 
    <span class="highlight">3 tahun sebagai Teller di BCA</span>. Menggabungkan kemampuan analitis 
    matematika dengan pengalaman praktis perbankan untuk menciptakan solusi berbasis data 
    yang efektif dan efisien dalam operasional perbankan modern.
    </p>
    
    <div style="margin-top: 25px;">
        <span class="badge badge-green">🎓 Cum Laude</span>
        <span class="badge badge-blue">🏦 Pengalaman BCA</span>
        <span class="badge badge-purple">📊 Analisis Data</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ================= METRIK KINERJA =================
st.markdown('<div class="section-header">📊 Performance Highlights</div>', unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="metric-card">
        <div style="font-size: 2.5rem; color: #00FF88; font-weight: 700; margin-bottom: 0.5rem;">99.8%</div>
        <div style="color: #CCCCCC; font-size: 0.9rem; margin-bottom: 0.5rem;">AKURASI TRANSAKSI</div>
        <div style="color: #00FF88; font-size: 0.8rem;">+1.8% di atas target</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="metric-card">
        <div style="font-size: 2.5rem; color: #00FFFF; font-weight: 700; margin-bottom: 0.5rem;">4.7/5.0</div>
        <div style="color: #CCCCCC; font-size: 0.9rem; margin-bottom: 0.5rem;">KEPUASAN NASABAH</div>
        <div style="color: #00FFFF; font-size: 0.8rem;">+0.4 di atas target</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="metric-card">
        <div style="font-size: 2.5rem; color: #FF00FF; font-weight: 700; margin-bottom: 0.5rem;">180-200</div>
        <div style="color: #CCCCCC; font-size: 0.9rem; margin-bottom: 0.5rem;">TRANSAKSI HARIAN</div>
        <div style="color: #FF00FF; font-size: 0.8rem;">20% di atas rata-rata</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="metric-card">
        <div style="font-size: 2.5rem; color: #FFAA00; font-weight: 700; margin-bottom: 0.5rem;">Rp 1M</div>
        <div style="color: #CCCCCC; font-size: 0.9rem; margin-bottom: 0.5rem;">PENANGANAN KAS HARIAN</div>
        <div style="color: #FFAA00; font-size: 0.8rem;">0% perbedaan</div>
    </div>
    """, unsafe_allow_html=True)

# ================= PENDIDIKAN & PENGALAMAN =================
st.markdown('<div class="section-header">🎓 Pendidikan & Pengalaman</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="profile-card">
        <h3 style="color: #FFFFFF; margin-bottom: 1rem;">📚 Pendidikan</h3>
        
        <div class="timeline-item">
            <h4 style="color: #00FFFF; margin-bottom: 0.3rem;">S1 Pendidikan Matematika</h4>
            <p style="color: #888888; margin-bottom: 0.5rem;">Universitas Kristen Satya Wacana</p>
            <p style="color: #00FF88; font-size: 0.9rem;">2017 - 2021 • Cum Laude • IPK 3.85</p>
        </div>
        
        <div class="timeline-item">
            <h4 style="color: #00FFFF; margin-bottom: 0.3rem;">SMA Negeri 2 Salatiga</h4>
            <p style="color: #888888; margin-bottom: 0.5rem;">Jurusan Matematika dan Ilmu Pengetahuan Alam</p>
            <p style="color: #00FF88; font-size: 0.9rem;">2014 - 2017</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="profile-card">
        <h3 style="color: #FFFFFF; margin-bottom: 1rem;">💼 Pengalaman Kerja</h3>
        
        <div class="timeline-item">
            <h4 style="color: #00FFFF; margin-bottom: 0.3rem;">Teller - Bank Central Asia (BCA)</h4>
            <p style="color: #888888; margin-bottom: 0.5rem;">Kantor Cabang Singosaren, Solo</p>
            <p style="color: #00FF88; font-size: 0.9rem; margin-bottom: 0.8rem;">Maret 2022 - Maret 2025 (3 Tahun)</p>
            <ul style="color: #CCCCCC; padding-left: 20px;">
                <li>Akurasi transaksi 99.8%</li>
                <li>PIC Proyek Kaizen untuk efisiensi</li>
                <li>Mentor 3 teller baru</li>
                <li>Penanganan kas Rp 1M/hari</li>
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ================= KE AHLIAN TEKNIS =================
st.markdown('<div class="section-header">🛠 Keahlian Teknis</div>', unsafe_allow_html=True)

st.markdown("""
<div class="profile-card">
    <div class="skill-container">
        <div class="skill-name">
            <span>Python & Analisis Data</span>
            <span>80%</span>
        </div>
        <div class="skill-bar">
            <div class="skill-level" style="width: 80%; background: linear-gradient(90deg, #00FF88, #00CC66);"></div>
        </div>
    </div>
    
    <div class="skill-container">
        <div class="skill-name">
            <span>Microsoft Excel (Advanced)</span>
            <span>95%</span>
        </div>
        <div class="skill-bar">
            <div class="skill-level" style="width: 95%; background: linear-gradient(90deg, #00FFFF, #0088FF);"></div>
        </div>
    </div>
    
    <div class="skill-container">
        <div class="skill-name">
            <span>SQL & Database</span>
            <span>70%</span>
        </div>
        <div class="skill-bar">
            <div class="skill-level" style="width: 70%; background: linear-gradient(90deg, #FF00FF, #CC00CC);"></div>
        </div>
    </div>
    
    <div class="skill-container">
        <div class="skill-name">
            <span>Streamlit Dashboard</span>
            <span>75%</span>
        </div>
        <div class="skill-bar">
            <div class="skill-level" style="width: 75%; background: linear-gradient(90deg, #00FF88, #00CC66);"></div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ================= KE AHLIAN PERBANKAN =================
st.markdown('<div class="section-header">🏦 Keahlian Perbankan</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="metric-card" style="text-align: left; padding: 20px;">
        <div style="color: #00FFFF; font-size: 1.5rem; margin-bottom: 10px;">💰</div>
        <div style="color: #FFFFFF; font-weight: 600; margin-bottom: 5px;">Penanganan Kas</div>
        <div style="color: #CCCCCC; font-size: 0.9rem;">Rekonsiliasi & pemrosesan kas harian</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="metric-card" style="text-align: left; padding: 20px;">
        <div style="color: #00FF88; font-size: 1.5rem; margin-bottom: 10px;">👥</div>
        <div style="color: #FFFFFF; font-weight: 600; margin-bottom: 5px;">Layanan Nasabah</div>
        <div style="color: #CCCCCC; font-size: 0.9rem;">Kepuasan nasabah 4.7/5.0</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="metric-card" style="text-align: left; padding: 20px;">
        <div style="color: #FF00FF; font-size: 1.5rem; margin-bottom: 10px;">⚠️</div>
        <div style="color: #FFFFFF; font-weight: 600; margin-bottom: 5px;">Manajemen Risiko</div>
        <div style="color: #CCCCCC; font-size: 0.9rem;">Pencegahan fraud & compliance</div>
    </div>
    """, unsafe_allow_html=True)

# ================= KONTAK =================
st.markdown('<div class="section-header">📞 Hubungi Saya</div>', unsafe_allow_html=True)

st.markdown("""
<div class="profile-card" style="text-align: center;">
    <p class="description-text" style="text-align: center; margin-bottom: 2rem;">
    Tertarik berkolaborasi atau memiliki pertanyaan?<br>
    Jangan ragu untuk menghubungi saya melalui salah satu cara berikut:
    </p>
    
    <div style="display: flex; justify-content: center; flex-wrap: wrap; gap: 15px; margin-bottom: 2rem;">
        <a href="mailto:aurelliarial0@gmail.com" class="contact-btn btn-email">
            📧 Email
        </a>
        <a href="https://wa.me/6281225805910" class="contact-btn btn-whatsapp">
            💬 WhatsApp
        </a>
        <a href="https://github.com/ReginaRiaAurellia" class="contact-btn btn-github">
            💻 GitHub
        </a>
    </div>
    
    <div style="color: #888888; font-size: 0.9rem; margin-top: 2rem; padding-top: 1rem; border-top: 1px solid #333;">
        <p>📍 Salatiga, Jawa Tengah, Indonesia</p>
        <p>📱 0812 2580 5910</p>
        <p style="margin-top: 1rem; font-style: italic;">
        "Mentransformasi perbankan dengan matematika dan teknologi"
        </p>
    </div>
</div>
""", unsafe_allow_html=True)

# ================= SIDEBAR =================
with st.sidebar:
    st.markdown("""
    <div style="text-align: center; padding: 20px 0;">
        <div style="width: 120px; height: 120px; border-radius: 50%; overflow: hidden; margin: 0 auto 20px; border: 3px solid #00FFFF;">
            <img src="https://images.unsplash.com/photo-1580489944761-15a19d654956?ixlib=rb-4.0.3&auto=format&fit=crop&w=500&q=80" 
                 style="width:100%; height:100%; object-fit:cover;">
        </div>
        <h3 style="color: #FFFFFF; margin-bottom: 5px;">Regina Ria</h3>
        <p style="color: #00FFFF; margin-bottom: 20px;">Profesional Perbankan</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Informasi kontak sidebar
    st.markdown("""
    <div style="background: rgba(30, 30, 30, 0.8); padding: 20px; border-radius: 10px; margin-bottom: 20px;">
        <h4 style="color: #FFFFFF; margin-bottom: 15px;">📋 Informasi Kontak</h4>
        <div style="color: #CCCCCC; margin-bottom: 10px;">
            <strong>Email:</strong><br>
            aurelliarial0@gmail.com
        </div>
        <div style="color: #CCCCCC; margin-bottom: 10px;">
            <strong>Telepon:</strong><br>
            0812 2580 5910
        </div>
        <div style="color: #CCCCCC;">
            <strong>Lokasi:</strong><br>
            Salatiga, Jawa Tengah
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Tombol download CV
    if st.button("📄 Download CV Lengkap", use_container_width=True, type="primary"):
        st.success("CV akan segera diunduh!")
    
    # Status ketersediaan
    st.markdown("""
    <div style="background: rgba(30, 30, 30, 0.8); padding: 15px; border-radius: 10px; margin-top: 20px;">
        <div style="display: flex; align-items: center; margin-bottom: 10px;">
            <div style="width: 10px; height: 10px; background: #00FF88; border-radius: 50%; margin-right: 10px;"></div>
            <span style="color: #CCCCCC;">Tersedia untuk peluang baru</span>
        </div>
        <div style="display: flex; align-items: center;">
            <div style="width: 10px; height: 10px; background: #00FFFF; border-radius: 50%; margin-right: 10px;"></div>
            <span style="color: #CCCCCC;">Open to remote work</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ================= FOOTER =================
st.markdown("""
<div style="text-align: center; color: #666; margin-top: 3rem; padding-top: 1rem; border-top: 1px solid #333; font-size: 0.8rem;">
    <p>© 2024 Regina Ria Aurellia • Portfolio dibuat dengan Streamlit & Python</p>
    <p>Terakhir diperbarui: Desember 2024</p>
</div>
""", unsafe_allow_html=True)
