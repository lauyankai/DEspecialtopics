from pyspark.sql import SparkSession
from pyspark.sql.functions import monotonically_increasing_id

spark = SparkSession.builder \
    .appName("Create Dimension Table") \
    .getOrCreate()

# Read parquet
df = spark.read.parquet("../parquet/countries_parquet")

# Create dimension table
dim_country = df.dropDuplicates() \
    .withColumn("country_id", monotonically_increasing_id())

# Reorder columns
dim_country = dim_country.select(
    "country_id",
    "Country",
    "Region"
)

print("=== DIMENSION TABLE ===")
dim_country.show()

print("=== SCHEMA ===")
dim_country.printSchema()

spark.stop()