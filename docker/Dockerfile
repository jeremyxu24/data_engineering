# Use the base Spark image
FROM docker.io/bitnami/spark:3.5

# Install the Kafka package as part of the image build
RUN /opt/bitnami/spark/bin/spark-shell --packages org.apache.spark:spark-streaming-kafka-0-8_2.12:3.5
