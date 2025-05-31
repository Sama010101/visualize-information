# 📊 Visualização da Cotação Histórica USD/BRL

Este projeto é uma aplicação web feita com **Streamlit** que permite visualizar a evolução da cotação do **dólar americano (USD)** em relação ao **real brasileiro (BRL)** ao longo do tempo.

Com ele, você pode:

- Enviar um arquivo CSV com dados históricos da cotação
- Visualizar:
  - 📈 A evolução temporal da cotação
  - 📊 A distribuição dos valores
  - 📅 A média **anual** da cotação

---

## 🧾 Formato esperado do CSV

O arquivo CSV deve conter ao menos duas colunas:

| Data       | USD_BRL |
|------------|---------|
| 01.01.2020 | 4.03    |
| 02.01.2020 | 4.05    |
| ...        | ...     |

- A coluna **"Data"** deve estar no formato `dd.mm.yyyy`.
- A coluna **"USD_BRL"** deve conter valores numéricos (float ou decimal) representando a cotação do dólar.

---

## 🛠️ Requisitos

- Python 3.10 ou superior (Python 3.13 pode apresentar incompatibilidades)
- pip

---

## 📦 Instalação

1. Clone o repositório:

    ```bash
    git clone https://github.com/Sama010101/visualize-information
    cd seu-repositorio


2. (Opcional) Crie e ative um ambiente virtual:

    bash
    Copiar
    Editar
    python -m venv venv

    ##### Windows:
    venv\Scripts\activate

    ##### macOS/Linux:
    source venv/bin/activate
   <br>

3. Instale as dependências:

     ```bash
    pip install -r requirements.txt
---

# 🚀 Como executar o projeto

No terminal, execute:

```bash
    streamlit run caminho/da/pasta/main.py
```
A aplicação será aberta no seu navegador. Basta enviar o arquivo CSV para começar a visualização.