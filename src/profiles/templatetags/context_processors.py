from django import template
from products.models import Category

register = template.Library()


@register.inclusion_tag('navbar.html')
def catalog():
    category = Category.objects.all()
    return {'category': category }