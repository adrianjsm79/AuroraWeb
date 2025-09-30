import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Location
from django.contrib.auth.models import User

class MapConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("map", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("map", self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        username = data["user"]
        lat = data["lat"]
        lon = data["lon"]

        # Guardar en la BD usando ORM
        user = User.objects.get(username=username)
        Location.objects.update_or_create(
            user=user,
            defaults={"latitude": lat, "longitude": lon}
        )

        # Enviar a todos en tiempo real
        await self.channel_layer.group_send(
            "map",
            {
                "type": "location_update",
                "user": username,
                "lat": lat,
                "lon": lon,
            }
        )

    async def location_update(self, event):
        await self.send(text_data=json.dumps(event))
