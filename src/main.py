import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import matplotlib.ticker as ticker

# Título da aplicação
st.title("Análise Histórica da Cotação USD/BRL")

# Carregamento do dataset
uploaded_file = st.file_uploader("Envie o arquivo CSV (USD_BRL_hist.csv)", type="csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # Tratamento da coluna de data
    df['Data'] = pd.to_datetime(df['Data'], format='%d.%m.%Y')
    df = df.sort_values('Data')
    df['Ano_Mes'] = df['Data'].dt.to_period('M')

    st.subheader("Primeiras linhas do dataset:")
    st.dataframe(df.head())

    # Estilo para os gráficos
    sns.set(style='whitegrid')

    # --- GRÁFICO 1: Evolução Temporal ---
    st.subheader("Evolução Temporal do Dólar")
    fig1, ax1 = plt.subplots(figsize=(14, 6))
    ax1.plot(df['Data'], df['USD_BRL'], label='USD/BRL')
    ax1.set_title('Evolução Temporal do Dólar Americano (USD) em Reais (BRL)')
    ax1.set_xlabel('Data')
    ax1.set_ylabel('Cotação USD/BRL')
    ax1.legend()
    st.pyplot(fig1)

    # --- GRÁFICO 2: Distribuição da Cotação ---
    st.subheader("Distribuição da Cotação do Dólar")
    fig2, ax2 = plt.subplots(figsize=(10, 6))
    sns.histplot(df['USD_BRL'], bins=40, kde=True, color='skyblue', ax=ax2)
    ax2.set_title('Distribuição da Cotação do Dólar (USD/BRL)')
    ax2.set_xlabel('Cotação')
    ax2.set_ylabel('Frequência')
    st.pyplot(fig2)

    # --- GRÁFICO 3: Média Mensal ---
    st.subheader("📅 Média Anual da Cotação")

    # Criar uma nova coluna de ano
    df['Ano'] = df['Data'].dt.year

    # Calcular média anual
    media_anual = df.groupby('Ano')['USD_BRL'].mean().reset_index()

    # Plotar gráfico com médias anuais
    fig3, ax3 = plt.subplots(figsize=(10, 5))
    sns.barplot(data=media_anual, x='Ano', y='USD_BRL', palette='Blues_d', ax=ax3)
    ax3.set_title('Média Anual da Cotação do Dólar (USD/BRL)')
    ax3.set_xlabel('Ano')
    ax3.set_ylabel('Cotação Média (R$)')

    # Melhorar visualização dos valores no eixo Y
    import matplotlib.ticker as ticker
    ax3.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f'R${x:.2f}'))

    st.pyplot(fig3)

else:
    st.info("Por favor, envie o arquivo CSV para iniciar a análise.")