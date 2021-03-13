from django.db import models
from django.contrib.auth.models import Group, User



class Instrument(models.Model):
    name = models.CharField(max_length=100)

class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instruments = models.ManyToManyField(Instrument)
    email = models.EmailField()
    password = models.CharField(max_length=500)

    def get_full_name(self):
        return self.first_name + " " + self.last_name

class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()

class Profile(models.Model):
    user = models.OneToOneField(Musician, on_delete=models.CASCADE)
    age = models.IntegerField(default=0)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    num_stars = models.IntegerField()

    def get_full_address(self):
        return "%s, %s" % (self.street, self.city)
