from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.response import Response
from .serializers import CustomJWTSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class UserView(APIView):
    serializer_class = CustomJWTSerializer

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class LoginView(TokenObtainPairView):
    serializer_class = CustomJWTSerializer
