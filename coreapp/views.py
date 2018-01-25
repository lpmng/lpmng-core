from rest_framework import viewsets, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from coreapp.models import User
from coreapp.serializers import UserSerializer, SelfUserSerializer
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope
from django.db.models import Q

import coreapp.permissions


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = (coreapp.permissions.IsAdminUserOrCreate,
                          coreapp.permissions.TokenHasReadWriteScopeOrCreate,)
    lookup_field = 'username'

    def create(self, request, *args, **kwargs):
        """
        Anyone can create a new user, but only staff can
        set the new user `cotisant` attribute to something
        different than `False` and `nbSession` than `0`
        """
        if not request.user.is_staff:
            request.data._mutable = True  # request.data is a immutable QueryDict instance at creat°
            request.data['cotisant'] = 'False'  # We make sure `cotisant` is set to False
            request.data['nbSessions'] = '0'  # Same for nbSessions
            request.data._mutable = False

        return super().create(request, args, kwargs)  # Call the original create with the new params

    def get_queryset(self):
        user_set = User.objects.all()

        query = self.request.query_params.get('q', None)

        if not query:
            return user_set

        return user_set.filter(
            Q(username__icontains=query) |
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query)
        )


class SelfView(generics.RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated, TokenHasReadWriteScope,)
    serializer_class = SelfUserSerializer

    def get_object(self):
        return self.request.user


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
