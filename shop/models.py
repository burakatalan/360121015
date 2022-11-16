from django.db import models

# Create your models here.

class Cart(models.Model):
 image = models.ImageField(upload_to='movie/images/')
 product_name = models.CharField(max_length=250)
 price = models.FloatField(blank=True)
 quantity = models.IntegerField(blank=True)
 total = models.FloatField(blank=True)

class Product(models.Model):
# id = models.IntegerField(blank=True)
 product_name = models.CharField(max_length=250)
 price = models.FloatField(blank=True)
 stock = models.IntegerField(blank=True)
 description = models.CharField(max_length=1000)

class Media(models.Model):
 image = models.ImageField(upload_to='movie/images/')
 product_name = models.CharField(max_length=250)

class Category(models.Model):
 image = models.ImageField(upload_to='movie/images/')
 category = models.CharField(max_length=50)

class User(models.Model):
 name = models.CharField(max_length=50)
 surname = models.CharField(max_length=50)

class UserAdress(models.Model):
 name = models.CharField(max_length=50)
 city = models.CharField(max_length=50)
 province = models.CharField(max_length=50)
 adress = models.CharField(max_length=50)

class Orders(models.Model):
 name = models.CharField(max_length=50)
 order_number = models.IntegerField(blank=True)
 product_name = models.CharField(max_length=250)   
 quantity = models.IntegerField(blank=True)