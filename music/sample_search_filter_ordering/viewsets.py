import logging
from django_filters.rest_framework import DjangoFilterBackend
from django_filters.rest_framework import filters, filterset
from rest_framework import viewsets, filters as rest_filters
from rest_framework import mixins

from music.models import Musician
from music.sample_search_filter_ordering.serializers import MusicianModelSerializer_search_filter_ordering



logger = logging.getLogger('django')

class CustomSearchFilter(rest_filters.SearchFilter):
    def get_search_fields(self, view, request):
        if request.query_params.get('last_name_only'):
            return ['=last_name']
        return super(CustomSearchFilter, self).get_search_fields(view, request)


class MusicanFilter(filterset.FilterSet):
    min_num_stars = filters.NumberFilter(field_name="profile__num_stars", lookup_expr='gte')
    max_num_stars = filters.NumberFilter(field_name="profile__num_stars", lookup_expr='lte')

    class Meta:
        model = Musician
        fields = ['first_name', 'last_name', 'min_num_stars', 'max_num_stars']

class MusicanListRetriveViews_Ordering(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Musician.objects.all()
    serializer_class = MusicianModelSerializer_search_filter_ordering
    filter_backends = [rest_filters.OrderingFilter]
    ordering_fields = ['last_name', 'first_name', 'email']
    ordering = ['email']    # default field for ordering


class MusicanListRetriveViews_Search(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Musician.objects.all()
    serializer_class = MusicianModelSerializer_search_filter_ordering
    # filter_backends = [rest_filters.SearchFilter]
    filter_backends = [CustomSearchFilter]
    search_fields = ['=first_name', '=last_name', '=email', '=profile__city']


class MusicanListRetriveViews_Fitler(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Musician.objects.all()
    serializer_class = MusicianModelSerializer_search_filter_ordering
    filter_backends = [DjangoFilterBackend]
    filterset_class = MusicanFilter     # NOTE: using filterset_class cannot show filter field in swagger, only filterset_fields work
    # filterset_fields = ['first_name', 'last_name']  # --> this is shortcut of filterset_class, use it if not add more fields: min_num_stars, max_num_stars
    #                                                 # this more here: https://django-filter.readthedocs.io/en/latest/guide/rest_framework.html#adding-a-filterset-with-filterset-class

class MusicianListRetriveViews_Filter_Search_Order(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Musician.objects.all()
    serializer_class = MusicianModelSerializer_search_filter_ordering
    filter_backends = [DjangoFilterBackend, CustomSearchFilter]
    filterset_class = MusicanFilter
    search_fields = ['=first_name', '=last_name', '=email', '=profile__city']
    ordering_fields = ['last_name', 'first_name', 'email']
    ordering = ['email']    # default field for ordering
