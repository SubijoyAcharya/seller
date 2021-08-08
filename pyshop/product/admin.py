from django.contrib import admin
from .models import Product
from django.contrib.auth import get_user_model


# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'image_url')



admin.site.register(Product, ProductAdmin)
