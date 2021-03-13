import logging
from music.paginations.custom_paginations import StandardResultsSetPagination, CustomPagination
from rest_framework import generics, filters
from music.models import Musician, Album

from music.serializers.model_serializers import MusicianModelSerializer
from music.serializers.serializers import MusicianSerializer

class MusicListCreateView(generics.ListCreateAPIView):
    queryset = Musician.objects.all()
    serializer_class = MusicianModelSerializer
    # serializer_class = MusicianSerializer
    # permission_classes = [permissions.IsAuthenticated]
    
    # pagination_class = StandardResultsSetPagination
    pagination_class = CustomPagination


class MusicRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Musician.objects.all()
    serializer_class = MusicianModelSerializer
    # serializer_class = MusicianSerializer
    lookup_field = "id"
    # permission_classes = [permissions.IsAuthenticated]


class MusicRetrieveFullNameView(generics.RetrieveAPIView):
    queryset = Musician.objects.all()
    serializer_class = MusicianModelSerializer
    lookup_field = "id"
    # permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        response = self.retrieve(request, *args, **kwargs)
        firt_name = response.data["first_name"]
        last_name = response.data["last_name"]
        response.data = {"full_name": firt_name + " " + last_name}
        return response
