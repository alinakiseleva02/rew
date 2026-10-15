from channels.generic.websocket import AsyncWebsocketConsumer

class EchoConsumer(AsyncWebsocketConsumer):
    async def receive(self, text_data=None, bytes_data=None):
        parts = text_data.split(' ')
        result = int(parts[0]) + int(parts[2])
        await self.send(text_data=str(result))