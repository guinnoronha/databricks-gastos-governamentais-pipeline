# Databricks notebook source
from pyspark.sql.functions import col, to_date

# Leitura da camada bronze
df_bronze = spark.read.format("delta").load("/mnt/bronze/gastos_deputados")

# Seleção e renomeação de colunas com base no CSV real
df_silver = (
    df_bronze.select(
        col("numano").alias("ano"),
        col("nummes").alias("mes"),
        col("nudeputadoid").alias("id_deputado"),
        col("txnomeparlamentar").alias("nome"),
        col("sgpartido").alias("partido"),
        col("sguf").alias("uf"),
        col("txtdescricao").alias("tipo_despesa"),
        col("vlrliquido").alias("valor"),
        to_date(col("datemissao"), "yyyy-MM-dd").alias("data_documento")
    )
    .dropna(subset=["valor"])
)

# Salvando na camada silver
df_silver.write.format("delta").mode("overwrite").save("/mnt/silver/gastos_deputados")

display(df_silver)
