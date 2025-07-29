from redis import asyncio as redis
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path="../../infra/.env")

REDIS_HOTS = os.getenv("REDIS_HOST", 'localhost')
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))

redis_client = redis.Redis(
    host='REDIS_HOST', port='REDIS_PORT', decode_responses=True)


async def publish_notification(channel: str, message: str):
    await redis_client.publish(channel, message)
