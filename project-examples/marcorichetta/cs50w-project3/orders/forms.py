from django.forms import ModelForm
from orders.models import PizzaOrder


class PizzaForm(ModelForm):
    class Meta:
        model = PizzaOrder
        fields = ['style', 'size', 'extras', 'toppings', 'quantity']