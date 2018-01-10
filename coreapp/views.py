from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from coreapp.models import User
from coreapp.serializers import UserSerializer
from coreapp.permissions import IsSelfOrStaffPermission
from django.db.models import Q


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = (IsSelfOrStaffPermission,)
    lookup_field = 'username'

    def get_queryset(self):
        current_user = self.request.user
        if current_user.is_staff:
            user_set = User.objects.all()
        else:
            user_set = User.objects.filter(username=current_user.username)

        query = self.request.query_params.get('q', None)

        if not query:
            return user_set

        return user_set.filter(
            Q(username__icontains=query) |
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query)
        )


"""
class LdapUserViewSet(viewsets.ModelViewSet):
    serializer_class = LdapUserSerializer

    def get_queryset(self):
        query = self.request.query_params.get('q', None)

        if not query:
            return LdapUser.objects.all()

        return LdapUser.objects.filter(
            Q(uid__icontains=query) |
            Q(commonname__icontains=query) |
            Q(surname__icontains=query)
        )"""
