from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Simple Spark app").master("local[2]").getOrCreate()

print("=======================")
print(f"Application name: {spark.sparkContext.appName}")
print(f"Spark version: {spark.version}")
print("=======================")

spark.stop()
