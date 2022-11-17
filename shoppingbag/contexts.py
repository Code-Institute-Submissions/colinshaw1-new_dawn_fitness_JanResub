from decimal import Decimal
from django.conf import settings

# makes all dictioanries avialble to all templeates on the app
def bag_contents(request):
    
    # setting bag items to an empty list
    bag_items = []
    # total set to 0
    total = 0
    # count set to 0
    product_count = 0

    # calculation for free shipping and adding on cost of shipping
    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE)
        # shows users if they spend a little more they will be able to get free delivery
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0
    
    grand_total = delivery + total

    # returns a dictionary as context processer
    # makes all avilabe in all templates
    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,

    }

    return context