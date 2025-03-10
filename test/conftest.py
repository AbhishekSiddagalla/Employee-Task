import os
from pathlib import Path

# For pytest-django, set the DJANGO_SETTINGS_MODULE to the test-specific settings.
os.environ['DJANGO_SETTINGS_MODULE'] = 'Employee_Project.settings_test'

# Path to your project root directory
BASE_DIR = Path(__file__).resolve().parent.parent

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ":memory:",
    }
}

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Employee_Note',
]


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
