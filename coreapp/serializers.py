import hashlib
from base64 import b64encode

from rest_framework import serializers
from coreapp.models import LdapUser


class LdapUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = LdapUser
        fields = ('uid', 'commonname', 'surname', 'mail', 'tel', 'password')
        extra_kwargs = {
            'password': {'write_only': True}  # Allow to set pwd, but disallow getting the hash from LDAP
        }

    def create(self, validated_data):
        password = validated_data.pop('password')  # Get the plain-text pwd and remove it from data to save
        hashed = hashlib.sha1(password.encode('utf-8')).digest()
        hashed_string = "{SHA}" + b64encode(hashed).decode()    # Password string formated for LDAP client

        # Create user with the validated_data dict along with the hashed pwd
        return LdapUser.objects.create(password=hashed_string, **validated_data)
