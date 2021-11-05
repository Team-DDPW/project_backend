from rest_framework import serializers
from .models import PackageRequest


class PackageRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = PackageRequest
        fields = "__all__"
