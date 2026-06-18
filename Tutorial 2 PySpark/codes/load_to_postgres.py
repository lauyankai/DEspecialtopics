from pyspark.sql import SparkSession
from pyspark.sql.functions import monotonically_increasing_id

spark = SparkSession.builder \
    .appName("Load to PostgreSQL") \
    .config("spark.jars.packages", "org.postgresql:postgresql:42.7.3") \
    .getOrCreate()

# Read parquet
df = spark.read.parquet("../parquet/countries_parquet")

# Create dimension table
dim_country = df.dropDuplicates() \
    .withColumn("country_id", monotonically_increasing_id())

dim_country = dim_country.select(
    "country_id",
    "Country",
    "Region"
)

# PostgreSQL connection
url = "jdbc:postgresql://127.0.0.1:5433/censo_escolar"

properties = {
    "user": "sparkuser",
    "password": "spark123",
    "driver": "org.postgresql.Driver"
}

# Write to PostgreSQL
dim_country.write \
    .mode("overwrite") \
    .jdbc(url=url, table="dim_country", properties=properties)

print("Dimension table successfully loaded into PostgreSQL!")

spark.stop()