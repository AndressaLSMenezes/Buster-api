from rest_framework import permissions
from rest_framework.views import Request, View
from .models import User


class Authenticated(permissions.BasePermission):
    def has_permission(self, request: Request, view: View):
        safe_methods = ["POST"]
        return request.method in safe_methods or request.user.is_authenticated


class IsOwnerOrEmployee(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj: User) -> bool:
        return request.user.is_employee or request.user == obj
