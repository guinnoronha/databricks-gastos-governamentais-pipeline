# Databricks notebook source
# Databricks notebook source
from pyspark.sql.functions import sum, col

# Leitura da camada Silver
df_silver = spark.read.format("delta").load("/mnt/silver/gastos_deputados")

# Exibe o schema para conferência
df_silver.printSchema()

# COMMAND ----------

# Agregação 1: Gasto total por deputado
df_gastos_por_deputado = (
    df_silver.groupBy("id_deputado", "nome", "partido", "uf")
    .agg(sum("valor").alias("gasto_total"))
    .orderBy(col("gasto_total").desc())
)

# COMMAND ----------

# Agregação 2: Gasto total por tipo de despesa
df_gastos_por_tipo = (
    df_silver.groupBy("tipo_despesa")
    .agg(sum("valor").alias("gasto_total"))
    .orderBy(col("gasto_total").desc())
)

# COMMAND ----------

# Agregação 3: Gasto total por mês e ano
df_gastos_mensal = (
    df_silver.groupBy("ano", "mes")
    .agg(sum("valor").alias("gasto_total"))
    .orderBy("ano", "mes")
)

# COMMAND ----------

# Salvando as tabelas agregadas na camada Gold
df_gastos_por_deputado.write.format("delta").mode("overwrite").save("/mnt/gold/gastos_por_deputado")
df_gastos_por_tipo.write.format("delta").mode("overwrite").save("/mnt/gold/gastos_por_tipo")
df_gastos_mensal.write.format("delta").mode("overwrite").save("/mnt/gold/gastos_mensal")

# COMMAND ----------

# Exibir uma das agregações para visualização
display(df_gastos_por_deputado)
