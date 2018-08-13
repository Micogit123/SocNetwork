from django.db import models
from django.contrib.auth.models import User


class Country(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name = "Country"
        verbose_name_plural = "Countries"

    def __str__(self):
        return self.name


class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name = "City"
        verbose_name_plural = "Cities"

    def __str__(self):
        return self.name
       

class UserInformation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    country = models.CharField(max_length=30, blank=True)
    city = models.CharField(max_length=30, blank=True)

    class Meta:
        verbose_name = "User Information"
        verbose_name_plural = "User Informations"

    def __str__(self):
        return self.user.username