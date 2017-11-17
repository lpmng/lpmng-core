from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from coreapp.models import LdapUser, LdapGroup
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


class LdapGroupView(APIView):
    def patch(self, request, uid, format=None):
        group_object = LdapGroup.objects.get(name="userkun")

        user_dn = "uid=" + uid + ",ou=people,dc=air-eisti,dc=fr"
        has_access = request.data['access']

        if user_dn not in group_object.members and has_access:
            group_object.members.append(user_dn)
        elif user_dn in group_object.members and not has_access:
            group_object.members.remove(user_dn)

        group_object.save()

        return Response(request.data, status=status.HTTP_200_OK)

    def get(self, request, uid, format=None):
        user_dn = "uid=" + uid + ",ou=people,dc=air-eisti,dc=fr"
        has_access = user_dn in LdapGroup.objects.get(name="userkun").members

        return Response({'has_access':has_access}, status=status.HTTP_200_OK)
