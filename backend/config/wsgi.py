"""
WSGI config for config project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = get_wsgi_application()
from django.contrib.auth.models import User

def create_admin():
    if not User.objects.filter(username="admin").exists():
        User.objects.create_superuser("admin", "admin@example.com", "admin123")

create_admin()
