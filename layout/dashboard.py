# Main dashboard layout with charts
import streamlit as st
import numpy as np
import plotly.express as px
from data.data import load_data1
from data.data import load_data2
from data.data import load_data3


def dashboard():
    df = load_data1()
    df2 = load_data2()
    df3 = load_data3()
    # df2 = pd.DataFrame(diaria)
    # df3 = pd.DataFrame(receita)
    kpi1, kpi2, kpi3, kpi4, kpi5 = st.columns(5)
    # ============== Filtro Indicadores ==============
    with st.container():
        col_per1, col_per2 = st.columns([1, 1])
        with col_per1:
            with st.expander("Filtros de Categorias", expanded=True):
                tipo_principal = st.radio(
                    '', ["Diária", "Receita"], horizontal=True, label_visibility="collapsed")
        with col_per2:
            with st.expander("Indicadores de Correção", expanded=True):
                indicadores_selecionados = st.multiselect('', options=["Original", "IPCA", "IGPM", "Sal. Min", "Correção Média"],
                                                          default=['Original', 'IPCA'], label_visibility="collapsed")
    df_selecionado = df2 if tipo_principal == "Diária" else df3
# ============== Grafico Indicadores ==============
  # Gráfico de barras
    st.markdown(f"### {tipo_principal} vs Indicadores")

    # Prepara dados para o gráfico
    cols_grafico = ['Ano'] + indicadores_selecionados
    df_grafico = df_selecionado[cols_grafico].melt(
        id_vars='Ano', var_name='Indicador', value_name='Valor')

    fig = px.bar(
        df_grafico,
        x='Ano',
        y='Valor',
        color='Indicador',
        barmode='group',
        labels={'Valor': 'Valor (R$)' if tipo_principal ==
                "Original" else 'Receita (R$)', 'Ano': 'Ano'},
        height=500
    )
    fig.update_layout(
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=-0.3,
            xanchor="center",
            x=0.5
        ),
        xaxis={'categoryorder': 'array',
               'categoryarray': df_selecionado['Ano']}
    )
    st.plotly_chart(fig, use_container_width=True)

######### Tabela com os dados filtrados ####################################
    st.markdown(f"### Tabela: {tipo_principal} vs Indicadores Selecionados")

    # Formatação condicional
    formatos = {
        "Original": "R$ %.2f",
        "Receita": "R$ %.2f",
        "IPCA": "R$ %.2f",
        "IGPM": "R$ %.2f",
        "Sal. Min": "R$ %.2f",
        "Correção Média": "R$ %.2f"
    }

    column_config = {
        col: st.column_config.NumberColumn(
            col,
            format=formatos.get(col, "%.2f")
        )
        for col in cols_grafico if col != 'Ano'
    }

    st.dataframe(
        df_selecionado[cols_grafico].set_index('Ano'),
        column_config=column_config,
        use_container_width=True,
        height=318
    )

    st.markdown("---")
