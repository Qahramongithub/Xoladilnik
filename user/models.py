from django.contrib.auth.models import AbstractUser
from django.db import models




class Admin(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.full_name


class User(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    telegram = models.CharField(max_length=255, blank=True, null=True)
    instagram = models.CharField(max_length=255, blank=True, null=True)
    cart = models.ForeignKey('auth.CartNumber', on_delete=models.SET_NULL, blank=True, null=True)
    address = models.ForeignKey('auth.Address', on_delete=models.SET_NULL, blank=True, null=True)
    avatar = models.ImageField(upload_to="avatars", blank=True, null=True)
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.user.email


class CartNumber(models.Model):
    cart_number = models.CharField(max_length=255, blank=True, null=True)
    expiration_date = models.DateField(blank=True, null=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.cart_number


class Address(models.Model):
    icon = models.CharField(max_length=255, blank=True, null=True)
    apartmentNumber = models.CharField(max_length=255, blank=True, null=True)
    floor = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    longitude = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)
    latitude = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)

    def __str__(self):
        return self.address
