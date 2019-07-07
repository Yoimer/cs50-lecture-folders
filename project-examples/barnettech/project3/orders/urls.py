from django.urls import path
from .models import Food

from . import views

# register all the url routes in the views.py file
urlpatterns = [
    path("", views.index, name="index"),
    path("signup", views.signup, name="signup"),
    path("menu", views.menu, name="menu"),
    path("order", views.order_from_menu, name="order"),
    path("checkout", views.checkout, name="checkout"),
    path("view_orders", views.view_orders, name="view_orders")
]
