from rest_framework import serializers
from .models import Movie, Ratings


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(max_length=10, required=False)
    rating = serializers.ChoiceField(
        max_length=20, choices=Ratings.choices, default=Ratings.G
    )
    synopsis = serializers.CharField(required=False)
    added_by = serializers.CharField(read_only=True)

    def create(self, validated_data: dict) -> Movie:
        return Movie.objects.create(**validated_data)
