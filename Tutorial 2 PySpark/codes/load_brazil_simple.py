from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# CHANGE THIS PATH TO YOUR BRAZILIAN CSV FILE
DATA_PATH = r"C:\spark-etl-project\raw\2021\microdados_ed_basica_2021\dados\microdados_ed_basica_2021.csv"

spark = SparkSession.builder \
    .appName("Load Brazilian School Census Simple Table") \
    .config("spark.jars.packages", "org.postgresql:postgresql:42.7.3") \
    .config("spark.hadoop.io.native.lib.available", "false") \
    .getOrCreate()

print("Reading Brazilian census CSV...")

df = spark.read \
    .option("header", "true") \
    .option("sep", ";") \
    .option("encoding", "iso-8859-1") \
    .option("inferSchema", "false") \
    .csv(DATA_PATH)

print("Raw data loaded.")
print("Available columns:")
print(df.columns)

selected_df = df.select(
    col("NU_ANO_CENSO").cast("int").alias("nu_ano_censo"),
    col("NO_UF").alias("no_uf"),
    col("SG_UF").alias("sg_uf"),
    col("NO_MUNICIPIO").alias("no_municipio"),
    col("TP_LOCALIZACAO").cast("int").alias("tp_localizacao"),
    col("IN_INTERNET").cast("int").alias("in_internet"),
    col("QT_MAT_BAS").cast("int").alias("qt_mat_bas"),
    col("QT_MAT_INF").cast("int").alias("qt_mat_inf"),
    col("QT_MAT_FUND").cast("int").alias("qt_mat_fund"),
    col("QT_MAT_MED").cast("int").alias("qt_mat_med"),
    col("QT_DOC_BAS").cast("int").alias("qt_doc_bas")
)

selected_df = selected_df.dropna(subset=["no_uf", "no_municipio"])

print("Preview of transformed Brazilian data:")
selected_df.show(10)

url = "jdbc:postgresql://127.0.0.1:5433/censo_escolar"

properties = {
    "user": "sparkuser",
    "password": "spark123",
    "driver": "org.postgresql.Driver"
}

print("Writing Brazilian data to PostgreSQL...")

selected_df.write \
    .mode("overwrite") \
    .jdbc(url=url, table="brazil_school_census", properties=properties)

print("Brazilian school census data successfully loaded into PostgreSQL!")

spark.stop()