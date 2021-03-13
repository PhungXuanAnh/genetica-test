import debugpy
from rest_framework import permissions

class CustomPermission(permissions.IsAuthenticated):
    def has_permission(self, request, view):
        debugpy.breakpoint()
        return super().has_permission(request, view)