"""
ASGI config for websocket_echo project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from channels.routing import ProtocolTypeRouter
from django.core.asgi import get_asgi_application
import echo.routing
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "websocket_echo.settings")

application = ProtocolTypeRouter({
    "http":get_asgi_application(),
    "websocket": AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter(
                echo.routing.websocket_urlpatterns
            )
        )
    )
})
