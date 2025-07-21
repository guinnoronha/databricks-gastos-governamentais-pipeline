# Databricks notebook source
# COMMAND ----------

# Carregando os dados da camada Gold
df_por_deputado = spark.read.format("delta").load("/mnt/gold/gastos_por_deputado")
df_por_tipo = spark.read.format("delta").load("/mnt/gold/gastos_por_tipo")
df_mensal = spark.read.format("delta").load("/mnt/gold/gastos_mensal")

# COMMAND ----------

# Visualização 1: Top 10 deputados com maiores gastos
display(
    df_por_deputado
    .orderBy("gasto_total", ascending=False)
    .limit(10)
)

# Dica: use o gráfico de barras no display e configure "nome" como eixo X e "gasto_total" como Y.

# COMMAND ----------

# Visualização 2: Gastos por tipo de despesa
display(
    df_por_tipo
    .orderBy("gasto_total", ascending=False)
)

# Dica: selecione o gráfico de pizza para visualizar a distribuição por tipo de despesa.

# COMMAND ----------

# Visualização 3: Gastos mensais ao longo do tempo
from pyspark.sql.functions import concat_ws, col

# Criar coluna "ano_mes" para facilitar o eixo temporal
df_mensal_tempo = df_mensal.withColumn("ano_mes", concat_ws("-", col("ano"), col("mes")))

display(
    df_mensal_tempo
    .orderBy("ano", "mes")
)