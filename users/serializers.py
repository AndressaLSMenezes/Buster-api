from rest_framework import serializers
from .models import User

# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField()
    email = serializers.CharField(max_length=127)
    password = serializers.CharField(max_length=127, write_only=True)
    birthdate = serializers.DateField(allow_null=True, default=None)
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    is_employee = serializers.BooleanField(required=False)
    is_superuser = serializers.BooleanField(read_only=True)

    def create(self, validated_data: dict) -> User:
        if validated_data.get("is_employee"):
            return User.objects.create_superuser(**validated_data)
        else:
            return User.objects.create_user(**validated_data)
