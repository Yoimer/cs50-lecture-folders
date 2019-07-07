from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Food, Order, Order_Number
from django.db import models
from django.contrib.auth.models import User
from django import forms
from .forms import UserCreateForm
import stripe
import datetime
import requests

# at the homepage, prompt to either login or register
def index(request):
    if request.user.username is not None:
      return redirect('order')
    return render(request, 'index.html', {})

# form to register for the site
def signup(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        # save the registration form.
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('order')
    else:
        form = UserCreateForm()
    return render(request, 'signup.html', {'form': form})

# show the menu (you dont order from here though)
def menu(request):
    # grab all the items on the menu.
    food_list=Food.objects.all()
    # get a count of all items on the menu.
    food_count=Food.objects.all().count()
    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'menu.html',
        context={'food_list':food_list, 'food_count':food_count},
    )

# view existing orders at this route.
def view_orders(request):
   # grab all the orders to display to the administrator.
   orders=Order.objects.all()
   return render(request, 'existing-orders.html', {'orders':orders})

# show the order form at this route.
def order_from_menu(request):
    food_list=Food.objects.all()
    print(food_list)
    shopping_cart_food = {};
    # If this is a POST request then process the Form data
    if request.method == 'POST':
        # first create a new order number
        ON = Order_Number()
        ON.save()
        # next cycle through all the ordered items and
        # add them to the order number created above.
        for i in range(0,len(food_list)):
            data = request.POST.get('fooditem_' + str(i))
            data_toppings = request.POST.getlist('select_' + str(i))
            toppings_string = ', '.join(data_toppings)
            if data:
                food = Food.objects.get(pk=i)
                persons_name = request.user.first_name + ' ' + request.user.last_name
                total_price = food.price * int(data)
                O = Order(title=food, quantity_ordered=data, username=request.user.username, name=persons_name, email=request.user.email,
                  price=total_price, size='Large', food_type='PIZZA', toppings=toppings_string, order_number = ON)
                O.save()
    # grab all the items to show in the shopping cart.
    shopping_cart_food = Order.objects.filter(username=request.user.username, order_status='INCOMPLETE')
    cart_total = 0
    for item in shopping_cart_food:
        cart_total = cart_total + item.price
    # grab the number of items in the users shopping cart.
    cart_count = Order.objects.filter(username=request.user.username, order_status='INCOMPLETE').count()
    if cart_count < 1:
        shopping_cart_food = 'Empty Cart'

    food_toppings =  ['NONE', 'PEPPERONI', 'SAUSAGE', 'MUSHROOMS',
        'ONIONS', 'HAM', 'CANADIAN BACON', 'PINEAPPLE',
        'EGGPLANT', 'TOMATO & BASIL', 'GREEN PEPPERS',
        'HAMBURGER', 'SPINACH', 'ARTICHOKE', 'BUFFALO CHICKEN',
        'BARBECUE CHICKEN', 'ANCHOVIES', 'BLACK OLIVES',
        'FRESH GARLIC', 'ZUCCHINI']

    return render(request, 'order_food_form.html', {'food_list':food_list,
      'shopping_cart_food':shopping_cart_food, 'food_toppings':food_toppings, 'cart_total':cart_total})

# this route works with checkout, marking items in your cart
# as FILLED after checkout.
def checkout(request):
    # update statement marking ordered items in the cart as FILLED orders.
    shopping_cart = Order.objects.filter(username=request.user.username,
      order_status='INCOMPLETE').update(order_status='FILLED')
    return render(request, 'thankyou.html', {'checkedout':1})