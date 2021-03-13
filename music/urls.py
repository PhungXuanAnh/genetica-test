from django.urls import include, path, re_path
from rest_framework import routers

from music.views import model_viewsets as music_model_viewsets
from music.views import generic_views as music_generic_views
from music.views import api_views as music_api_views
from music.sample_debug_views_serializers import debug_views as music_debug_views
from music.sample_using_serializer_effective import viewsets as read_affective
from music.sample_search_filter_ordering import viewsets as sample_search_filter_ordering_views

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'musican-viewset', music_model_viewsets.MusicianModelViewSet, basename='musican-viewset')
router.register(r'musican-debug', music_debug_views.MusicianModelDebugViewSet, basename='musican-debug')
router.register(r'musican-using-serializer-affective-source-keyword', read_affective.MusicianModelReadEffective_SourceKeyword_ViewSet, basename='musican-using-serializer-affective-source-keyword')
router.register(r'musican-using-serializer-affective-serializer-method', read_affective.MusicianModelReadEffective_SerializerMethod_ViewSet, basename='musican-using-serializer-affective-serializer-method')

router.register(r'musican-sample-ordering', sample_search_filter_ordering_views.MusicanListRetriveViews_Ordering, basename='musican-sample-ordering')
router.register(r'musican-sample-search', sample_search_filter_ordering_views.MusicanListRetriveViews_Search, basename='musican-sample-search')
router.register(r'musican-sample-filter', sample_search_filter_ordering_views.MusicanListRetriveViews_Fitler, basename='musican-sample-filter')
router.register(r'musican-sample-filter-search-ordering', sample_search_filter_ordering_views.MusicianListRetriveViews_Filter_Search_Order, basename='musican-sample-filter-search-ordering')

urlpatterns = [
    path(r'musican-api-views', music_api_views.CreateListMusicanView.as_view(), name='api_view_list_musican'),
    path(r'musican-api-views/<id>', music_api_views.MusicanRetriveUpdateDestroyView.as_view(), name='api_view_getputpatchdelete_musican'),
    path(r'musican-api-views/<id>/sample-action', music_api_views.MusicanFullNameView.as_view(), name='api_view_full_name_musican'),

    path(r'musican-generic-views', music_generic_views.MusicListCreateView.as_view(), name='list_create_musican'),
    path(r'musican-generic-views/<id>', music_generic_views.MusicRetrieveUpdateDestroyView.as_view(), name='get_musican'),
    path(r'musican-generic-views/<id>/sample-action', music_generic_views.MusicRetrieveFullNameView.as_view(), name='get_musican_full_name'),
    
    re_path(r'^', include(router.urls))
]

