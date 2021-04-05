from django.contrib import admin
from .models import Category, Products


class ProductsAdmin(admin.ModelAdmin):
    list_display = ('category', 'name', 'normal_price', 'promotion_price', 'promotion')
    list_filter = ('category', 'promotion')
    list_per_page = 10
    search_fields = ('category', 'name', 'promotion')


admin.site.register(Products, ProductsAdmin)
admin.site.register(Category)
