from kafka import KafkaConsumer

# Define server with port
bootstrap_servers = ['localhost:29092']

# Define topic name from where the message will receive
topicName = 'source.public.client'

# Initialize consumer variable
consumer = KafkaConsumer(
    topicName,
    auto_offset_reset='earliest',
    enable_auto_commit=False,  # Disable automatic offset committing
    group_id='jxu_client_group',
    bootstrap_servers=bootstrap_servers
)

try:
    # Read and print message from consumer
    for msg in consumer:
        print("Topic Name=%s, Message=%s" % (msg.topic, msg.value))
        
        # Manually commit the offset after processing each message
        consumer.commit()
        
except KeyboardInterrupt:
    print("Consumer stopped by user.")

finally:
    # Close the consumer
    consumer.close()
