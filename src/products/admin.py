# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Product, Category, ProductImage


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = { 'slug': ('name',)}
admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['category', 'name', 'slug', 'short_description', 'long_description', 'product_info','features','manufacturer','condition','model','shipping', 'price',]
    #list_filter = ['available', 'created', 'updated', 'category']
    #list_editable = ['price', 'stock', 'available']
    prepopulated_fields = { 'slug': ('name',),}
    
admin.site.register(Product, ProductAdmin)

class ProductImageInline(admin.StackedInline):
    model = ProductImage
    extra = 4

class ProductAdmin(admin.ModelAdmin):
    inlines = [ ProductImageInline, ]
admin.site.register(ProductImage)