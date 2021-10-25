from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer, RegisterSerializer, LogInSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import User1


class CreateUser(ListCreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer
    queryset = User1.objects.all()


class UpdateUser(RetrieveUpdateDestroyAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer
    queryset = User1.objects.all()


class RegisterView(CreateAPIView):
    queryset = User1.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class LogInView(TokenObtainPairView):
    serializer_class = LogInSerializer


class LogoutView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
