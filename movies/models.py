from django.db import models

# Create your models here.


class Ratings(models.TextChoices):
    G = "G"
    PG = "PG"
    PG_13 = "PG-13"
    R = "R"
    NC_17 = "NC-17"


class Movie(models.Model):
    title = models.CharField(max_length=127)
    duration = models.CharField(max_length=10, default=None)
    rating = models.CharField(max_length=20, choices=Ratings.choices, default=Ratings.G)
    synopsis = models.TextField(default=None)