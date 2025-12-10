import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="Regina Ria - Banking Portfolio",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ================= CUSTOM CSS =================
st.markdown("""
<style>
    /* Main background */
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    /* Card styling */
    .card {
        background: white;
        border-radius: 15px;
        padding: 25px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        margin-bottom: 20px;
        border-left: 5px solid #667eea;
    }
    
    /* Metric cards */
    .metric-card {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        border-radius: 12px;
        padding: 20px;
        text-align: center;
        box-shadow: 0 4px 15px rgba(0,0,0,0.08);
    }
    
    /* Photo frame */
    .photo-frame {
        width: 200px;
        height: 200px;
        border-radius: 50%;
        overflow: hidden;
        border: 5px solid white;
        box-shadow: 0 8px 25px rgba(0,0,0,0.15);
        margin: 0 auto;
    }
    
    /* Custom headers */
    .section-header {
        color: #2d3748;
        font-size: 1.8rem;
        margin-bottom: 1.5rem;
        padding-bottom: 0.5rem;
        border-bottom: 3px solid #667eea;
        display: inline-block;
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 12px 25px;
        border-radius: 25px;
        font-weight: 600;
        transition: all 0.3s;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 7px 20px rgba(102, 126, 234, 0.4);
    }
    
    /* Timeline styling */
    .timeline-item {
        padding-left: 25px;
        border-left: 3px solid #667eea;
        margin-bottom: 20px;
        position: relative;
    }
    
    .timeline-item:before {
        content: "●";
        position: absolute;
        left: -10px;
        color: #667eea;
        font-size: 20px;
        background: white;
        border-radius: 50%;
    }
</style>
""", unsafe_allow_html=True)

# ================= HEADER WITH PHOTO =================
col1, col2 = st.columns([1, 2])

with col1:
    st.markdown("""
    <div class="photo-frame">
        <img src="https://images.unsplash.com/photo-1580489944761-15a19d654956?ixlib=rb-4.0.3&auto=format&fit=crop&w=500&q=80" 
             style="width:100%; height:100%; object-fit:cover;">
    </div>
    """, unsafe_allow_html=True)
    
    # Quick contact
    st.markdown("""
    <div style="text-align:center; margin-top:20px;">
        <p style="color:white; font-weight:600;">📧 aurelliarial0@gmail.com</p>
        <p style="color:white; font-weight:600;">📱 081 225 805 910</p>
        <p style="color:white;">📍 Salatiga, Jawa Tengah</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style="background: rgba(255,255,255,0.95); padding: 40px; border-radius: 20px; margin-top: 20px;">
        <h1 style="color: #2d3748; margin-bottom: 10px;">🏦 Regina Ria Aurellia</h1>
        <h3 style="color: #667eea; margin-bottom: 20px;">Banking Professional | Data Enthusiast</h3>
        
        <p style="font-size: 1.1rem; color: #4a5568; line-height: 1.6;">
        Lulusan <strong>S1 Pendidikan Matematika Cum Laude</strong> dengan pengalaman 
        <strong>3 tahun sebagai Teller di BCA</strong>. Menggabungkan kemampuan analitis 
        matematika dengan pengalaman praktis perbankan untuk menciptakan solusi berbasis data.
        </p>
        
        <div style="display: flex; gap: 15px; margin-top: 25px;">
            <div style="background: #48bb78; color: white; padding: 8px 15px; border-radius: 20px; font-weight: 600;">
                🎓 Cum Laude
            </div>
            <div style="background: #4299e1; color: white; padding: 8px 15px; border-radius: 20px; font-weight: 600;">
                🏦 BCA Experience
            </div>
            <div style="background: #9f7aea; color: white; padding: 8px 15px; border-radius: 20px; font-weight: 600;">
                📊 Data Analysis
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ================= PERFORMANCE METRICS =================
st.markdown('<h2 class="section-header">📊 Performance Highlights at BCA</h2>', unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="metric-card">
        <div style="font-size: 2.5rem; color: #48bb78; font-weight: 700;">99.8%</div>
        <div style="color: #4a5568; font-size: 0.9rem;">TRANSACTION ACCURACY</div>
        <div style="color: #38a169; font-size: 0.8rem; margin-top: 5px;">▲ +1.8% above target</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="metric-card">
        <div style="font-size: 2.5rem; color: #4299e1; font-weight: 700;">4.7/5.0</div>
        <div style="color: #4a5568; font-size: 0.9rem;">CUSTOMER SATISFACTION</div>
        <div style="color: #3182ce; font-size: 0.8rem; margin-top: 5px;">▲ +0.4 above target</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="metric-card">
        <div style="font-size: 2.5rem; color: #9f7aea; font-weight: 700;">180-200</div>
        <div style="color: #4a5568; font-size: 0.9rem;">DAILY TRANSACTIONS</div>
        <div style="color: #805ad5; font-size: 0.8rem; margin-top: 5px;">▲ 20% above average</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="metric-card">
        <div style="font-size: 2.5rem; color: #ed8936; font-weight: 700;">Rp 1M</div>
        <div style="color: #4a5568; font-size: 0.9rem;">DAILY CASH HANDLING</div>
        <div style="color: #dd6b20; font-size: 0.8rem; margin-top: 5px;">▼ 0% discrepancy</div>
    </div>
    """, unsafe_allow_html=True)

