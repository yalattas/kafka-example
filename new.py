from kafka import KafkaConsumer
import json
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("kafka_consumer")

consumer = KafkaConsumer(
    'test_topic',
    bootstrap_servers='kafka:9092',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my-group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

logger.info("Consumer started...")

try:
    for message in consumer:
        logger.info(f"Received message: {message.value}")
except Exception as e:
    logger.error(f"Error in consumer: {str(e)}")
