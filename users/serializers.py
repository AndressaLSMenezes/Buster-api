from rest_framework import serializers
from .models import User
from django.db import IntegrityError


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField()
    email = serializers.CharField()
    password = serializers.CharField(write_only=True)
    birthdate = serializers.DateField(required=False)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    is_employee = serializers.BooleanField(required=False)
    is_superuser = serializers.BooleanField(read_only=True)

    def create(self, validated_data: dict) -> User:
        if validated_data.get("is_employee"):
            try:
                return User.objects.create_superuser(**validated_data)
            except IntegrityError as err:
                print("OIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII")
                print(err)
                # return err
        else:
            try:
                return User.objects.create_user(**validated_data)
            except IntegrityError as err:
                print("OI22222222222222222222222222222222222222222")
                print(err)
                # return err
