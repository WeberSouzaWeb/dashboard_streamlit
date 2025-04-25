import streamlit as st
import pandas as pd
from data.data import load_data1
from data.data import load_data2
from data.data import load_data3
from data.data import load_data4


def dados():
    df = load_data1()
    df2 = load_data2()
    df3 = load_data3()
    df4 = load_data4()
    tab1, tab2, tab3, tab4 = st.tabs(
        ["Hospedagem", "Diária", "Receita", "Ocupação"])

    with tab1:
        st.subheader("Dados do Dashboard Hospedagem")
        st.dataframe(
            df,
            use_container_width=True,
            height=318,
            hide_index=True,
            column_config={
                col: st.column_config.NumberColumn(format="%.2f")
                for col in df.select_dtypes(include=['float64']).columns
            }
        )

        # Botão para download
        st.download_button(
            label="Baixar CSV",
            data=df.to_csv(index=False).encode('utf-8'),
            file_name='dados_hospedagem.csv',
            mime='text/csv'
        )

    with tab2:
        st.subheader("Dados do Dashboard de Ocupação")
        st.dataframe(
            df2,
            use_container_width=True,
            height=318,
            hide_index=True,
            column_config={
                col: st.column_config.NumberColumn(format="%.2f")
                for col in df2.select_dtypes(include=['float64']).columns
            }
        )

        # Botão para download
        st.download_button(
            label="Baixar CSV",
            data=df4.to_csv(index=False).encode('utf-8'),
            file_name='dados_diaria.csv',
            mime='text/csv'
        )
    with tab3:
        st.subheader("Dados do Dashboard de Receita")
        st.dataframe(
            df3,
            use_container_width=True,
            height=318,
            hide_index=True,
            column_config={
                col: st.column_config.NumberColumn(format="%.2f")
                for col in df3.select_dtypes(include=['float64']).columns
            }
        )

        # Botão para download
        st.download_button(
            label="Baixar CSV",
            data=df3.to_csv(index=False).encode('utf-8'),
            file_name='dados_receita.csv',
            mime='text/csv'
        )
    with tab4:
        st.subheader("Dados do Dashboard de Ocupação")
        st.dataframe(
            df4,
            use_container_width=True,
            height=318,
            hide_index=True,
            column_config={
                col: st.column_config.NumberColumn(format="%.2f")
                for col in df4.select_dtypes(include=['float64']).columns
            }
        )

        # Botão para download
        st.download_button(
            label="Baixar CSV",
            data=df4.to_csv(index=False).encode('utf-8'),
            file_name='dados_ocupacao.csv',
            mime='text/csv'
        )

    # Estilo adicional
    st.markdown("""
    <style>
        .stDataFrame {
            font-size: 0.9rem;
        }
        .stTabs [data-baseweb="tab-list"] {
            gap: 10px;
        }
        .stTabs [data-baseweb="tab"] {
            padding: 8px 20px;
            border-radius: 4px 4px 0 0;
        }
    </style>
    """, unsafe_allow_html=True)
