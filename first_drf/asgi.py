"""
ASGI config for first_drf project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.1/howto/deployment/asgi/
"""

import os
from channels.routing import ProtocolTypeRouter
from django.core.asgi import get_asgi_application
from first_def_app.websocket_routing import router

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_drf.settings')

django_app = get_asgi_application()

application = ProtocolTypeRouter({
    'http': django_app,
    'websocket': router,
})

# django channels unicorn[standard]