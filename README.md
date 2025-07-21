# 📊 Análise dos Gastos Públicos dos Deputados Federais

Este projeto tem como objetivo construir um pipeline de engenharia de dados no **Databricks**, utilizando **PySpark**, para analisar os **gastos públicos declarados por deputados federais brasileiros**, com base em dados abertos disponibilizados pela Câmara dos Deputados.

---

## 📁 Estrutura do Projeto

├── notebooks/
│ ├── 01_ingestao_dados.ipynb
│ ├── 02_transformacao_dados.ipynb
│ ├── 03_limpando_e_modelando.ipynb
│ └── 04_analise_exploratoria.ipynb
├── data/
│ └── database_2024.csv (dados brutos dos gastos parlamentares)
└── README.md

---

## 🧱 Tecnologias Utilizadas

- **Apache Spark** (via Databricks)
- **PySpark**
- **Delta Lake**
- **Databricks Notebooks**
- **Pandas e Matplotlib** (para análises complementares, se necessário)

---

## 🧪 Notebooks Explicados

### 📥 01_ingestao_dados

- Leitura dos arquivos CSV contendo os gastos parlamentares.
- Padronização dos nomes das colunas.
- Escrita dos dados crus em formato Delta Lake para processamento eficiente.

### 🔧 02_transformacao_dados

- Carregamento dos dados Delta.
- Seleção e renomeação das colunas principais.
- Conversão de datas, tratamento de tipos e valores nulos.

### 🧹 03_limpando_e_modelando

- Criação de tabelas analíticas com agregações por deputado, tipo de despesa e tempo (ano/mês).
- Preparação para análises visuais e relatórios.

### 📊 04_analise_exploratoria

- Geração de insights com Spark SQL e DataFrames:
  - Maiores gastos por deputado.
  - Evolução dos gastos ao longo do tempo.
  - Tipos de despesas mais frequentes.

---

## 🗂️ Fonte dos Dados

Os dados foram extraídos do portal da Câmara dos Deputados:  
🔗 https://www.camara.leg.br/transparencia/gastos-parlamentares/

---

## 🚀 Como Executar

1. Suba os arquivos `.csv` dos gastos para o **Databricks FileStore** ou para uma pasta do DBFS (por exemplo, `/FileStore/gastos/`).
2. Execute sequencialmente os notebooks:
   - **01_ingestao_dados**
   - **02_transformacao_dados**
   - **03_limpando_e_modelando**
   - **04_analise_exploratoria**
3. Visualize os resultados diretamente no notebook.

---

## 📌 Possíveis Extensões

- Criação de dashboards com **Power BI** ou **Tableau**.
- Pipeline automatizado com **Databricks Workflows**.
- Integração com dados de votação, presença ou redes sociais dos parlamentares.

---

## 👨‍💻 Autor

**Guilherme Mello**  
Engenheiro de Dados | Analista de Soluções  

