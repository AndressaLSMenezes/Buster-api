from rest_framework import serializers
from .models import Movie, Ratings, MovieOrder


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    duration = serializers.CharField(required=False)
    rating = serializers.ChoiceField(choices=Ratings.choices, default=Ratings.G)
    synopsis = serializers.CharField(required=False)
    added_by = serializers.CharField(read_only=True)

    def create(self, validated_data: dict) -> Movie:
        return Movie.objects.create(**validated_data)


class MovieOrderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(read_only=True)
    buyed_by = serializers.EmailField(read_only=True)
    buyed_at = serializers.DateTimeField(read_only=True)
    price = serializers.DecimalField(max_digits=8, decimal_places=2)

    def create(self, validated_data: dict) -> MovieOrder:
        return MovieOrder.objects.create(**validated_data)
