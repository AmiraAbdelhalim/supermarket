from django.db import models
from phone_field import PhoneField
from django.utils import timezone


# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=191)
    phone = PhoneField()
    address = models.TextField(max_length=200)
    email = models.EmailField(max_length=200)
    blocked_status = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=191)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    available_quantity = models.IntegerField()

    def __str__(self):
        return self.name


class Invoice(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    shipping_address = models.TextField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Invoice created at {}'.format(self.created_on)
