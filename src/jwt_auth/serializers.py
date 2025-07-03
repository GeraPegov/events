from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import AuthorizationModel

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorizationModel
        fields = ['login', 'password']
    def create(self, validated_data):
        user = AuthorizationModel.objects.create(
            login = validated_data['login'],
            password = make_password(validated_data['password'])
        )
        return user

class LoginSerializer(serializers.Serializer):
    login = serializers.CharField()
    password = serializers.CharField(write_only=True)
    def validate(self, data):
        return data

class RefreshTokenSerializer(serializers.Serializer):
    refresh_token = serializers.CharField()