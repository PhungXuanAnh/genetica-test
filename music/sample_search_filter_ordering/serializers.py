from rest_framework import serializers
from music.models import Musician, Instrument, Profile
from music.serializers.model_serializers import ProfileModelSerializer


class MusicianModelSerializer_search_filter_ordering(serializers.ModelSerializer):
    profile = ProfileModelSerializer()
    class Meta:
        model = Musician
        fields = ['id', 'first_name', 'last_name', 'email', 'profile']