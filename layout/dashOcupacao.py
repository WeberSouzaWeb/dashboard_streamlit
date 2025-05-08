"""
Dashboard de Ocupação - Análise de Dados Habitacionais

Estrutura:
1. 4 KPIs principais
2. Gráfico misto (barras + linhas)
3. Tabela com dados brutos
"""
from scipy.interpolate import make_interp_spline
import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from data.data import load_data4
# import matplotlib
# matplotlib.use('TkAgg')  # Ou 'Qt5Agg', dependendo do que está instalado


def dashOcupacao():
    df = load_data4()

    # KPIs no topo
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.metric("Total Habitação", "59.860")
    with col2:
        st.metric("Vendido 2024",
                  f"{df.loc[df['Ano'] == 2024, 'Vendido'].values[0]:}")
    with col3:
        st.metric("Ocupação 2024",
                  f"{df.loc[df['Ano'] == 2024, 'Ocupação (%)'].values[0]:.1f}%")
    with col4:
        st.metric("PAX", "104.626")
    with col5:
        st.metric("PAX / Hab", "2,81")
    # Criação da figura
    fig = go.Figure()

    # Barras empilhadas (Disp. Vendas + Reforma + Manutenção)
    fig.add_trace(go.Bar(
        x=df['Ano'],
        y=df['Disp. Vendas'],
        name='Disp. Vendas',
        marker_color='lightgray',
        offsetgroup=1  # Mesmo grupo de offset que o Vendido
    ))

    fig.add_trace(go.Bar(
        x=df['Ano'],
        y=df['Reforma'],
        name='Reforma',
        marker_color='green',
        base=df['Disp. Vendas'],
        offsetgroup=1
    ))

    fig.add_trace(go.Bar(
        x=df['Ano'],
        y=df['Manutenção'],
        name='Manutenção',
        marker_color='orange',
        base=df['Disp. Vendas']+df['Reforma'],
        offsetgroup=1
    ))

    # Barra de Vendido - agora alinhada com as empilhadas
    fig.add_trace(go.Bar(
        x=df['Ano'],
        y=df['Vendido'],
        name='Vendido',
        marker_color='steelblue',
        offsetgroup=2,  # Mesmo grupo que as empilhadas
        base=0  # Começa da base
    ))

    # Linhas suavizadas (mantidas como antes)
    x = np.arange(len(df))
    x_smooth = np.linspace(x.min(), x.max(), 300)

    spline_ocup = make_interp_spline(x, df['Ocupação (%)'])(x_smooth)
    spline_disp = make_interp_spline(x, df['Ocup. Disp. (%)'])(x_smooth)

    fig.add_trace(go.Scatter(
        x=np.linspace(df['Ano'].min(), df['Ano'].max(), 300),
        y=spline_ocup,
        name='Ocupação (%)',
        line=dict(color='red', width=3),
        yaxis='y2'
    ))

    fig.add_trace(go.Scatter(
        x=np.linspace(df['Ano'].min(), df['Ano'].max(), 300),
        y=spline_disp,
        name='Ocup. Disp. (%)',
        line=dict(color='purple', width=3),
        yaxis='y2'
    ))

    # Linha de referência
    fig.add_hline(
        y=59860,
        line=dict(color="gray", width=2, dash="dot"),
        annotation_text="Referência (59.860)",
        annotation_position="top left"
    )
    # Layout do gráfico ajustado
    fig.update_layout(
        barmode='relative',  # Modo relativo para alinhamento perfeito
        title={
            'text': "<span class='main-title'>EVOLUÇÃO ANUAL - OCUPAÇÃO E DISPONIBILIDADE</span><br>",
            'y': 0.95,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': {
                'size': 20,  # Tamanho grande da fonte
            }},
        xaxis_title='Ano',
        yaxis_title='Unidades',
        yaxis2=dict(
            title='Percentual (%)',
            overlaying='y',
            side='right',
            range=[0, 100]
        ),
        height=600,
        bargap=0.15,  # Espaço entre grupos de barras
        bargroupgap=0.1,  # Espaço dentro do grupo
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="center",
            x=0.5
        )
    )

    st.plotly_chart(fig, use_container_width=True)

    # Tabela de Dados
    st.header("📋 Dados Brutos")
    st.dataframe(
        df,
        column_config={
            "Ano": "Ano",
            "Vendido": st.column_config.NumberColumn("Vendido"),
            "Manutenção": st.column_config.NumberColumn("Manutenção"),
            "Reforma": st.column_config.NumberColumn("Reforma"),
            "Ocupção": st.column_config.NumberColumn("Ocupação (%)", format="%.0f"),
            "Ocupação Disponivel": st.column_config.NumberColumn("Ocup. Disp. (%)", format="%.1f%%")
        },
        hide_index=True,
        use_container_width=True
    )
