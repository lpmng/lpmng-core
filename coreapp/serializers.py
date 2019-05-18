from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from coreapp.models import User, Session
from coreapp.utils import hash_password


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password',
                  'cotisant', 'tel', 'nbSessions', 'is_admin')
        extra_kwargs = {
            # Allow to set pwd, but disallow getting the hash
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
            'cotisant': {'read_only': True},
            'nbSession': {'read_only': True}
        }

    def validate_password(self, value: str):
        return make_password(value)


class SessionSerializer(serializers.ModelSerializer):
    internet = serializers.BooleanField(default=True)

    class Meta:
        model = Session
        fields = ('mac', 'ip4', 'user', 'internet')

    def validate_user(self, value: str):
        user = User.objects.get(username=value)
        if len(user.session_set.all()) >= user.nbSessions:  # Si user as utilisé toutes ses sessions
            raise serializers.ValidationError("Max autorised number of sessions reached")
        return user


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