# ================= TRANSACTION ANALYSIS =================
st.markdown('<h2 class="section-header">💰 Transaction Analysis Dashboard</h2>', unsafe_allow_html=True)

# Generate sample data
np.random.seed(42)
dates = pd.date_range('2024-01-01', periods=30, freq='D')
data = pd.DataFrame({
    'Date': dates,
    'Transactions': np.random.randint(150, 220, 30),
    'Cash Flow (Million Rp)': np.random.randint(500, 1200, 30),
    'Customer Satisfaction': np.round(np.random.uniform(4.3, 5.0, 30), 2),
    'Errors': np.random.randint(0, 2, 30)
})

col1, col2 = st.columns([2, 1])

with col1:
    # Transaction trend chart
    st.markdown("""
    <div class="card">
        <h4 style="color: #2d3748;">📈 Transaction Volume Trend</h4>
    """, unsafe_allow_html=True)
    st.line_chart(data.set_index('Date')['Transactions'])
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    # Summary statistics
    st.markdown("""
    <div class="card">
        <h4 style="color: #2d3748;">📊 Monthly Summary</h4>
        <div style="margin: 15px 0;">
            <div style="display: flex; justify-content: space-between; margin: 10px 0;">
                <span>Total Transactions:</span>
                <strong style="color: #667eea;">{:,}</strong>
            </div>
            <div style="display: flex; justify-content: space-between; margin: 10px 0;">
                <span>Average Daily:</span>
                <strong style="color: #667eea;">{:.0f}</strong>
            </div>
            <div style="display: flex; justify-content: space-between; margin: 10px 0;">
                <span>Total Cash Flow:</span>
                <strong style="color: #667eea;">Rp {:.1f} B</strong>
            </div>
            <div style="display: flex; justify-content: space-between; margin: 10px 0;">
                <span>Avg Satisfaction:</span>
                <strong style="color: #667eea;">{:.2f}/5.0</strong>
            </div>
        </div>
    </div>
    """.format(
        data['Transactions'].sum(),
        data['Transactions'].mean(),
        data['Cash Flow (Million Rp)'].sum() / 1000,
        data['Customer Satisfaction'].mean()
    ), unsafe_allow_html=True)

