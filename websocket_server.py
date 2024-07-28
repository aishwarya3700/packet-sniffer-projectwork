import asyncio
import websockets

clients = set()

async def handle_client(websocket):
    async for message in websocket:
        for client in clients:
            if client != websocket:
                await client.send(message)
    clients.remove(websocket)

async def main():
    async with websockets.serve(handle_client, "localhost", 8000):
        print("WebSocket server started")

asyncio.run(main())
