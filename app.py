"""
🏦 REGINA RIA - BANKING PORTFOLIO DASHBOARD
All-in-One Working App
"""

import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="Regina Ria Portfolio",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ================= HEADER =================
st.title("🏦 Regina Ria Aurellia")
st.markdown("""
**S1 Pendidikan Matematika Cum Laude | BCA Teller (Maret 2022 – Maret 2025)**  
*Menggabungkan ketelitian matematika dengan pengalaman perbankan untuk analisis data finansial*
""")

# ================= SIDEBAR =================
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2784/2784459.png", width=100)
    
    st.header("🎯 Pencapaian di BCA")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Akurasi", "99.8%", "+1.8%")
    with col2:
        st.metric("Kepuasan", "4.7/5.0", "+0.4")
    
    st.info("""
    **🏆 Highlights:**
    • Transaksi: 180-200/hari
    • Cash Handling: Rp 1M/hari
    • PIC Kaizen Project
    • Mentor 3 teller baru
    """)
    
    st.divider()
    st.caption("📧 aurelliarial0@gmail.com")
    st.caption("📱 081 225 805 910")
    st.caption("📍 Salatiga, Jawa Tengah")

# ================= MAIN DASHBOARD =================

# Row 1: Key Metrics
st.subheader("📊 Performance Dashboard")

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Total Transaksi", "15,420", "1,240")
with col2:
    st.metric("Total Nilai", "Rp 24.5B", "Rp 3.2B")
with col3:
    st.metric("Error Rate", "0.18%", "-0.32%")
with col4:
    st.metric("Resolusi Komplain", "100%", "5%")

# Row 2: Sample Data
st.subheader("📈 Transaction Analysis")

# Generate sample data
@st.cache_data
def generate_transaction_data():
    dates = pd.date_range('2024-01-01', periods=30, freq='D')
    data = pd.DataFrame({
        'Tanggal': dates,
        'Jumlah_Transaksi': np.random.randint(150, 220, 30),
        'Nilai_Juta_Rp': np.random.randint(500, 1200, 30),
        'Kepuasan': np.round(np.random.uniform(4.3, 5.0, 30), 2),
        'Kesalahan': np.random.randint(0, 2, 30)
    })
    return data

df = generate_transaction_data()

# Display data
col1, col2 = st.columns([2, 1])

with col1:
    st.line_chart(df.set_index('Tanggal')['Jumlah_Transaksi'])
    st.caption("Trend Volume Transaksi Harian")

with col2:
    st.dataframe(df.tail(5))
    if st.button("📥 Download Sample Data"):
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Download CSV",
            data=csv,
            file_name="bca_transaction_sample.csv",
            mime="text/csv"
        )

# Row 3: Projects
st.subheader("🚀 Portfolio Projects")

tab1, tab2, tab3 = st.tabs(["Banking Analytics", "Financial Tools", "Case Studies"])

with tab1:
    st.markdown("""
    ### 📊 **Banking Analytics Dashboard**
    **Tech:** Python, Streamlit, Pandas
    
    **Fitur:**
    ✅ Analisis transaksi real-time  
    ✅ Optimasi cash flow teller  
    ✅ Customer segmentation  
    ✅ Automated reporting  
    
    *Berdasarkan pengalaman nyata di BCA counter*
    """)
    
    if st.button("View Code Snippet", key="code1"):
        st.code("""
        # Transaction accuracy calculation
        def calculate_accuracy(transactions):
            successful = sum(1 for t in transactions if t['status'] == 'success')
            total = len(transactions)
            return (successful / total) * 100
        
        # BCA Performance: 99.8% accuracy
        """, language="python")

with tab2:
    st.markdown("""
    ### 🧮 **Financial Calculator Suite**
    **Tech:** Python, NumPy
    
    **Tools:**
    • Deposit Interest Calculator  
    • Loan EMI Calculator  
    • Currency Converter  
    • Investment Planner  
    
    *Mengaplikasikan matematika keuangan praktis*
    """)
    
    # Simple calculator
    st.write("**Kalkulator Bunga Deposito:**")
    col_a, col_b, col_c = st.columns(3)
    with col_a:
        principal = st.number_input("Principal (Rp)", value=10000000, step=1000000)
    with col_b:
        rate = st.slider("Annual Rate (%)", 1.0, 10.0, 5.0)
    with col_c:
        months = st.selectbox("Tenor", [1, 3, 6, 12])
    
    interest = principal * (rate/100) * (months/12)
    st.metric("Bunga (Sebelum Pajak)", f"Rp {interest:,.0f}")

with tab3:
    st.markdown("""
    ### 🏆 **BCA Case Studies**
    
    **1. Kaizen Project - Efisiensi Antrian**
    • Problem: Waktu tunggu nasabah 15+ menit  
    • Solution: Implementasi sistem antrian digital  
    • Result: -30% waktu tunggu
    
    **2. Cash Optimization**
    • Problem: Sering kehabisan pecahan kecil  
    • Solution: Predictive cash ordering system  
    • Result: 0% stockout dalam 6 bulan
    
    **3. Customer Complaint Resolution**
    • Problem: Komplain transfer gagal  
    • Solution: SOP eskalsi cepat + komunikasi proaktif  
    • Result: 100% resolusi dalam 24 jam
    """)

# Row 4: Skills
st.subheader("🛠 Skills & Expertise")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("**💻 Technical:**")
    st.write("• Python (Pandas, NumPy)")
    st.write("• Data Analysis")
    st.write("• Streamlit Dashboard")
    st.write("• Microsoft Excel")

with col2:
    st.markdown("**🏦 Banking:**")
    st.write("• Cash Handling & Processing")
    st.write("• Customer Service Excellence")
    st.write("• Risk Management")
    st.write("• Compliance & SOP")

with col3:
    st.markdown("**🌟 Soft Skills:**")
    st.write("• Detail-Oriented (99.8% accuracy)")
    st.write("• Team Leadership")
    st.write("• Problem Solving")
    st.write("• Communication")

# Footer
st.divider()
st.markdown("""
<div style='text-align: center'>
    <p><strong>GitHub:</strong> <a href='https://github.com/ReginaRiaAurellia'>github.com/ReginaRiaAurellia</a></p>
    <p><em>"From counting cash to analyzing data – Transforming banking with mathematics & technology"</em></p>
    <p>📅 Last Updated: April 2024</p>
</div>
""", unsafe_allow_html=True)
