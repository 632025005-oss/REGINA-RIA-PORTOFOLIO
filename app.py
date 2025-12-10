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

# ================= DARK THEME CSS =================
st.markdown("""
<style>
    /* Main background */
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
    }
    
    /* Card styling */
    .card {
        background: rgba(30, 41, 59, 0.85);
        border-radius: 15px;
        padding: 25px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.3);
        margin-bottom: 20px;
        border-left: 5px solid #3b82f6;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(100, 116, 139, 0.2);
    }
    
    /* Metric cards */
    .metric-card {
        background: linear-gradient(135deg, rgba(30, 41, 59, 0.9) 0%, rgba(51, 65, 85, 0.9) 100%);
        border-radius: 12px;
        padding: 20px;
        text-align: center;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        border: 1px solid rgba(100, 116, 139, 0.2);
    }
    
    /* Photo frame */
    .photo-frame {
        width: 200px;
        height: 200px;
        border-radius: 50%;
        overflow: hidden;
        border: 5px solid rgba(30, 41, 59, 0.9);
        box-shadow: 0 8px 25px rgba(0,0,0,0.3);
        margin: 0 auto;
    }
    
    /* Custom headers */
    .section-header {
        color: #e2e8f0;
        font-size: 1.8rem;
        margin-bottom: 1.5rem;
        padding-bottom: 0.5rem;
        border-bottom: 3px solid #3b82f6;
        display: inline-block;
        font-weight: 600;
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%);
        color: white;
        border: none;
        padding: 12px 25px;
        border-radius: 25px;
        font-weight: 600;
        transition: all 0.3s;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 7px 20px rgba(59, 130, 246, 0.4);
        background: linear-gradient(135deg, #2563eb 0%, #1e40af 100%);
    }
    
    /* Timeline styling */
    .timeline-item {
        padding-left: 25px;
        border-left: 3px solid #3b82f6;
        margin-bottom: 20px;
        position: relative;
    }
    
    .timeline-item:before {
        content: "●";
        position: absolute;
        left: -10px;
        color: #3b82f6;
        font-size: 20px;
        background: #0f172a;
        border-radius: 50%;
        width: 20px;
        height: 20px;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    
    /* Custom text colors */
    h1, h2, h3, h4, h5, h6 {
        color: #f1f5f9 !important;
    }
    
    p, span, li, td, th {
        color: #cbd5e1 !important;
    }
    
    strong {
        color: #e2e8f0 !important;
    }
    
    /* Link styling */
    a {
        color: #60a5fa !important;
        text-decoration: none;
    }
    
    a:hover {
        color: #93c5fd !important;
        text-decoration: underline;
    }
    
    /* Sidebar styling */
    .css-1d391kg, .css-12oz5g7 {
        background-color: #0f172a !important;
    }
    
    /* Text input styling */
    .stTextInput > div > div > input {
        background-color: #1e293b;
        color: #e2e8f0;
        border: 1px solid #475569;
    }
    
    /* Select box styling */
    .stSelectbox > div > div > select {
        background-color: #1e293b;
        color: #e2e8f0;
        border: 1px solid #475569;
    }
    
    /* Divider */
    hr {
        border-color: #475569 !important;
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
        <p style="color:#60a5fa; font-weight:600;">📧 aurelliarial0@gmail.com</p>
        <p style="color:#60a5fa; font-weight:600;">📱 081 225 805 910</p>
        <p style="color:#94a3b8;">📍 Salatiga, Jawa Tengah</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <h1 style="color: #f1f5f9; margin-bottom: 10px;">🏦 Regina Ria Aurellia</h1>
        <h3 style="color: #60a5fa; margin-bottom: 20px;">Banking Professional | Data Enthusiast</h3>
        
        <p style="font-size: 1.1rem; color: #cbd5e1; line-height: 1.6;">
        Lulusan <strong>S1 Pendidikan Matematika Cum Laude</strong> dengan pengalaman 
        <strong>3 tahun sebagai Teller di BCA</strong>. Menggabungkan kemampuan analitis 
        matematika dengan pengalaman praktis perbankan untuk menciptakan solusi berbasis data.
        </p>
        
        <div style="display: flex; gap: 15px; margin-top: 25px;">
            <div style="background: linear-gradient(135deg, #10b981 0%, #059669 100%); color: white; padding: 8px 15px; border-radius: 20px; font-weight: 600; border: 1px solid rgba(255,255,255,0.1);">
                🎓 Cum Laude
            </div>
            <div style="background: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%); color: white; padding: 8px 15px; border-radius: 20px; font-weight: 600; border: 1px solid rgba(255,255,255,0.1);">
                🏦 BCA Experience
            </div>
            <div style="background: linear-gradient(135deg, #8b5cf6 0%, #7c3aed 100%); color: white; padding: 8px 15px; border-radius: 20px; font-weight: 600; border: 1px solid rgba(255,255,255,0.1);">
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
        <div style="font-size: 2.5rem; color: #10b981; font-weight: 700;">99.8%</div>
        <div style="color: #cbd5e1; font-size: 0.9rem;">TRANSACTION ACCURACY</div>
        <div style="color: #34d399; font-size: 0.8rem; margin-top: 5px;">▲ +1.8% above target</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="metric-card">
        <div style="font-size: 2.5rem; color: #60a5fa; font-weight: 700;">4.7/5.0</div>
        <div style="color: #cbd5e1; font-size: 0.9rem;">CUSTOMER SATISFACTION</div>
        <div style="color: #93c5fd; font-size: 0.8rem; margin-top: 5px;">▲ +0.4 above target</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="metric-card">
        <div style="font-size: 2.5rem; color: #8b5cf6; font-weight: 700;">180-200</div>
        <div style="color: #cbd5e1; font-size: 0.9rem;">DAILY TRANSACTIONS</div>
        <div style="color: #a78bfa; font-size: 0.8rem; margin-top: 5px;">▲ 20% above average</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="metric-card">
        <div style="font-size: 2.5rem; color: #f59e0b; font-weight: 700;">Rp 1M</div>
        <div style="color: #cbd5e1; font-size: 0.9rem;">DAILY CASH HANDLING</div>
        <div style="color: #fbbf24; font-size: 0.8rem; margin-top: 5px;">▼ 0% discrepancy</div>
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
        <h4 style="color: #f1f5f9;">📈 Transaction Volume Trend</h4>
    """, unsafe_allow_html=True)
    st.line_chart(data.set_index('Date')['Transactions'], height=300)
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    # Summary statistics
    st.markdown("""
    <div class="card">
        <h4 style="color: #f1f5f9;">📊 Monthly Summary</h4>
        <div style="margin: 15px 0;">
            <div style="display: flex; justify-content: space-between; margin: 10px 0;">
                <span style="color: #cbd5e1;">Total Transactions:</span>
                <strong style="color: #60a5fa;">{:,}</strong>
            </div>
            <div style="display: flex; justify-content: space-between; margin: 10px 0;">
                <span style="color: #cbd5e1;">Average Daily:</span>
                <strong style="color: #60a5fa;">{:.0f}</strong>
            </div>
            <div style="display: flex; justify-content: space-between; margin: 10px 0;">
                <span style="color: #cbd5e1;">Total Cash Flow:</span>
                <strong style="color: #60a5fa;">Rp {:.1f} B</strong>
            </div>
            <div style="display: flex; justify-content: space-between; margin: 10px 0;">
                <span style="color: #cbd5e1;">Avg Satisfaction:</span>
                <strong style="color: #60a5fa;">{:.2f}/5.0</strong>
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
        <h4 style="color: #f1f5f9; display: flex; align-items: center; gap: 10px;">
            <div style="background: #10b981; color: white; width: 40px; height: 40px; border-radius: 50%; display: flex; align-items: center; justify-content: center;">🎓</div>
            Education
        </h4>
        <div class="timeline-item">
            <strong>S1 Pendidikan Matematika</strong><br>
            <em style="color: #94a3b8;">Universitas Kristen Satya Wacana</em><br>
            <small style="color: #64748b;">2017 - 2021 • Cum Laude</small>
        </div>
        <div class="timeline-item">
            <strong>SMA Negeri 2 Salatiga</strong><br>
            <em style="color: #94a3b8;">Jurusan MIPA</em><br>
            <small style="color: #64748b;">2014 - 2017</small>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <h4 style="color: #f1f5f9; display: flex; align-items: center; gap: 10px;">
            <div style="background: #3b82f6; color: white; width: 40px; height: 40px; border-radius: 50%; display: flex; align-items: center; justify-content: center;">🏦</div>
            Banking Experience
        </h4>
        <div class="timeline-item">
            <strong>Teller - BCA Singosaren Solo</strong><br>
            <em style="color: #94a3b8;">Full-time • Banking Operations</em><br>
            <small style="color: #64748b;">Maret 2022 - Maret 2025</small>
            <ul style="margin: 10px 0 0 20px; color: #cbd5e1;">
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
        <h4 style="color: #f1f5f9; display: flex; align-items: center; gap: 10px;">
            <div style="background: #8b5cf6; color: white; width: 40px; height: 40px; border-radius: 50%; display: flex; align-items: center; justify-content: center;">💼</div>
            Other Experience
        </h4>
        <div class="timeline-item">
            <strong>Finance Tutor</strong><br>
            <em style="color: #94a3b8;">Private & Bimbingan Belajar</em><br>
            <small style="color: #64748b;">2021 - 2023</small>
        </div>
        <div class="timeline-item">
            <strong>Master Teacher</strong><br>
            <em style="color: #94a3b8;">Ruang Guru</em><br>
            <small style="color: #64748b;">2021</small>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ================= SKILLS =================
st.markdown('<h2 class="section-header">🛠 Skills & Expertise</h2>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card">
        <h4 style="color: #f1f5f9;">💻 Technical Skills</h4>
        <div style="margin-top: 15px;">
            <div style="display: flex; justify-content: space-between; margin: 8px 0;">
                <span style="color: #cbd5e1;">Python & Data Analysis</span>
                <div style="display: flex; gap: 3px;">
                    <div style="width: 12px; height: 12px; background: #10b981; border-radius: 2px;"></div>
                    <div style="width: 12px; height: 12px; background: #10b981; border-radius: 2px;"></div>
                    <div style="width: 12px; height: 12px; background: #10b981; border-radius: 2px;"></div>
                    <div style="width: 12px; height: 12px; background: #10b981; border-radius: 2px;"></div>
                    <div style="width: 12px; height: 12px; background: #475569; border-radius: 2px;"></div>
                </div>
            </div>
            <div style="display: flex; justify-content: space-between; margin: 8px 0;">
                <span style="color: #cbd5e1;">Microsoft Office Suite</span>
                <div style="display: flex; gap: 3px;">
                    <div style="width: 12px; height: 12px; background: #3b82f6; border-radius: 2px;"></div>
                    <div style="width: 12px; height: 12px; background: #3b82f6; border-radius: 2px;"></div>
                    <div style="width: 12px; height: 12px; background: #3b82f6; border-radius: 2px;"></div>
                    <div style="width: 12px; height: 12px; background: #3b82f6; border-radius: 2px;"></div>
                    <div style="width: 12px; height: 12px; background: #3b82f6; border-radius: 2px;"></div>
                </div>
            </div>
            <div style="display: flex; justify-content: space-between; margin: 8px 0;">
                <span style="color: #cbd5e1;">SQL & Databases</span>
                <div style="display: flex; gap: 3px;">
                    <div style="width: 12px; height: 12px; background: #8b5cf6; border-radius: 2px;"></div>
                    <div style="width: 12px; height: 12px; background: #8b5cf6; border-radius: 2px;"></div>
                    <div style="width: 12px; height: 12px; background: #8b5cf6; border-radius: 2px;"></div>
                    <div style="width: 12px; height: 12px; background: #475569; border-radius: 2px;"></div>
                    <div style="width: 12px; height: 12px; background: #475569; border-radius: 2px;"></div>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <h4 style="color: #f1f5f9;">🏦 Banking Skills</h4>
        <div style="margin-top: 15px;">
            <div style="background: rgba(15, 23, 42, 0.6); padding: 10px 15px; border-radius: 8px; margin: 8px 0; border: 1px solid rgba(100, 116, 139, 0.2);">
                💰 Cash Handling & Processing
            </div>
            <div style="background: rgba(15, 23, 42, 0.6); padding: 10px 15px; border-radius: 8px; margin: 8px 0; border: 1px solid rgba(100, 116, 139, 0.2);">
                👥 Customer Service Excellence
            </div>
            <div style="background: rgba(15, 23, 42, 0.6); padding: 10px 15px; border-radius: 8px; margin: 8px 0; border: 1px solid rgba(100, 116, 139, 0.2);">
                ⚠️ Risk Management
            </div>
            <div style="background: rgba(15, 23, 42, 0.6); padding: 10px 15px; border-radius: 8px; margin: 8px 0; border: 1px solid rgba(100, 116, 139, 0.2);">
                📋 Compliance & SOP
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
        <h4 style="color: #f1f5f9;">🌟 Soft Skills</h4>
        <div style="margin-top: 15px;">
            <div style="display: flex; align-items: center; gap: 10px; margin: 10px 0;">
                <div style="color: #10b981; font-size: 1.5rem;">✓</div>
                <span style="color: #cbd5e1;">Detail-Oriented (99.8% accuracy)</span>
            </div>
            <div style="display: flex; align-items: center; gap: 10px; margin: 10px 0;">
                <div style="color: #3b82f6; font-size: 1.5rem;">✓</div>
                <span style="color: #cbd5e1;">Team Leadership & Mentoring</span>
            </div>
            <div style="display: flex; align-items: center; gap: 10px; margin: 10px 0;">
                <div style="color: #8b5cf6; font-size: 1.5rem;">✓</div>
                <span style="color: #cbd5e1;">Problem Solving</span>
            </div>
            <div style="display: flex; align-items: center; gap: 10px; margin: 10px 0;">
                <div style="color: #f59e0b; font-size: 1.5rem;">✓</div>
                <span style="color: #cbd5e1;">Communication</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ================= FOOTER =================
st.markdown("""
<div class="card" style="text-align: center; margin-top: 50px;">
    <h3 style="color: #f1f5f9;">Let's Connect!</h3>
    <p style="color: #cbd5e1; margin: 20px 0;">
        Interested in discussing banking technology, data analysis, or career opportunities?
    </p>
    
    <div style="display: flex; justify-content: center; gap: 20px; margin: 30px 0;">
        <a href="mailto:aurelliarial0@gmail.com" style="text-decoration: none;">
            <div style="background: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%); color: white; padding: 12px 25px; border-radius: 25px; font-weight: 600; display: flex; align-items: center; gap: 8px; border: 1px solid rgba(255,255,255,0.1);">
                📧 Email Me
            </div>
        </a>
        <a href="https://wa.me/6281225805910" style="text-decoration: none;">
            <div style="background: linear-gradient(135deg, #10b981 0%, #059669 100%); color: white; padding: 12px 25px; border-radius: 25px; font-weight: 600; display: flex; align-items: center; gap: 8px; border: 1px solid rgba(255,255,255,0.1);">
                💬 WhatsApp
            </div>
        </a>
        <a href="https://github.com/ReginaRiaAurellia" style="text-decoration: none;">
            <div style="background: linear-gradient(135deg, #475569 0%, #1e293b 100%); color: white; padding: 12px 25px; border-radius: 25px; font-weight: 600; display: flex; align-items: center; gap: 8px; border: 1px solid rgba(255,255,255,0.1);">
                💻 GitHub
            </div>
        </a>
    </div>
    
    <p style="color: #94a3b8; font-size: 0.9rem; margin-top: 20px;">
        <em>"From counting cash to analyzing data – Transforming banking with mathematics & technology"</em><br>
        © 2024 Regina Ria Aurellia • Portfolio Built with Streamlit
    </p>
</div>
""", unsafe_allow_html=True)

# ================= SIDEBAR CONTENT =================
with st.sidebar:
    st.markdown("""
    <div class="card" style="margin-bottom: 20px;">
        <h4 style="color: #f1f5f9; margin-bottom: 15px;">🔗 Quick Links</h4>
        <div style="display: flex; flex-direction: column; gap: 10px;">
            <a href="#performance" style="text-decoration: none;">
                <div style="color: #cbd5e1; padding: 10px; border-radius: 8px; background: rgba(15, 23, 42, 0.6); text-align: center; border: 1px solid rgba(100, 116, 139, 0.2);">
                    📊 Performance Metrics
                </div>
            </a>
            <a href="#timeline" style="text-decoration: none;">
                <div style="color: #cbd5e1; padding: 10px; border-radius: 8px; background: rgba(15, 23, 42, 0.6); text-align: center; border: 1px solid rgba(100, 116, 139, 0.2);">
                    🎓 Career Timeline
                </div>
            </a>
            <a href="#skills" style="text-decoration: none;">
                <div style="color: #cbd5e1; padding: 10px; border-radius: 8px; background: rgba(15, 23, 42, 0.6); text-align: center; border: 1px solid rgba(100, 116, 139, 0.2);">
                    🛠 Skills & Expertise
                </div>
            </a>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Download CV button
    if st.button("📄 Download CV / Portfolio", use_container_width=True):
        st.success("CV download link would be available here!")
    
    # Theme toggle (visual only)
    st.markdown("""
    <div class="card">
        <h4 style="color: #f1f5f9; margin-bottom: 10px;">🎨 Theme</h4>
        <div style="display: flex; gap: 10px;">
            <div style="width: 30px; height: 30px; background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%); border-radius: 5px; cursor: pointer; border: 2px solid #3b82f6;"></div>
            <div style="width: 30px; height: 30px; background: linear-gradient(135deg, #1e3a8a 0%, #1e40af 100%); border-radius: 5px; cursor: pointer;"></div>
            <div style="width: 30px; height: 30px; background: linear-gradient(135deg, #064e3b 0%, #065f46 100%); border-radius: 5px; cursor: pointer;"></div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Certifications
    st.markdown("""
    <div class="card">
        <h4 style="color: #f1f5f9; margin-bottom: 10px;">🏆 Certifications</h4>
        <div style="display: flex; flex-direction: column; gap: 8px;">
            <div style="background: rgba(15, 23, 42, 0.6); padding: 10px; border-radius: 8px; border-left: 3px solid #10b981;">
                <small style="color: #94a3b8;">BCA</small><br>
                <span style="color: #cbd5e1; font-size: 0.9rem;">Teller Certification</span>
            </div>
            <div style="background: rgba(15, 23, 42, 0.6); padding: 10px; border-radius: 8px; border-left: 3px solid #3b82f6;">
                <small style="color: #94a3b8;">Coursera</small><br>
                <span style="color: #cbd5e1; font-size: 0.9rem;">Python for Data Science</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
