# pylint: disable=protected-access
# pylint: disable=broad-except
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "main.settings")
django.setup()

# pylint: disable=wrong-import-position
from django.contrib.auth.models import User
from music.models import Album, Musician, Profile
import datetime

musican = Musician.objects.get(id=1)
print(musican.album_set.all())
