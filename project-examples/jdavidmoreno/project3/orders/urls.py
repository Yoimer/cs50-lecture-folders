from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_page, name="login"),
    path("register", views.register, name="register"),
    path("logout", views.logout_page, name="logout"),
    path("pizzas", views.pizzas, name="pizzas"),
    path("subs", views.subs, name="subs"),
    path("pasta", views.pasta, name="pasta"),
    path("salads", views.salads, name="salads"),
    path("platters", views.platters, name="platters"),
    path("added", views.added, name="added"),
    path("cart", views.cart, name="cart"),
    path("delete", views.delete, name="delete"),
    path("checkout", views.checkout, name="checkout")
]
