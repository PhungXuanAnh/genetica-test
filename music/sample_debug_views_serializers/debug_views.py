from music.paginations.custom_paginations import CustomPagination
import debugpy
import django_filters
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from music.models import Musician, Album
from .debug_model_serializers import MusicianModelDebugSerializer

from main.custom_authentications import CustomAuthBackend
from main.custom_permissions import CustomPermission

def my_queryset():
    debugpy.breakpoint()
    return Musician.objects.all()


class MusicianModelDebugViewSet(viewsets.ModelViewSet):
    # http_method_names = ["post"]
    queryset = Musician.objects.all()
    serializer_class = MusicianModelDebugSerializer
    authentication_classes = [CustomAuthBackend]
    permission_classes = [CustomPermission]
    pagination_class = CustomPagination
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]

    # --------------- APIView method ---------------------
    def get_parsers(self):
        debugpy.breakpoint()
        return super().get_parsers()

    def get_authenticators(self):
        debugpy.breakpoint()
        return super().get_authenticators()

    def get_permissions(self):
        debugpy.breakpoint()
        return super().get_permissions()

    def get_throttles(self):
        debugpy.breakpoint()
        return super().get_throttles()

    def get_paginated_response(self, data):
        debugpy.breakpoint()
        return super().get_paginated_response(data)

    # def check_permissions(self, request):
    #     debugpy.breakpoint()
    #     return super().check_permissions(request)

    # def check_throttles(self, request):
    #     debugpy.breakpoint()
    #     return super().check_throttles(request)

    # --------------- GenericView method ---------------------
    def get_object(self):
        debugpy.breakpoint()
        return super().get_object()

    def get_queryset(self):
        debugpy.breakpoint()
        return super().get_queryset()

    def filter_queryset(self, queryset):
        debugpy.breakpoint()
        return super().filter_queryset(queryset)

    # def get_permissions(self)

    def get_serializer_class(self):
        debugpy.breakpoint()
        return super().get_serializer_class()

    def paginate_queryset(self, queryset):
        debugpy.breakpoint()
        return super().paginate_queryset(queryset)

    # ---------------------------------------------------
    def retrieve(self, request, *args, **kwargs):
        debugpy.breakpoint()
        return super().retrieve(request, *args, **kwargs)
    
    def create(self, request, *args, **kwargs):
        debugpy.breakpoint()
        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        debugpy.breakpoint()
        return super().perform_create(serializer)

    def list(self, request, *args, **kwargs):
        debugpy.breakpoint()
        return super().list(request, *args, **kwargs)




