from rest_framework import generics
from .serializers import PackageRequestSerializer
from .models import PackageRequest
from .permissions import IsOwnerOrReadOnly


class PackageRequestList(generics.ListCreateAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = PackageRequest.objects.all()
    serializer_class = PackageRequestSerializer


class PackageRequestDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = PackageRequest.objects.all()
    serializer_class = PackageRequestSerializer
