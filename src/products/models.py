# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.urls import reverse


#from filer.fields.image import FilerImageField
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=150)
    #publisher = models.CharField(max_length=300)
    description = models.TextField(blank=True)
    #pub_date = models.DateTimeField(auto_now_add=True, blank=True)
    def __unicode__(self):
        return self.name
#
#class CatalogCategory(models.Model):
#    catalog = models.ForeignKey('Catalog',related_name='categories')
#    parent = models.ForeignKey('self', blank=True, null=True,related_name='children')
#    name = models.CharField(max_length=300)
#    slug = models.SlugField(max_length=150)
#    description = models.TextField(blank=True)
#


class Product(models.Model):
    category = models.ForeignKey('Category',on_delete=models.CASCADE,related_name='products')
    name = models.CharField(max_length=300)
    slug = models.SlugField(max_length=150)
    #images = models.ForeignKey(ProductImage)
    short_description = models.TextField(max_length=150, default="", null=True, blank=True)
    long_description = models.TextField(default="", null=True, blank=True)
    product_info = models.TextField(default="", null=True, blank=True)
    features =models.TextField(default="", null=True, blank=True)
    manufacturer = models.CharField(max_length=300, null=True, blank=True)
    model = models.CharField(max_length=300, null=True, blank=True)
    condition = models.CharField(max_length=300, null=True, blank=True)
    shipping = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    price = models.DecimalField(max_digits=10,decimal_places=2, null=True, blank=True)

    class Meta:
        #ordering = ('-created',)
        index_together = (('id', 'slug'))

    def get_category(self):
        return reverse("product", kwargs={"category": self.category})
    
    def get_absolute_url(self):
    	return reverse("product", kwargs={"slug": self.slug})

    def get_checkout_url(self):
        return reverse("checkout", kwargs={"slug": self.slug})

    def __unicode__(self):
        return self.name

#   
#    def __unicode__(self):
#        #if self.parent:
#        #    return u'%s: %s - %s' % (self.catalog.name,self.parent.name,self.name)
#        return self.category#u'%s: %s' % (self.catalog.name, self.name)


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='products_photos', default ="")
    featured = models.BooleanField(default=False)

    def __unicode__(self):
    		return self.product.name
#class ProductDetail(models.Model):
#    '''
#    The ``ProductDetail`` model represents information unique to a
#    specific product. This is a generic design that can be used
#    to extend the information contained in the ``Product`` model with
#    specific, extra details.
#    '''
#    product = models.ForeignKey('Product',related_name='details')
#    attribute = models.ForeignKey('ProductAttribute')
#    value = models.CharField(max_length=500)
#    description = models.TextField(blank=True)
#
#def __unicode__(self):
#    return u'%s: %s - %s' % (self.product,self.attribute,self.value)
#
#class ProductAttribute(models.Model):
#    '''
#    The "ProductAttribute" model represents a class of feature found
#    across a set of products. It does not store any data values
#    related to the attribute, but only describes what kind of a
#    product feature we are trying to capture. Possible attributes
#    include things such as materials, colors, sizes, and many, many
#    more.
#    '''
#    name = models.CharField(max_length=300)
#    description = models.TextField(blank=True)
#
#def __unicode__(self):
#    return u'%s' % self.name

