from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from django.db import models

# from django.contrib.auth.models import User
# from django.conf import settings
from .models import CustomUser
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password

from a_project.settings import AUTH_USER_MODEL

# Register serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("id", "email", "password")
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def create(self, validated_data):
        user = CustomUser.objects.create_user(email=validated_data["email"], password=validated_data["password"])
        return user


# User serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"


# from rest_framework import serializers
# from .models import CustomUser


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomUser
#         fields = "__all__"
