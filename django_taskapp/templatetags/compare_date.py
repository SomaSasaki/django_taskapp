from django import template
import datetime

register = template.Library()


@register.filter(expects_localtime=True)
def is_future(value):
    if type(value) is datetime.datetime:
        value = value.date()
    return value >= value.today()

@register.filter(expects_localtime=True)
def is_previous(value):
    if type(value) is datetime.datetime:
        value = value.date()
    return value < value.today()
