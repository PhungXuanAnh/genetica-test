from django.urls import include, path, re_path
from rest_framework import routers

from user import views as user_views

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'users', user_views.UserViewSet)
router.register(r'groups', user_views.GroupViewSet)

urlpatterns = [
    re_path(r'^', include(router.urls))
]
