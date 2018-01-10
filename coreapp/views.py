from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from coreapp.models import User
from coreapp.serializers import UserSerializer
from django.db.models import Q


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    lookup_field = 'username'

    def get_queryset(self):
        query = self.request.query_params.get('q', None)

        if not query:
            return User.objects.all()

        return User.objects.filter(
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
