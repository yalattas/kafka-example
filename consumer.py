from kafka import KafkaConsumer, TopicPartition
import json
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("kafka_consumer")

# Define the topic and group ID
topic = 'test_topic'
group_id = 'my-group'

# Create Kafka consumer
consumer = KafkaConsumer(
    bootstrap_servers='kafka:9092',
    auto_offset_reset='earliest',
    enable_auto_commit=False,  # Disable auto-commit of offsets
    group_id=group_id,
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

# Subscribe to the topic
consumer.subscribe([topic])

logger.info("Consumer started...")

try:
    for message in consumer:
        logger.info(f"Received message: {message.value} from partition: {message.partition}, offset: {message.offset}")
        # Commit the offset manually after processing  the message
        consumer.commit()
except Exception as e:
    logger.error(f"Error in consumer: {str(e)}")
finally:
    consumer.close()
