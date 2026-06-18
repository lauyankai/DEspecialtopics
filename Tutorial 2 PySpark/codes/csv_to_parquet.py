from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("CSV to Parquet") \
    .config("spark.hadoop.io.native.lib.available", "false") \
    .getOrCreate()

df = spark.read.csv(
    "../data/countries.csv",
    header=True,
    inferSchema=True
)

df.write.mode("overwrite").parquet("../parquet/countries_parquet")

print("CSV successfully converted to Parquet!")

spark.stop()