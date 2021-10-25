from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import User1


class UserSerializer(serializers.ModelSerializer):
    """ Serializer for User Model """
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User1.objects.all())]
    )
    username = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=User1.objects.all())]
    )

    class Meta:
        model = User1
        fields = ('email', 'username', 'password', 'first_name', 'last_name', 'city',
                  'contact', 'Address', 'city', 'education', "user_roles", "id")
        read_only_fields = ["updated_date", "created_date", "id", "is_superuser",
                            "is_staff", "is_active"]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validate_data):
        """ creating user with the validated_data """
        return User1.objects.create_user(**validate_data)


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User1.objects.all())]
    )
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    id = serializers.CharField(read_only=True)

    class Meta:
        model = User1
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name', 'id')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User1.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class LogInSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super(LogInSerializer, cls).get_token(user)

        token['username'] = user.username
        token['password'] = user.password
        return token
