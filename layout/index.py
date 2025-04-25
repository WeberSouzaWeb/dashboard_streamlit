# Top-level layout for the app

import streamlit as st
from layout.sidebar import sidebar
from layout.dashboard import dashboard
from layout.dashOcupacao import dashOcupacao
from layout.home import home
from layout.dados import dados


def load_layout():
    # Configuração inicial da página
    # st.set_page_config(page_title="Home", layout="wide")

    # Inicializa o usuário (substitua por sua lógica de autenticação)
    if 'username' not in st.session_state:
        st.session_state.username = "Admin"  # Ou obtenha do seu sistema de login
    # Carrega o sidebar
    sidebar()

    # Lógica para exibir o conteúdo com base na página selecionada
    if st.session_state.current_page == "Home":
        home()

    elif st.session_state.current_page == "Faturamento":
        st.header("Análise Faturamento")
        dashboard()
    elif st.session_state.current_page == "Ocupacao":
        st.header("Análise de Ocupação")
        dashOcupacao()
    elif st.session_state.current_page == "Dados":
        st.title("📊 Dados Brutos Completos")
        dados()

    # Ou redirecione para outra página:
    # st.switch_page("pages/finance/overview.py")
