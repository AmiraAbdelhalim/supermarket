from django.contrib import admin
from .models import Customer, Invoice, Product

# Register your models here.

admin.site.register(Customer)
admin.site.register(Invoice)
admin.site.register(Product)

