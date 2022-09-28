from ast import Return
from lib2to3.pytree import Base
from urllib import request
from rest_framework.permissions import BasePermission
from rest_framework import permissions

class UpdateSelfProfile(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id