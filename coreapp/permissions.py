from rest_framework import permissions


class IsSelfOrStaffPermission(permissions.BasePermission):
    """
    Permission to allow user actions on his own profile
    """

    def has_object_permission(self, request, view, obj):
        return obj == request.user or request.user.is_staff
