from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from .serializers import MovieSerializer, MovieOrderSerializer
from .models import Movie
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import (
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
    IsAuthenticated,
)
from django.shortcuts import get_object_or_404


class MovieView(APIView, PageNumberPagination):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly, IsAdminUser]

    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def get(self, request):
        movies = Movie.objects.all()
        paginated_movies = self.paginate_queryset(movies, request, view=self)
        serializer = MovieSerializer(paginated_movies, many=True)
        return self.get_paginated_response(serializer.data)


class MovieDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser, IsAuthenticatedOrReadOnly]

    def get(self, request, movie_id):
        movie = get_object_or_404(Movie, pk=movie_id)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

    def delete(self, request, movie_id):
        movie = get_object_or_404(Movie, pk=movie_id)

        movie.delete()
        return Response(status=204)


class MovieOrderView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, movie_id):
        movie = get_object_or_404(Movie, pk=movie_id)
        serializer = MovieOrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(movie=movie, user=request.user)
        return Response(serializer.data, status=201)
