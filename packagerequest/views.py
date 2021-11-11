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

# from .serializers import PackageRequestSerializer
# from .models import PackageRequest
# from rest_framework.views import APIView
# from rest_framework.parsers import MultiPartParser, FormParser
# from rest_framework.response import Response
# from rest_framework import status
# # Create your views here.

# class PackageRequestView(APIView):
#     parser_classes = (MultiPartParser, FormParser)

#     def get(self, request, *args, **kwargs):
#         packageRequests = PackageRequest.objects.all()
#         serializer = PackageRequestSerializer(packageRequests, many=True)
#         return Response(serializer.data)

#     def packageRequest(self, request, *args, **kwargs):
#         packageRequests = PackageRequestSerializer(data=request.data)
#         if packageRequests_serializer.is_valid():
#             packageRequests_serializer.save()
#             return Response(packageRequests_serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             print('error', packageRequests_serializer.errors)
#             return Response(packageRequests_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
