from django import template

register = template.Library()

@register.filter
def remove_decimal_point(value):
    # return value.replace(".","")
    return int(value)