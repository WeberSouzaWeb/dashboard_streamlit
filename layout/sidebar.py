import streamlit as st
from PIL import Image  # Para ícones (opcional)


def sidebar():
    with st.sidebar:
        st.title("Dashboard")
        # Variável de estado para controlar a página atual
        if 'current_page' not in st.session_state:
            st.session_state.current_page = "Home"

        # Markdown dinâmico
        st.markdown(st.session_state.current_page)

        # Ícone de perfil e usuário logado
        col1, col2 = st.columns([1, 3])
        with col1:
            # Você pode substituir por um ícone personalizado
            st.image(
                "https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=40)
        with col2:
            st.markdown(
                f"**Usuário:** {st.session_state.get('username', 'Admin')}")

        st.markdown("---")

        # Botões de navegação
        if st.button("Ocupação"):
            st.session_state.current_page = "Ocupacao"
            st.rerun()

        if st.button("Faturamento"):
            st.session_state.current_page = "Faturamento"
            st.rerun()

        # Adicione mais botões conforme necessário
        if st.button("Dados"):
            st.session_state.current_page = "Dados"
            st.rerun()

        st.markdown("---")

        # Botão Sair
        if st.button("Sair"):
            st.session_state.current_page = "Home"
            # Limpar dados de sessão se necessário
            if 'username' in st.session_state:
                del st.session_state['username']
            st.rerun()

    # CSS para o sidebar
    st.markdown("""
    <style>
        /* Container fixo para o usuário */
        div.user-container {
            display: flex;
            padding: 0.5rem 0;
            margin: 0.5rem 0;
            min-height: 60px; /* Altura fixa */
        }
        /* Remove qualquer margem que cause deslocamento */
        div[data-testid="stHorizontalBlock"] {
            margin: 0 !important;
            padding: 0 !important;
        }
        /* Mantém o ícone alinhado */
        div.user-container img {
            margin-right: 10px;
            flex-shrink: 0;
        }
        /* Texto do usuário estável */
        div.user-container p {
            margin: 0;
            white-space: nowrap;
            font-size: 0.9rem;
        }
    </style>
    """, unsafe_allow_html=True)
