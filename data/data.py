import streamlit as st
import pandas as pd


def load_data1() -> pd.DataFrame:
    data = {
        'Ano': ['2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024'],
        'Diária': [85.66, 86.02, 86.12, 87.80, 86.21, 85.08, 86.22, 88.93],
        'Hospedagem': [54.82, 55.05, 55.12, 56.19, 55.18, 54.45, 55.18, 56.91],
        'A&B': [32.37, 32.10, 32.75, 33.56, 34.68, 34.29, 33.80, 33.66],
        'A&B Incluso': [22.27, 22.36, 22.39, 22.83, 22.42, 22.12, 22.42, 23.12],
        'A&B Extra': [10.10, 9.74, 10.36, 10.73, 12.27, 12.16, 11.38, 10.54],
        'Lazer': [8.57, 8.60, 8.61, 8.78, 8.62, 8.51, 8.62, 8.89],
        'Eventos': [2.50, 2.42, 1.81, 0.20, 0.44, 1.94, 1.84, 0.08],
        'Outros': [1.75, 1.83, 1.70, 1.28, 1.09, 0.81, 0.55, 0.46]
    }
    try:
        df = pd.DataFrame(data)
        return df
    except Exception as e:
        st.error(f"Erro ao carregar dados: {e}")
        return pd.DataFrame()


def load_data2() -> pd.DataFrame:
    diaria = {
        'Ano': ['2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024'],
        'Original': [874.17, 967.95, 994.78, 1177.43, 1126.64, 1204.41, 1337.42, 1486.58],
        'IPCA': [1299.90, 1398.11, 1384.93, 1571.48, 1438.66, 1397.40, 1466.79, 1558.38],
        'IGPM': [1697.02, 1888.90, 1805.15, 1991.23, 1547.29, 1404.39, 1478.89, 1583.80],
        'Sal. Min': [1416.21, 1540.20, 1513.10, 1710.37, 1554.76, 1508.49, 1538.03, 1598.18],
        'Correção Média': [1471.04, 1609.07, 1567.72, 1757.69, 1513.57, 1436.76, 1494.57, 1580.12],
    }
    try:
        return pd.DataFrame(diaria)
    except Exception as e:
        st.error(f"Erro ao carregar dados: {e}")
        return pd.DataFrame()


def load_data3() -> pd.DataFrame:
    receita = {
        'Ano': ['2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024'],
        'Original': [41151543, 41219852, 40711020, 24941597, 48525312, 66316217, 69756217, 65505970],
        'IPCA': [61192804, 59538009, 56677640, 33288796, 61964473, 76942211, 76503838, 68669908],
        'IGPM': [79887189, 80438075, 73874949, 42180308, 66643021, 77327600, 77134936, 69790060],
        'Sal. Min': [66668135, 65588821, 61923175, 36230951, 66964931, 83059420, 80219650, 70423557],
        'Correção Média': [69249376, 68521635, 64158588, 37233352, 65190808, 79109744, 77952808, 69627842],
    }
    try:
        return pd.DataFrame(receita)
    except Exception as e:
        st.error(f"Erro ao carregar dados: {e}")
        return pd.DataFrame()


def load_data4() -> pd.DataFrame:
    ocupacao = {
        "Ano": [2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024],
        "Disp. Vendas": [58092, 56215, 56514, 53779, 55414, 55796, 55974, 47904],
        "Vendido": [40330, 36639, 35254, 18602, 37142, 46859, 44839, 39065],
        "Manutenção": [1768, 3645, 3346, 6245, 4446, 4064, 3886, 5806],
        "Reforma": [0, 0, 0, 0, 0, 0, 0, 6314],
        "Ocupação (%)": [67.37, 61.22, 58.90, 30.99, 62.05, 78.03, 74.91, 65.08],
        "Ocup. Disp. (%)": [69.42, 65.18, 62.38, 34.59, 67.03, 83.98, 80.11, 81.55]
    }
    try:
        return pd.DataFrame(ocupacao)
    except Exception as e:
        st.error(f"Erro ao carregar dados: {e}")
        return pd.DataFrame()

# with pd.ExcelWriter('./database.xlsx') as writer:
#     diaria.to_excel(writer, sheet_name='receita', index=False)
#     diaria.to_excel(writer, sheet_name='receita', index=False)
#     receita.to_excel(writer, sheet_name='diaria', index=False)
