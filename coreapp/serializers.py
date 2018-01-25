from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from coreapp.models import User
from coreapp.utils import hash_password


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email',
                  'password', 'cotisant', 'tel', 'nbSessions')
        extra_kwargs = {
            # Allow to set pwd, but disallow getting the hash from LDAP
            'password': {'write_only': True}
        }

    def validate_password(self, value: str):
        return make_password(value)


class SelfUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email',
                  'password', 'cotisant', 'tel', 'nbSessions')
        extra_kwargs = {
            'password': {'write_only': True},
            'username': {'read_only': True},
            'cotisant': {'read_only': True}
        }

    def validate_password(self, value: str):
        return make_password(value)


"""
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
        return instance"""
