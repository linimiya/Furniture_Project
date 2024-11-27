from django.db import models


class Contact_DB(models.Model):
    Name = models.CharField(max_length=100, blank=True, null=True)
    Email = models.CharField(max_length=100, blank=True, null=True)
    Message = models.TextField(max_length=100, blank=True, null=True)


class signup_DB(models.Model):
    Name = models.CharField(max_length=100, blank=True, null=True)
    Email = models.CharField(max_length=100, blank=True, null=True)
    Mobile = models.IntegerField(blank=True, null=True)
    Password = models.CharField(max_length=100, blank=True, null=True)
    ConfirmPassword = models.CharField(max_length=100, blank=True, null=True)


class CartDb(models.Model):
    Username = models.CharField(max_length=100, null=True, blank=True)
    ProductName = models.CharField(max_length=100, null=True, blank=True)
    Quantity = models.IntegerField(blank=True, null=True)
    TotalPrice = models.IntegerField(blank=True, null=True)
    PricePerItem = models.CharField(max_length=100, blank=True, null=True)
    Prod_Img = models.ImageField(upload_to="cart_Img", null=True, blank=True)


class OrderDB(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    Email = models.CharField(max_length=100, blank=True, null=True)
    Place = models.CharField(max_length=100, null=True, blank=True)
    Address = models.CharField(max_length=100, null=True, blank=True)
    Mobile = models.IntegerField(blank=True, null=True)
    Message = models.CharField(max_length=100, null=True, blank=True)
    TotalPrice = models.IntegerField(blank=True, null=True)

# Create your models here.
