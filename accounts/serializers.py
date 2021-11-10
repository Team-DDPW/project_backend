from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import  serializers
from rest_framework.permissions import IsAuthenticated
from django.db import models
# from django.contrib.auth.models import User
# from django.conf import settings
from .models import CustomUser
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password

from a_project.settings import AUTH_USER_MODEL


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        # fields = ('id','email','password')
        fields = '__all__'

        extra_kwargs = {
            'password':{'write_only': True},
        }
    def create(self, validated_data):
        user = CustomUser.objects.create_user(email = validated_data['email'], password = validated_data['password'])
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['email'] = user.email
        token['id'] = user.id
        return token
