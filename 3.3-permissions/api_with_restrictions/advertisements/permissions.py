
from rest_framework.permissions import BasePermission

class IsOwner(BasePermission):
    # def has_permission(self, request, view):
    def has_object_permission(self, request, view, objects):
        return request.user == object.creator or request.user.is_superuser



