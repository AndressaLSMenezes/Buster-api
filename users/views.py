from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserSerializer, LoginSerializer
# from .models import User
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken


class UserView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(**serializer.validated_data)
        
        if not user:
            return Response({"detail": "invalid cedentials"}, status=403)
        
        refresh = RefreshToken.for_user(user)

