from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Spark Test") \
    .getOrCreate()

data = [("Bryan", 22), ("Spark", 10)]

df = spark.createDataFrame(data, ["Name", "Value"])

df.show()

spark.stop()