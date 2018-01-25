from rest_framework import permissions
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope


class IsSelfOrStaffPermission(permissions.BasePermission):
    """
    Permission to allow user actions on his own profile
    """
    def has_object_permission(self, request, view, obj):
        return obj == request.user or request.user.is_staff


class IsAdminUserOrCreate(permissions.IsAdminUser):
    def has_permission(self, request, view):
        return view.action == "create" or super().has_permission(request, view)


class TokenHasReadWriteScopeOrCreate(TokenHasReadWriteScope):
    """
    Permission to create user for anyone or check if TokenHasReadWriteScope
    """
    def has_permission(self, request, view):
        return view.action == "create" or super().has_permission(request, view)
