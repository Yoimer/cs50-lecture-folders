"""Trees URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login_page, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout_page, name='logout'),
    path('<str:user_username>/myforest', views.myforest, name='myforest'),
    path('<str:user_username>/edit_profile', views.edit_profile, name='edit_profile'),
    path('add_old_markers', views.add_old_markers, name="add_old_markers"),
    path('<str:user_username>/new_tree', views.new_tree, name="new_tree"),
    path('delete_marker', views.delete_marker, name="delete_marker"),
    path('update', views.update, name="update"),
    path('treecodes', views.treecodes, name="treecodes"),
    path('offer/<int:offer_id>', views.offer, name="offer"),
    path('myoffers', views.myoffers, name="myoffers"),
    path('coupon/<int:offer_id>', views.coupon, name="coupon")
]
