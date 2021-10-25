from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer, RegisterSerializer, LogInSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework_simplejwt.views import TokenObtainPairView
from .TokenGenrator import token_validator

from .models import User1


class CreateUser(ListCreateAPIView):
    """ class developed for getting & creating the by a Authorized
        user using UserSerializer class"""

    permission_classes = (AllowAny,)
    serializer_class = UserSerializer
    queryset = User1.objects.all()


class UpdateUser(RetrieveUpdateDestroyAPIView):
    """ class to Get & Update & DELETE by ID and using
     UserSerializer class"""

    permission_classes = (AllowAny,)
    serializer_class = UserSerializer
    queryset = User1.objects.all()


class RegisterView(CreateAPIView):

    """ A User Register class  """

    queryset = User1.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class LogInView(TokenObtainPairView):
    """ USER login  """
    serializer_class = LogInSerializer


class LogoutView(APIView):
    """   User Logout
        :key refresh_token
        :return status.HTTP_205_RESET_CONTENT
    """
    permission_classes = (AllowAny,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class VerifyEmail(APIView):
    """verify the email using user_id
        :param token
        :return status 200 ok
    """

    def get(self, request, token):
        user = token_validator(token)
        if user:
            User1.objects.filter(id=user['id']).update(is_verified=True)
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
