# Databricks notebook source
# Databricks notebook source
from pyspark.sql.functions import input_file_name

# Caminho do arquivo CSV
caminho_csv = "dbfs:/FileStore/dados/database_2024.csv"

# Leitura do arquivo CSV
df_bronze = (
    spark.read.option("header", True)
              .option("inferSchema", True)
              .option("multiLine", True)
              .option("quote", '"')
              .option("escape", '"')
              .option("delimiter", ";")  # ← importante!
              .csv(caminho_csv)
              .withColumn("source_file", input_file_name())
)

# Limpeza dos nomes das colunas
def limpar_colunas(df):
    for col_name in df.columns:
        novo_nome = col_name.strip().lower().replace(" ", "_")\
                      .replace("(", "").replace(")", "")\
                      .replace("-", "_").replace("/", "_")\
                      .replace(";", "").replace(",", "")\
                      .replace("=", "")
        df = df.withColumnRenamed(col_name, novo_nome)
    return df

df_bronze = limpar_colunas(df_bronze)

# Salvando como Delta na camada bronze
df_bronze.write.format("delta").mode("overwrite").save("/mnt/bronze/gastos_deputados")

display(df_bronze)

