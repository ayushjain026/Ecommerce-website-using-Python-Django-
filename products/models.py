from django.db import models


class Product(models.Model):
    P_name = models.CharField(max_length=200)
    P_price = models.IntegerField()
    P_stock = models.IntegerField()
    P_image_url = models.CharField(max_length=2083)


class Cart(models.Model):
    name = models.CharField(max_length=30)
    product = models.CharField(max_length=40)
    item = models.CharField(max_length=50)
    item_url = models.CharField(max_length=2083)
    item_price = models.IntegerField()
    quantity = models.IntegerField(blank=True)


class Vegetable(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)


class Dal_Rice(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)


class Cookies_Snakes(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)


class Order(models.Model):
    user = models.CharField(max_length=50)
    fullname = models.CharField(max_length=40)
    phone = models.IntegerField()
    email = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    address = models.CharField(max_length=2000)
    note = models.CharField(max_length=2000, blank=True)
    item = models.CharField(max_length=50, blank=True)
    bill_amount = models.IntegerField()
    date = models.CharField(max_length=15)