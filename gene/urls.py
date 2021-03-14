from django.urls import include, re_path
from rest_framework import routers

from gene.views import GenelViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'gene', GenelViewSet, basename='gene')

urlpatterns = [
    re_path(r'^', include(router.urls))
]

