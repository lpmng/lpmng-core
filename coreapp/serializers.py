from rest_framework import serializers
from coreapp.models import LdapUser
from coreapp.utils import hash_password


class LdapUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = LdapUser
        fields = ('uid', 'commonname', 'surname', 'mail', 'tel', 'password')
        extra_kwargs = {
            'password': {'write_only': True}  # Allow to set pwd, but disallow getting the hash from LDAP
        }

    def create(self, validated_data):
        password = validated_data.pop('password')  # Get the plain-text pwd and remove it from data to save

        # Create user with the validated_data dict along with the hashed pwd
        return LdapUser.objects.create(password=hash_password(password), **validated_data)

    def update(self, instance, validated_data):
        validated_data['password'] = hash_password(validated_data['password'])

        for attr_name,attr_value in validated_data.items():
            setattr(instance, attr_name, attr_value)

        instance.save()
        return instance
