from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    pass


class Account(models.Model):

    class GenderChoices(models.TextChoices):
        MALE = "M"
        FEMALE = "F"
        OTHER = "O"
        NOT_SPECIFIED = "NS"

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.URLField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    gender = models.CharField(
        max_length=2, blank=True, null=True, choices=GenderChoices.choices
    )
    bio = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
