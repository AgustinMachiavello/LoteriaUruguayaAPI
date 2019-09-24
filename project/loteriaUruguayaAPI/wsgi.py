"""
WSGI config for loteriaUruguayaAPI project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os
from django.dispatch import receiver
from django.db.backends.signals import connection_created
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'loteriaUruguayaAPI.settings.production')

application = get_wsgi_application()


@receiver(connection_created)
def setup_postgres(connection, **kwargs):
	if connection.vendor != 'postgresql':
		return

	# Timeout statements after 30 seconds.
	with connection.cursor() as cursor:
		cursor.execute("""
            SET statement_timeout TO 30000;
        """)