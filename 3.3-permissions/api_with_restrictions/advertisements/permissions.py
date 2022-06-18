
from rest_framework.permissions import BasePermission

class IsOwnerOrReadOnly(BasePermission):
    # def has_permission(self, request, view):
    def has_object_permission(self, request, view, objects):

        if request.metod == 'GET':
            return True
        return request.user == object.creator or request.user.is_superuser



