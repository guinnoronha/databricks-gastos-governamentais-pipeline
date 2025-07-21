# 🏛️ Projeto: Análise dos Gastos dos Deputados com Databricks

Este projeto utiliza dados públicos da Câmara dos Deputados para construir uma pipeline de engenharia de dados no Databricks, aplicando boas práticas com Delta Lake e camadas Bronze → Silver → Gold.

---

## 📊 Objetivo

Transformar dados brutos sobre os gastos parlamentares em insights úteis e acessíveis à sociedade, permitindo análises como:

- Quem são os deputados que mais gastam?
- Quais os tipos de despesa mais comuns?
- Há sazonalidade nos gastos?
- Como o gasto médio evolui ao longo do tempo?

---

## 🔧 Tecnologias Utilizadas

- **Databricks** (PySpark, Delta Lake, SQL)
- **Python**
- **Visualização**: Databricks SQL / Power BI
- **Armazenamento**: DBFS (Delta)

---

## 📁 Estrutura dos Notebooks

| Notebook | Descrição |
|----------|-----------|
| `01_ingestao_csv` | Lê dados CSV dos gastos e salva em Delta (Bronze) |
| `02_transformacao_silver` | Limpa, transforma e estrutura dados (Silver) |
| `03_modelagem_gold` | Agrega e cria fatos para análise (Gold) |
| `04_analise_final` | Dashboards exploratórios com Spark SQL |

---

## 📂 Camadas do Data Lake

- **Bronze**: Dados brutos (CSV)
- **Silver**: Dados tratados e estruturados
- **Gold**: Dados prontos para análise e BI

---

## 📦 Fonte de Dados

Portal da Câmara dos Deputados – [https://www.camara.leg.br/transparencia/despesas-parlamentares/](https://www.camara.leg.br/transparencia/despesas-parlamentares/)

---

## 🛠️ Como Executar

1. Suba o arquivo CSV para `/FileStore/dados/gastos_deputados_2024.csv`
2. Execute os notebooks em ordem (1 → 4)
3. Analise os resultados via display ou conecte ao Power BI
4. (Opcional) Crie dashboards com Databricks SQL

---

## 📌 Exemplos de Visualizações

- Top 10 deputados por gasto total
- Evolução mensal de gastos por partido
- Distribuição por tipo de despesa
- Comparativo de gastos entre estados

---

## 📃 Licença

Projeto para fins educacionais com dados públicos.

---

## ✉️ Contato

Guilherme Mello  
[LinkedIn](https://linkedin.com/in/seu-perfil) • [GitHub](https://github.com/seu-usuario)

