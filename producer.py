from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from kafka import KafkaProducer
import json
import os

app = FastAPI()

class Message(BaseModel):
    content: str

producer = KafkaProducer(
    bootstrap_servers='kafka:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)
topic = os.environ.get('KAFKA_TOPIC', default='test_topic')

@app.post("/produce/")
async def produce(message: Message):
    try:
        producer.send(topic, value={'message': message.content})
        # producer.flush()
        return {"status": "Message scheduled successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
@app.post("/send/")
async def produce():
    producer.flush() # it will make client wait till it make sure that message is delivered
    return {"status": "Message sent"}