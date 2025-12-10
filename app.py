"""
STREAMLIT APP ENTRY POINT
Banking Portfolio Dashboard
"""

import streamlit as st

# Set page config pertama
st.set_page_config(
    page_title="Regina Ria Portfolio",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Import aplikasi
from transaction_analysis import main

if __name__ == "__main__":
    main()