# ============== Filtro Cenarios ==============
    with st.container():
        cols = st.columns([1, 1])
        with cols[0]:
            with st.expander("Filtros de Cenário", expanded=True):
                scenario = st.radio(
                    '', ["Real", "Setor", "Desdobrado"], horizontal=True, label_visibility="collapsed")
        with cols[1]:
            with st.expander("Distribuição das Diárias", expanded=True):
                col1, col2, col3 = st.columns([2, 2, 3])
                with col1:
                    hosp_perc = st.number_input(  # Inputs para percentuais
                        "Hospedagem (%)",
                        min_value=0, max_value=100, value=64, label_visibility="visible"
                    )
                with col2:
                    lazer_perc = st.number_input(
                        "Lazer (%)",
                        min_value=0, max_value=100, value=10, label_visibility="visible"
                    )
                if hosp_perc + lazer_perc > 100:  # Verifica se a soma não ultrapassa 100%
                    st.error("A soma dos percentuais não pode exceder 100%")
                    st.stop()
                with col3:
                    ab_incluso = 100 - (hosp_perc + lazer_perc)
                    st.text_input(
                        "A&B Incluso (%)",
                        value=f"{ab_incluso}%",
                        disabled=True,
                        label_visibility="visible"
                    )

    # ============== CÁLCULOS DINÂMICOS ==============

    def calculate_with_factors(base_df, hosp_factor, lazer_factor):
        """Calcula novos valores baseados nos fatores de distribuição"""
        df_calc = base_df.copy()

        # Converte percentuais para fatores (0-1)
        hosp_factor = hosp_factor / 100
        lazer_factor = lazer_factor / 100
        ab_incluso = 1.0 - (lazer_factor+hosp_factor)

        # Calcula novos valores
        df_calc['Hospedagem'] = df_calc['Diária'] * hosp_factor
        df_calc['Lazer'] = df_calc['Diária'] * lazer_factor
        df_calc['A&B Incluso'] = df_calc['Diária'] * ab_incluso
        df_calc['A&B'] = df_calc['A&B Incluso']+df_calc['A&B Extra']
        return df_calc

    # Aplica os cálculos com os fatores do usuário
    df_calculated = calculate_with_factors(df, hosp_perc, lazer_perc)

    def get_scenario_data(scenario, df):
        """Retorna dados filtrados por cenário"""
        if scenario == "Real":
            cols = ['Diária', 'A&B Extra', 'Eventos', 'Outros']
        elif scenario == "Setor":
            cols = ['Hospedagem', 'A&B', 'Lazer', 'Eventos', 'Outros']
        else:  # Desdobrado
            cols = ['Hospedagem', 'A&B Incluso',
                    'A&B Extra', 'Lazer', 'Eventos', 'Outros']

        scenario_df = df[['Ano'] + cols].copy()
        scenario_df['Total'] = scenario_df[cols].sum(axis=1)
        return scenario_df, cols

    scenario_df, selected_cols = get_scenario_data(scenario, df_calculated)

    # ============== KPIs DINÂMICOS ==============
    with kpi1:
        st.metric(label="Anos Analisados", value=f"{len(df)}",
                  help="Período da análise"
                  )
    with kpi2:
        # total = scenario_df['Total'].sum()
        st.metric("Diária Média", "R$ 1.486,58")
    with kpi3:
        std_dev = np.std(df2['Original'])
        st.metric(label="Desvio Padrão", value=f"R${std_dev:.2f}", delta="+16.5%",
                  delta_color="normal", help="Desvio Padrão da Diária Original")
    with kpi4:
        mean_val = np.mean(scenario_df['Total'])
        st.metric("Média Anual", f"R$ {mean_val:.2f}")
    with kpi5:
        variation = ((scenario_df.iloc[-1]['Total'] - scenario_df.iloc[0]
                     ['Total']) / scenario_df.iloc[0]['Total']) * 100
        st.metric("Variação %", f"{variation:.1f}%")

    # ============== VISUALIZAÇÕES GRAFICA ==============

    st.subheader(f"📈 Análise: {scenario}")

    with st.container(border=True):
        fig = px.bar(
            scenario_df.melt(id_vars='Ano', value_vars=selected_cols),
            title="Distribuição Percentual por Categoria de Receita (2017-2024)",
            y='Ano',
            x='value',
            color='variable',
            orientation='h',
            barmode='stack',
            text_auto='.1f',
            labels={'value': 'Percentual (%)', 'variable': 'Categoria'},
            color_discrete_map={
                'Diária': '#88B58C',
                'Hospedagem': '#8AD89E',
                'A&B': '#5682C1',
                'A&B Incluso': '#73A5AE',
                'A&B Extra': '#C6D5F4',
                'Lazer': '#FF9460',
                'Eventos': '#9FB1C5',
                'Outros': '#FFC715'
            },
        )

        # Personalização do layout (similar ao primeiro código)
        fig.update_layout(
            height=600,
            xaxis_title='Percentual (%)',
            yaxis_title='Ano',
            legend=dict(
                orientation='h',
                yanchor='bottom',
                y=-0.3,
                xanchor='center',
                x=0.5
            ),
            yaxis={'categoryorder': 'array',
                   'categoryarray': scenario_df['Ano'].tolist()},
            uniformtext_minsize=16,
            uniformtext_mode='hide'
        )

        # Adiciona grid como no primeiro código
        fig.update_xaxes(showgrid=True, gridwidth=1,
                         gridcolor='rgba(0,0,0,0.1)')

        st.plotly_chart(fig, use_container_width=True)
############# TABELA CENARIO ################################
    with st.container(border=True):
        st.markdown("##### 📋 Dados Percentuais (Anual)")

        # Prepara dados para tabela (mantém anos como linhas)
        table_data = scenario_df.set_index('Ano')[selected_cols]

        # Formatação condicional para a tabela
        st.dataframe(
            table_data,
            column_config={
                **{col: st.column_config.NumberColumn(
                    col,
                    format="%.1f%%",
                    help=f"Percentual de {col}"
                ) for col in selected_cols}
            },
            use_container_width=True,
            height=318  # Mantém a mesma altura do gráfico
        )
        column_config = {
            "Ano": st.column_config.NumberColumn("Ano", format="%d"),
            **{col: st.column_config.NumberColumn(
                col,
                format="%.1f%%"
            ) for col in selected_cols}
        }

    # ============== ESTILOS ==============
    st.markdown("""
    <style>
    div[data-testid="stMetric"] {
        background: rgba(28, 131, 225, 0.1);
        border-radius: 10px;
        padding: 15px 5px;
    }
    div[data-testid="stExpander"] div[role="radiogroup"] {
        width: 100%;
        display: flex;
        justify-content: space-between;
    }
    div[data-testid="stHorizontalBlock"] > div {
        flex: 1;
        min-width: 0 !important;
    }
    div[data-testid="stVerticalBlock"] > div[style*="flex-direction: column"] {
        gap: 0;
    }
    div.stPlotlyChart {
        height: 590px !important;
    }
    </style>
    """, unsafe_allow_html=True)
