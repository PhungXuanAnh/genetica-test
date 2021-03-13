from rest_framework import serializers
from music.models import Musician, Instrument, Profile


class ProfileModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['age', 'street', 'city', 'num_stars']

class InstrumentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instrument
        fields = ['id', 'name']


class MusicianModelSerializer(serializers.ModelSerializer):
    instruments = InstrumentModelSerializer(read_only=True, many=True)
    profile = ProfileModelSerializer()
    class Meta:
        model = Musician
        fields = ['id', 'first_name', 'last_name', 'email', 'instruments', 'profile']