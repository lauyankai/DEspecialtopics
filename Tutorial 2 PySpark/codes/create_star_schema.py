from pyspark.sql import SparkSession
from pyspark.sql.functions import monotonically_increasing_id, lit, col

spark = SparkSession.builder \
    .appName("Create Star Schema") \
    .config("spark.jars.packages", "org.postgresql:postgresql:42.7.3") \
    .getOrCreate()

# Read parquet data
df = spark.read.parquet("../parquet/countries_parquet")

# -----------------------------
# Dimension 1: Region
# -----------------------------
dim_region = df.select("Region") \
    .dropDuplicates() \
    .withColumn("region_id", monotonically_increasing_id()) \
    .select("region_id", "Region")

# -----------------------------
# Dimension 2: Country
# -----------------------------
dim_country = df.select("Country", "Region") \
    .dropDuplicates() \
    .join(dim_region, on="Region", how="left") \
    .withColumn("country_id", monotonically_increasing_id()) \
    .select("country_id", "Country", "region_id")

# -----------------------------
# Fact Table
# -----------------------------
fact_country_stats = df.select("Country", "Region") \
    .dropDuplicates() \
    .join(dim_country, on="Country", how="left") \
    .withColumn("country_count", lit(1)) \
    .select("country_id", "country_count")

# PostgreSQL connection
url = "jdbc:postgresql://127.0.0.1:5433/censo_escolar"

properties = {
    "user": "sparkuser",
    "password": "spark123",
    "driver": "org.postgresql.Driver"
}

# Load tables
dim_region.write.mode("overwrite").jdbc(url=url, table="dim_region", properties=properties)
dim_country.write.mode("overwrite").jdbc(url=url, table="dim_country_star", properties=properties)
fact_country_stats.write.mode("overwrite").jdbc(url=url, table="fact_country_stats", properties=properties)

print("Star schema tables successfully loaded into PostgreSQL!")

print("=== dim_region ===")
dim_region.show()

print("=== dim_country ===")
dim_country.show()

print("=== fact_country_stats ===")
fact_country_stats.show()

spark.stop()