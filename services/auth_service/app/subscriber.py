import asyncio
from cache import redis_client


async def handle_message():
    pubsub = redis_client.pubsub()
    await pubsub.subscribe('notifications')
    print("Подписан на канал 'notifications'...")

    async for message in pubsub.listen():
        if message['type'] == 'message':
            print(f"Получено сообщение: {message['data']}")


if __name__ == '__main__':
    asyncio.run(handle_message())
