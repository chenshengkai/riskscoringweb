from django import template
from django.utils.encoding import smart_str

register = template.Library()

@register.filter
def verbose_name(obj, fieldname):
    return obj.model._meta.get_field(fieldname).verbose_name

@register.filter
def verbose_name_plural(obj, fieldname):
    return obj.model._meta.get_field(fieldname).verbose_name_plural