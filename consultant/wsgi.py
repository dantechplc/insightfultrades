"""
WSGI config for consultant project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from decouple import config
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'consultant.settings_pro' if config('DJANGO_ENVIRONMENT') == 'production' else 'consultant.settings_dev')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'consultant.settings')

application = get_wsgi_application()
