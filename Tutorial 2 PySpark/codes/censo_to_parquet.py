from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Censo CSV to Parquet") \
    .getOrCreate()

csv_path = r"../raw/2021/microdados_ed_basica_2021/dados/microdados_ed_basica_2021.csv"

print("Reading CSV...")

df = spark.read.csv(
    csv_path,
    header=True,
    inferSchema=True,
    sep=";",
    encoding="latin1"
)

print("Writing parquet...")

df.write.mode("overwrite").parquet(
    "../parquet/censo_2021_parquet"
)

print("Parquet successfully created!")

spark.stop()