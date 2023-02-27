from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import MovieSerializer
from .models import Movie
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly


class MovieView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly, IsAdminUser]

    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(added_by=request.user.email)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer)


class MovieDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser, IsAuthenticatedOrReadOnly]

    def get(self, request, movie_id):
        try:
            movie = Movie.objects.get(pk=movie_id)
        except Movie.DoesNotExist:
            return Response({"detail": "Not found."}, status=404)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

    def delete(self, request, movie_id):
        try:
            movie = Movie.objects.get(pk=movie_id)
        except Movie.DoesNotExist:
            return Response({"detail": "Not found."}, status=404)
        movie.delete()
        return Response(status=204)
