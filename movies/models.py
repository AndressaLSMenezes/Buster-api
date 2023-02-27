from django.db import models
from users.models import User


class Ratings(models.TextChoices):
    G = "G"
    PG = "PG"
    PG_13 = "PG-13"
    R = "R"
    NC_17 = "NC-17"


class Movie(models.Model):
    title = models.CharField(max_length=127)
    duration = models.CharField(max_length=10, blank=True, null=True)
    rating = models.CharField(max_length=20, choices=Ratings.choices, default=Ratings.G)
    synopsis = models.TextField(blank=True, null=True)
    added_by = models.EmailField()
    users = models.ManyToManyField(User, through="MovieOrder", related_name="movies")


class MovieOrder(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    buyed_at = models.DateTimeField(auto_now_add=True)
    buyed_by = models.EmailField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
