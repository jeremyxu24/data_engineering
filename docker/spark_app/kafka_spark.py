from pyspark.sql import SparkSession
from pyspark.sql.functions import rand, col
import json

# Create a SparkSession
spark = SparkSession.builder \
    .appName("KafkaStreamExample") \
    .getOrCreate()

# Read data from Kafka as a streaming DataFrame
df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:29092") \
    .option("subscribe", "source.public.client") \
    .load()

# Define a schema for the Kafka messages and parse JSON data
schema = df.schema
parsed_df = df.selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)") \
    .selectExpr("from_json(value, '{}') as data".format(schema.json()))

# Apply random transformations
transformed_df = parsed_df.select(
    col("data.client_id"),
    col("data.first_name"),
    col("data.last_name"),
    col("data.email_address"),
    col("data.phone_number"),
    rand().alias("random_value")
)

# Write the transformed data to the console
query = transformed_df.writeStream \
    .outputMode("append") \
    .format("console") \
    .start()

# Wait for the query to terminate
query.awaitTermination()
