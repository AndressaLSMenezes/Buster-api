from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.CharField(
        max_length=127, unique=True, error_messages={"email": "This email"}
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birthdate = models.DateField(blank=True)
    is_employee = models.BooleanField(default=False)
