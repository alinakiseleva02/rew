from channels.routing import URLRouter
from django.urls import path
from .consumers import EchoConsumer

router = URLRouter([
    path('ws/echo', EchoConsumer.as_asgi())
])