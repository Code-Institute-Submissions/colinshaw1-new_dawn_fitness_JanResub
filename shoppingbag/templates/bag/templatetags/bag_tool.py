from django import template

# taken from the django documention
register = template.Library()

#registers the filter as a template
@register.filter(name="cal_subtotal")
# function that takes in a price and parm and returns the product
def calc_subtotal(price, quanity):
    return price * quantity