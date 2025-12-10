"""
TRANSACTION ANALYSIS TOOL - STREAMLIT COMPATIBLE
By: Regina Ria Aurellia | Former BCA Teller
"""

try:
    import pandas as pd
    import numpy as np
    import streamlit as st
    import plotly.graph_objects as go
    import plotly.express as px
    from datetime import datetime, timedelta
    import io
    import base64
    
    # Matplotlib optional untuk Streamlit Cloud
    try:
        import matplotlib.pyplot as plt
        matplotlib_available = True
    except ImportError:
        matplotlib_available = False
        st.warning("Matplotlib not available, using Plotly instead")
        
except ImportError as e:
    st.error(f"Import Error: {e}")
    st.info("Please check requirements.txt file")

class TransactionAnalyzer:
    """Analisis transaksi perbankan - Streamlit compatible"""
    
    def __init__(self):
        self.author = "Regina Ria Aurellia"
        self.background = "S1 Pendidikan Matematika | BCA Teller 2022-2025"
        
    def generate_sample_data(self):
        """Generate data sample"""
        np.random.seed(42)
        dates = pd.date_range('2024-01-01', periods=30, freq='D')
        
        data = {
            'Tanggal': dates,
            'Jumlah_Transaksi': np.random.randint(120, 220, 30),
            'Nilai_Tunai_Juta': np.random.randint(300, 1200, 30),
            'Kepuasan_Nasabah': np.round(np.random.uniform(4.0, 5.0, 30), 2),
            'Kesalahan': np.random.randint(0, 3, 30)
        }
        
        return pd.DataFrame(data)
    
    def plot_plotly_charts(self, df):
        """Create Plotly charts (lebih compatible dengan Streamlit Cloud)"""
        # Chart 1: Transaction Volume
        fig1 = go.Figure()
        fig1.add_trace(go.Scatter(
            x=df['Tanggal'], 
            y=df['Jumlah_Transaksi'],
            mode='lines+markers',
            name='Transaksi',
            line=dict(color='blue', width=3)
        ))
        fig1.add_hline(y=150, line_dash="dash", line_color="red", 
                      annotation_text="Target BCA: 150")
        fig1.update_layout(
            title='Volume Transaksi Harian',
            xaxis_title='Tanggal',
            yaxis_title='Jumlah Transaksi'
        )
        
        # Chart 2: Cash Flow
        fig2 = go.Figure()
        fig2.add_trace(go.Bar(
            x=df['Tanggal'],
            y=df['Nilai_Tunai_Juta'],
            name='Nilai Tunai (Juta Rp)',
            marker_color='green'
        ))
        fig2.update_layout(
            title='Aliran Kas Harian',
            xaxis_title='Tanggal',
            yaxis_title='Juta Rupiah'
        )
        
        # Chart 3: Customer Satisfaction
        fig3 = go.Figure()
        fig3.add_trace(go.Scatter(
            x=df['Tanggal'],
            y=df['Kepuasan_Nasabah'],
            mode='lines+markers',
            name='Kepuasan',
            fill='tozeroy',
            line=dict(color='orange', width=3)
        ))
        fig3.update_layout(
            title='Trend Kepuasan Nasabah',
            xaxis_title='Tanggal',
            yaxis_title='Skor (1-5)',
            yaxis=dict(range=[3.5, 5.0])
        )
        
        return fig1, fig2, fig3

# Streamlit App
def main():
    st.set_page_config(
        page_title="Banking Analytics Dashboard",
        page_icon="🏦",
        layout="wide"
    )
    
    st.title("🏦 Banking Analytics Dashboard")
    st.markdown("**By: Regina Ria Aurellia** | *Former BCA Teller & Mathematics Graduate*")
    
    # Sidebar
    with st.sidebar:
        st.image("https://cdn-icons-png.flaticon.com/512/2784/2784459.png", width=100)
        st.header("Pengaturan")
        st.info("Dashboard ini berdasarkan pengalaman nyata di BCA")
        
        if st.button("📊 Generate Report"):
            st.session_state.generate_report = True
            
        st.divider()
        st.caption("S1 Matematika Cum Laude | BCA 2022-2025")
        st.caption("Akurasi: 99.8% | Kepuasan: 4.7/5.0")
    
    # Main content
    analyzer = TransactionAnalyzer()
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("🏆 Akurasi Transaksi", "99.8%", "1.8%")
    with col2:
        st.metric("👥 Transaksi/Hari", "187", "12%")
    with col3:
        st.metric("😊 Kepuasan Nasabah", "4.7/5.0", "0.4")
    
    # Generate data
    df = analyzer.generate_sample_data()
    
    # Display charts
    st.subheader("📈 Analisis Trend")
    fig1, fig2, fig3 = analyzer.plot_plotly_charts(df)
    
    col1, col2 = st.columns(2)
    with col1:
        st.plotly_chart(fig1, use_container_width=True)
    with col2:
        st.plotly_chart(fig2, use_container_width=True)
    
    st.plotly_chart(fig3, use_container_width=True)
    
    # Data table
    with st.expander("📋 Lihat Data Transaksi"):
        st.dataframe(df)
        
        # Download button
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Download Data CSV",
            data=csv,
            file_name="transaksi_bca_sample.csv",
            mime="text/csv"
        )
    
    # Performance summary
    st.subheader("📊 Ringkasan Performa")
    
    total_cash = df['Nilai_Tunai_Juta'].sum() * 1_000_000
    accuracy = (1 - (df['Kesalahan'].sum() / df['Jumlah_Transaksi'].sum())) * 100
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Transaksi", f"{df['Jumlah_Transaksi'].sum():,}")
    with col2:
        st.metric("Total Nilai Tunai", f"Rp {total_cash:,.0f}")
    with col3:
        st.metric("Akurasi Rata-rata", f"{accuracy:.2f}%")
    with col4:
        st.metric("Kepuasan Rata-rata", f"{df['Kepuasan_Nasabah'].mean():.2f}/5.0")
    
    # Footer
    st.divider()
    st.caption("""
    **Disclaimer:** Data ini merupakan simulasi berdasarkan pengalaman kerja di BCA. 
    Dashboard ini menunjukkan kemampuan analitis dengan Python & Streamlit.
    """)

if __name__ == "__main__":
    main()
