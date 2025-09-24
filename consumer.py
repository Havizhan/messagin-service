from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pika, os, threading

app = FastAPI()

# Allow CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

RABBIT_URL = os.getenv("RABBIT_URL", "amqps://ipeodtkq:sKSFZhGtLGY7Za_TiYT1ikp0H8GXoKJP@gerbil.rmq.cloudamqp.com/ipeodtkq")
messages = []

def consume():
    params = pika.URLParameters(RABBIT_URL)
    connection = pika.BlockingConnection(params)
    channel = connection.channel()
    channel.queue_declare(queue="chat", durable=True)

    def callback(ch, method, properties, body):
        msg = body.decode()
        print("Received:", msg)
        messages.append(msg)

    channel.basic_consume(queue="chat", on_message_callback=callback, auto_ack=True)
    channel.start_consuming()

threading.Thread(target=consume, daemon=True).start()

@app.get("/receive")
def get_messages():
    return {"messages": messages}