# ================= EXPERIENCE TIMELINE =================
st.markdown('<h2 class="section-header">🎓 Career Timeline</h2>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card">
        <h4 style="color: #2d3748; display: flex; align-items: center; gap: 10px;">
            <div style="background: #48bb78; color: white; width: 40px; height: 40px; border-radius: 50%; display: flex; align-items: center; justify-content: center;">🎓</div>
            Education
        </h4>
        <div class="timeline-item">
            <strong>S1 Pendidikan Matematika</strong><br>
            <em>Universitas Kristen Satya Wacana</em><br>
            <small>2017 - 2021 • Cum Laude</small>
        </div>
        <div class="timeline-item">
            <strong>SMA Negeri 2 Salatiga</strong><br>
            <em>Jurusan MIPA</em><br>
            <small>2014 - 2017</small>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <h4 style="color: #2d3748; display: flex; align-items: center; gap: 10px;">
            <div style="background: #4299e1; color: white; width: 40px; height: 40px; border-radius: 50%; display: flex; align-items: center; justify-content: center;">🏦</div>
            Banking Experience
        </h4>
        <div class="timeline-item">
            <strong>Teller - BCA Singosaren Solo</strong><br>
            <em>Full-time • Banking Operations</em><br>
            <small>Maret 2022 - Maret 2025</small>
            <ul style="margin: 10px 0 0 20px; color: #4a5568;">
                <li>99.8% transaction accuracy</li>
                <li>PIC Kaizen Project</li>
                <li>Mentor 3 new tellers</li>
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
        <h4 style="color: #2d3748; display: flex; align-items: center; gap: 10px;">
            <div style="background: #9f7aea; color: white; width: 40px; height: 40px; border-radius: 50%; display: flex; align-items: center; justify-content: center;">💼</div>
            Other Experience
        </h4>
        <div class="timeline-item">
            <strong>Finance Tutor</strong><br>
            <em>Private & Bimbingan Belajar</em><br>
            <small>2021 - 2023</small>
        </div>
        <div class="timeline-item">
            <strong>Master Teacher</strong><br>
            <em>Ruang Guru</em><br>
            <small>2021</small>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ================= SKILLS =================
st.markdown('<h2 class="section-header">🛠 Skills & Expertise</h2>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card">
        <h4 style="color: #2d3748;">💻 Technical Skills</h4>
        <div style="margin-top: 15px;">
            <div style="display: flex; justify-content: space-between; margin: 8px 0;">
                <span>Python & Data Analysis</span>
                <div style="display: flex; gap: 3px;">
                    <div style="width: 12px; height: 12px; background: #48bb78; border-radius: 2px;"></div>
                    <div style="width: 12px; height: 12px; background: #48bb78; border-radius: 2px;"></div>
                    <div style="width: 12px; height: 12px; background: #48bb78; border-radius: 2px;"></div>
                    <div style="width: 12px; height: 12px; background: #48bb78; border-radius: 2px;"></div>
                    <div style="width: 12px; height: 12px; background: #cbd5e0; border-radius: 2px;"></div>
                </div>
            </div>
            <div style="display: flex; justify-content: space-between; margin: 8px 0;">
                <span>Microsoft Office Suite</span>
                <div style="display: flex; gap: 3px;">
                    <div style="width: 12px; height: 12px; background: #4299e1; border-radius: 2px;"></div>
                    <div style="width: 12px; height: 12px; background: #4299e1; border-radius: 2px;"></div>
                    <div style="width: 12px; height: 12px; background: #4299e1; border-radius: 2px;"></div>
                    <div style="width: 12px; height: 12px; background: #4299e1; border-radius: 2px;"></div>
                    <div style="width: 12px; height: 12px; background: #4299e1; border-radius: 2px;"></div>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <h4 style="color: #2d3748;">🏦 Banking Skills</h4>
        <div style="margin-top: 15px;">
            <div style="background: #f7fafc; padding: 10px 15px; border-radius: 8px; margin: 8px 0;">
                💰 Cash Handling & Processing
            </div>
            <div style="background: #f7fafc; padding: 10px 15px; border-radius: 8px; margin: 8px 0;">
                👥 Customer Service Excellence
            </div>
            <div style="background: #f7fafc; padding: 10px 15px; border-radius: 8px; margin: 8px 0;">
                ⚠️ Risk Management
            </div>
            <div style="background: #f7fafc; padding: 10px 15px; border-radius: 8px; margin: 8px 0;">
                📋 Compliance & SOP
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
        <h4 style="color: #2d3748;">🌟 Soft Skills</h4>
        <div style="margin-top: 15px;">
            <div style="display: flex; align-items: center; gap: 10px; margin: 10px 0;">
                <div style="color: #48bb78; font-size: 1.5rem;">✓</div>
                <span>Detail-Oriented (99.8% accuracy)</span>
            </div>
            <div style="display: flex; align-items: center; gap: 10px; margin: 10px 0;">
                <div style="color: #4299e1; font-size: 1.5rem;">✓</div>
                <span>Team Leadership & Mentoring</span>
            </div>
            <div style="display: flex; align-items: center; gap: 10px; margin: 10px 0;">
                <div style="color: #9f7aea; font-size: 1.5rem;">✓</div>
                <span>Problem Solving</span>
            </div>
            <div style="display: flex; align-items: center; gap: 10px; margin: 10px 0;">
                <div style="color: #ed8936; font-size: 1.5rem;">✓</div>
                <span>Communication</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ================= FOOTER =================
st.markdown("""
<div style="text-align: center; margin-top: 50px; padding: 30px; background: rgba(255,255,255,0.9); border-radius: 15px;">
    <h3 style="color: #2d3748;">Let's Connect!</h3>
    <p style="color: #4a5568; margin: 20px 0;">
        Interested in discussing banking technology, data analysis, or career opportunities?
    </p>
    
    <div style="display: flex; justify-content: center; gap: 20px; margin: 30px 0;">
        <a href="mailto:aurelliarial0@gmail.com" style="text-decoration: none;">
            <div style="background: #4299e1; color: white; padding: 12px 25px; border-radius: 25px; font-weight: 600; display: flex; align-items: center; gap: 8px;">
                📧 Email Me
            </div>
        </a>
        <a href="https://wa.me/6281225805910" style="text-decoration: none;">
            <div style="background: #48bb78; color: white; padding: 12px 25px; border-radius: 25px; font-weight: 600; display: flex; align-items: center; gap: 8px;">
                💬 WhatsApp
            </div>
        </a>
        <a href="https://github.com/ReginaRiaAurellia" style="text-decoration: none;">
            <div style="background: #2d3748; color: white; padding: 12px 25px; border-radius: 25px; font-weight: 600; display: flex; align-items: center; gap: 8px;">
                💻 GitHub
            </div>
        </a>
    </div>
    
    <p style="color: #718096; font-size: 0.9rem; margin-top: 20px;">
        <em>"From counting cash to analyzing data – Transforming banking with mathematics & technology"</em><br>
        © 2024 Regina Ria Aurellia • Portfolio Built with Streamlit
    </p>
</div>
""", unsafe_allow_html=True)

# ================= SIDEBAR CONTENT =================
with st.sidebar:
    st.markdown("""
    <div style="background: white; padding: 20px; border-radius: 15px; margin-bottom: 20px;">
        <h4 style="color: #2d3748; margin-bottom: 15px;">🔗 Quick Links</h4>
        <div style="display: flex; flex-direction: column; gap: 10px;">
            <a href="#performance" style="text-decoration: none; color: #4a5568; padding: 10px; border-radius: 8px; background: #f7fafc; text-align: center;">
                📊 Performance Metrics
            </a>
            <a href="#timeline" style="text-decoration: none; color: #4a5568; padding: 10px; border-radius: 8px; background: #f7fafc; text-align: center;">
                🎓 Career Timeline
            </a>
            <a href="#skills" style="text-decoration: none; color: #4a5568; padding: 10px; border-radius: 8px; background: #f7fafc; text-align: center;">
                🛠 Skills & Expertise
            </a>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Download CV button
    if st.button("📄 Download CV / Portfolio", use_container_width=True):
        st.success("CV download link would be available here!")
    
    # Theme toggle (visual only)
    st.markdown("""
    <div style="background: white; padding: 20px; border-radius: 15px;">
        <h4 style="color: #2d3748; margin-bottom: 10px;">🎨 Theme</h4>
        <div style="display: flex; gap: 10px;">
            <div style="width: 30px; height: 30px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 5px; cursor: pointer;"></div>
            <div style="width: 30px; height: 30px; background: linear-gradient(135deg, #4299e1 0%, #48bb78 100%); border-radius: 5px; cursor: pointer;"></div>
            <div style="width: 30px; height: 30px; background: linear-gradient(135deg, #ed8936 0%, #dd6b20 100%); border-radius: 5px; cursor: pointer;"></div>
        </div>
    </div>
    """, unsafe_allow_html=True)
