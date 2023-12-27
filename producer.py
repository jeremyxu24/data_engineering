from kafka import KafkaProducer

bootstrap_servers = ['localhost:29092']

topicName = 'test'

# Initialize producer variable
producer = KafkaProducer(bootstrap_servers = bootstrap_servers)

# Publish text in defined topic
producer.send(topicName, b'Hello Kafka...')

print("Message Sent")