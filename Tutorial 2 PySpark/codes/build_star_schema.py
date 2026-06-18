from pyspark.sql import SparkSession
from pyspark.sql.functions import monotonically_increasing_id, count

spark = SparkSession.builder \
    .appName("Build Star Schema") \
    .config("spark.jars.packages", "org.postgresql:postgresql:42.7.3") \
    .getOrCreate()

# Read parquet
df = spark.read.parquet("../parquet/censo_2021_parquet")

# =========================
# DIM_REGION
# =========================

dim_region = df.select("NO_REGIAO") \
    .dropDuplicates() \
    .withColumn("region_id", monotonically_increasing_id())

dim_region = dim_region.select(
    "region_id",
    "NO_REGIAO"
)

# =========================
# DIM_COUNTRY_STAR
# =========================

dim_country_star = df.select(
    "NO_MUNICIPIO",
    "NO_REGIAO"
).dropDuplicates()

dim_country_star = dim_country_star.join(
    dim_region,
    on="NO_REGIAO",
    how="left"
)

dim_country_star = dim_country_star.withColumn(
    "country_id",
    monotonically_increasing_id()
)

dim_country_star = dim_country_star.select(
    "country_id",
    "NO_MUNICIPIO",
    "region_id"
)

# =========================
# FACT TABLE
# =========================

fact_country_stats = dim_country_star.groupBy(
    "country_id"
).agg(
    count("*").alias("school_count")
)

# =========================
# PostgreSQL Connection
# =========================

url = "jdbc:postgresql://127.0.0.1:5433/censo_escolar"

properties = {
    "user": "sparkuser",
    "password": "spark123",
    "driver": "org.postgresql.Driver"
}

# =========================
# WRITE TABLES
# =========================

dim_region.write \
    .mode("overwrite") \
    .jdbc(url=url, table="dim_region", properties=properties)

dim_country_star.write \
    .mode("overwrite") \
    .jdbc(url=url, table="dim_country_star", properties=properties)

fact_country_stats.write \
    .mode("overwrite") \
    .jdbc(url=url, table="fact_country_stats", properties=properties)

print("Star schema successfully loaded!")

spark.stop()