"""
SIMPLE BANKING DASHBOARD - NO MATPLOTLIB
By: Regina Ria Aurellia
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

# Set page config
st.set_page_config(
    page_title="Banking Portfolio - Regina",
    page_icon="🏦",
    layout="wide"
)

def main():
    # HEADER
    st.title("🏦 Regina Ria Aurellia - Banking Portfolio")
    st.markdown("**S1 Matematika Cum Laude | Former BCA Teller 2022-2025**")
    
    # SIDEBAR
    with st.sidebar:
        st.image("🏦", width=80)
        st.header("Tentang Saya")
        st.info("""
        **Latar Belakang:**
        - S1 Pendidikan Matematika (Cum Laude)
        - Teller BCA 2022-2025
        - Akurasi Transaksi: 99.8%
        - Kepuasan Nasabah: 4.7/5.0
        """)
        
        st.divider()
        st.caption("📍 Salatiga, Jawa Tengah")
        st.caption("📧 aurelliarial0@gmail.com")
        st.caption("📱 081 225 805 910")
    
    # METRICS
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Akurasi Transaksi", "99.8%", "+1.8%")
    with col2:
        st.metric("Transaksi/Hari", "187", "+12%")
    with col3:
        st.metric("Kepuasan Nasabah", "4.7/5.0", "+0.4")
    with col4:
        st.metric("Cash Handling", "Rp 1M/hari", "")
    
    # GENERATE SAMPLE DATA
    @st.cache_data
    def generate_data():
        dates = pd.date_range('2024-01-01', periods=30, freq='D')
        data = pd.DataFrame({
            'Tanggal': dates,
            'Transaksi': np.random.randint(120, 220, 30),
            'Nilai_Juta': np.random.randint(300, 1200, 30),
            'Kepuasan': np.round(np.random.uniform(4.0, 5.0, 30), 2)
        })
        return data
    
    df = generate_data()
    
    # CHARTS
    st.subheader("📈 Analisis Transaksi BCA")
    
    tab1, tab2, tab3 = st.tabs(["Volume Transaksi", "Aliran Kas", "Kepuasan Nasabah"])
    
    with tab1:
        fig1 = px.line(df, x='Tanggal', y='Transaksi', 
                      title='Volume Transaksi Harian')
        fig1.add_hline(y=150, line_dash="dash", line_color="red",
                      annotation_text="Target BCA: 150 transaksi")
        st.plotly_chart(fig1, use_container_width=True)
    
    with tab2:
        fig2 = px.bar(df, x='Tanggal', y='Nilai_Juta',
                     title='Nilai Tunai Harian (Juta Rp)')
        st.plotly_chart(fig2, use_container_width=True)
    
    with tab3:
        fig3 = px.area(df, x='Tanggal', y='Kepuasan',
                      title='Trend Kepuasan Nasabah')
        fig3.add_hline(y=4.0, line_dash="dash", line_color="orange",
                      annotation_text="Minimum Target: 4.0")
        st.plotly_chart(fig3, use_container_width=True)
    
    # DATA TABLE
    with st.expander("📋 Lihat Data Sample"):
        st.dataframe(df)
        
        # Download button
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            "📥 Download Data CSV",
            csv,
            "transaksi_bca_sample.csv",
            "text/csv"
        )
    
    # PROJECTS SECTION
    st.subheader("🚀 Portfolio Projects")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 📊 Banking Analytics
        **Python + Streamlit Dashboard**
        - Analisis transaksi real-time
        - Optimasi cash flow
        - Customer insights
        """)
        if st.button("View Code", key="btn1"):
            st.code("""
            # Contoh kode analisis
            def analyze_transactions(data):
                accuracy = calculate_accuracy(data)
                return accuracy
            """, language="python")
    
    with col2:
        st.markdown("""
        ### 🧮 Financial Calculator
        **Python Banking Tools**
        - Kalkulator bunga deposito
        - Konversi mata uang
        - Simulasi pinjaman
        """)
        if st.button("View Code", key="btn2"):
            st.code("""
            # Kalkulator bunga
            def calculate_interest(principal, rate):
                interest = principal * rate / 100
                return interest
            """, language="python")
    
    # FOOTER
    st.divider()
    st.markdown("""
    <div style='text-align: center'>
        <p>📚 <strong>Skills:</strong> Python • Data Analysis • Banking Operations • Mathematics</p>
        <p>🔗 <strong>GitHub:</strong> github.com/ReginaRiaAurellia</p>
        <p>⭐ <em>From counting cash to writing code - My digital transformation journey</em></p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
