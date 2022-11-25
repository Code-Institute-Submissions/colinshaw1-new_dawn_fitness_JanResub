from django.urls import path
from . import views

urlpatterns = [
    # url to link the proile view
    path('', views.profile, name='profile')
    # view for order history
    path('order_history/<order_number>', views.profile, name='order_history')
]