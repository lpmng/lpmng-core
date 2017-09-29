from rest_framework import serializers
from coreapp.models import LdapUser


class LdapUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = LdapUser
        fields = ('uid', 'commonname', 'surname', 'mail', 'tel')
