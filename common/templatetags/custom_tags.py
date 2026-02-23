import urllib.parse
from django import template


register = template.Library()

@register.simple_tag(takes_context=True)
def query_param_add(context, key, value):
    dict_: dict = context["request"].GET.copy()
    dict_[key] = value
    return "?" + urllib.parse.urlencode(dict_)

@register.filter(name='currency')
def currency_formatter(value):
    try:
        float_value = float(value)
        return f"{float_value:.2f} EUR"
    except (ValueError, TypeError):
        return value

