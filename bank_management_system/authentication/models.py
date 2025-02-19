from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True, null=True)
    full_name = models.CharField(max_length=100, null=True)
    birthday = models.DateTimeField(null=True)
