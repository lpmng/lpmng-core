from rest_framework import viewsets
from coreapp.models import LdapUser
from coreapp.serializers import LdapUserSerializer


class LdapUserViewSet(viewsets.ModelViewSet):
    queryset = LdapUser.objects.all()
    serializer_class = LdapUserSerializer
