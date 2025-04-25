from PIL import Image  # Caso queira adicionar uma imagem/logo
import streamlit as st
from PIL import Image


def home():
   # Espaçamento no topo (ajuste conforme necessário)
    st.write("")
    st.write("")

    # Container principal centralizado
    with st.container():
        col1, col2, col3 = st.columns([1, 3, 1])

        with col2:  # Coluna central (conteúdo principal)
            # Título principal
            st.markdown("""
            <h1 style='text-align: center; color: #2c3e50; margin-bottom: 30px;'>
                Bem-vindo ao Painel de Controle
            </h1>
            """, unsafe_allow_html=True)

            # Subtítulo
            st.markdown("""
            <p style='text-align: center; color: #7f8c8d; font-size: 1.1rem;'>
                Acesse os módulos através do menu lateral para visualizar os dados operacionais
            </p>
            """, unsafe_allow_html=True)

            # Divisor visual
            st.divider()

            # Métricas rápidas (opcional)
            col_met1, col_met2, col_met3 = st.columns(3)
            with col_met1:
                st.metric(label="Ocupação Atual", value="82%", delta="2% ↗")
            with col_met2:
                st.metric(label="Faturamento Mensal",
                          value="R$ 1.2M", delta="5% ↗")
            with col_met3:
                st.metric(label="Usuários Ativos", value="24", delta="1 novo")

            # Espaçamento
            st.write("")
            st.write("")

            # Imagem/ícone central (opcional - remova se não quiser)
            # Você precisaria ter uma imagem na pasta
            try:
                # Substitua pelo seu arquivo
                image = Image.open('dashboard_icon.png')
                st.image(image, width=150, use_column_width=False)
            except:
                st.info("Ícone do dashboard pode ser adicionado aqui")
