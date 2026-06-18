from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Read CSV Example") \
    .getOrCreate()

df = spark.read.csv(
    "../data/countries.csv",
    header=True,
    inferSchema=True
)

print("=== DATA PREVIEW ===")
df.show()

print("=== SCHEMA ===")
df.printSchema()

spark.stop()