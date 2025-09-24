from fastapi import FastAPI
import pika, os

app = FastAPI()

RABBIT_URL = os.getenv("RABBIT_URL", "amqps://ipeodtkq:sKSFZhGtLGY7Za_TiYT1ikp0H8GXoKJP@gerbil.rmq.cloudamqp.com/ipeodtkq")

@app.get("/send/{message}")
def send_message(message: str):
    params = pika.URLParameters(RABBIT_URL)
    connection = pika.BlockingConnection(params)
    channel = connection.channel()
    channel.queue_declare(queue='chat', durable=True)
    channel.basic_publish(exchange='', routing_key='chat', body=message)
    connection.close()
    return {"status": "sent", "message": message}
