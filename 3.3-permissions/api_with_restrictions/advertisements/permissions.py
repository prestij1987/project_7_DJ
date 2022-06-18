
from rest_framework.permissions import BasePermission

class IsOwner(BasePermission):
    # def has_permission(self, request, view):
    def has_object_permission(self, request, view, objects):
        return request.user == user.objects



