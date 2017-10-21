from rest_framework import serializers
from coreapp.models import LdapUser
from coreapp.utils import hash_password


class LdapUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = LdapUser
        fields = ('uid', 'commonname', 'surname', 'mail', 'tel', 'password')
        extra_kwargs = {
            # Allow to set pwd, but disallow getting the hash from LDAP
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        # Get the plain-text pwd and remove it from data to save
        password = validated_data.pop('password')

        # Create user with the validated_data dict along with the hashed pwd
        return LdapUser.objects.create(
            password=hash_password(password), **validated_data)

    def update(self, instance, validated_data):
        validated_data['password'] = hash_password(validated_data['password'])

        for attr_name, attr_value in validated_data.items():
            setattr(instance, attr_name, attr_value)

        instance.save()
        return instance
