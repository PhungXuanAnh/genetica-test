import debugpy
from django.contrib.auth.backends import ModelBackend
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

class CustomAuthBackend(BasicAuthentication):
    def authenticate(self, request):
        debugpy.breakpoint()
        return super().authenticate(request)
