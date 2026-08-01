from django.db import models

from accounts.models import User

# Create your models here.


class Address(models.Model):
    country = models.CharField(max_length=50)
    state = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=100)
    line_1 = models.CharField(max_length=100)
    line_2 = models.CharField(
        max_length=100,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.country


class PhoneBookRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.OneToOneField(to=Address, on_delete=models.CASCADE)

    name = models.CharField(max_length=120)
    number = models.CharField(max_length=120)
    email = models.EmailField()

    profile_picture = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name
