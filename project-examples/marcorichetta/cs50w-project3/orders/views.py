from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from orders.forms import PizzaForm, GenericForm
from orders.models import (DinnerPlatter, Pasta, Pizza, Salad, Sub, SubExtra,
                           Topping)


def index(request):
    """ Homepage where users can view the menu and add items to a virtual cart """
    
    form = PizzaForm()
    generic_form = GenericForm()

    context = {
        "pizzas": Pizza.objects.all(),
        "toppings": Topping.objects.all(),
        "subs": Sub.objects.all(),
        "subExtras": SubExtra.objects.all(),

        "pastas": Pasta.objects.all(),
        "platters": DinnerPlatter.objects.all(),
        "salads": Salad.objects.all(),
        "form": form,
        "genericForm": generic_form
    }

    return render(request, "orders/index.html", context)

def cart(request):
    """ Here the user should see the items added with his price, quantity
    and detail, and then proceed to checkout.
    https://stackoverflow.com/questions/2827764/ecommerceshopping-cartwhere-should-i-store-shopping-cart-data-in-session-or#40130593"""

    if request.method == 'POST':

        pass
    
    else:
        return render(request, "orders/cart.html")


@login_required(login_url='/login/')
def checkout(request):
    """ Here the """

    if request.method == 'POST':

        form = PizzaForm(request.POST)

        if form.is_valid():
            #form.save()
            messages.success(request, f'Your order was placed!')
            return redirect('index')
    else:
        return render(request, "orders/checkout.html")
