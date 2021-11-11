from rest_framework import generics  # permissions
from rest_framework.response import Response
from .serializers import RegisterSerializer, UserSerializer


from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny
from .serializers import MyTokenObtainPairSerializer


class RegisterApi(generics.GenericAPIView):
    # permission_classes = (permissions.AllowAny)
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(
            {
                "user": UserSerializer(user, context=self.get_serializer_context()).data,
                "message": "User Created Successfully.  Now perform Login to get your token",
            }
        )


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer
