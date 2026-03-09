import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api.settings')
django.setup()

from django.contrib.auth.models import User

# Delete existing admin if any
User.objects.filter(username='admin').delete()

# Create new admin user
user = User.objects.create_superuser('admin', 'admin@example.com', 'admin')
print(f"Superuser 'admin' created with password 'admin'. Is_staff: {user.is_staff}, Is_superuser: {user.is_superuser}")
