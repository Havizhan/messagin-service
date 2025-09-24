from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import asyncio, aio_pika, os

RABBIT_URL = os.getenv("RABBIT_URL")  # ambil dari CloudAMQP
app = FastAPI()
connection = None
channel = None
exchange_name = "messages_exchange"

class Msg(BaseModel):
    user: str
    text: str

@app.on_event("startup")
async def startup():
    global connection, channel
    connection = await aio_pika.connect_robust(RABBIT_URL)
    channel = await connection.channel()
    await channel.declare_exchange(exchange_name, aio_pika.ExchangeType.FANOUT)

@app.on_event("shutdown")
async def shutdown():
    await connection.close()

@app.post("/publish")
async def publish(msg: Msg):
    try:
        exchange = await channel.get_exchange(exchange_name)
        await exchange.publish(
            aio_pika.Message(body=f"{msg.user}:{msg.text}".encode()),
            routing_key=""
        )
        return {"status": "ok"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
