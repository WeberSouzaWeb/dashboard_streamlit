# Main entry point of the HR Dashboard application using Streamlit

from layout.index import load_layout
from globals import GLOBAL_CSS
import streamlit as st


st.set_page_config(
    page_title="Dashboard Corporativo",
    layout="wide",
    page_icon="📊",  # Optional
    initial_sidebar_state="expanded"  # Optional
)

# with open(GLOBAL_CSS) as f:
#     st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
try:
    with open(GLOBAL_CSS) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
except FileNotFoundError:
    st.warning("CSS file not found. Using default styles.")


if __name__ == "__main__":
    load_layout()
