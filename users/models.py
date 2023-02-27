from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True)
    birthdate = models.DateField(blank=True)
    is_employee = models.BooleanField(default=False)
