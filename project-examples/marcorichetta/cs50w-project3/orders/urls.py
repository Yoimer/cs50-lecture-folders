from django.urls import path

from . import views

urlpatterns = [
    # This will execute index() on views.py
    path("", views.index, name='index'),
    path('checkout', views.checkout, name='checkout')
]
