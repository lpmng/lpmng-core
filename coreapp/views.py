from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from coreapp.models import LdapUser
from coreapp.serializers import LdapUserSerializer
from django.db.models import Q


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
        )
