from django.db import models

# Create your models here.
class Pizzas(models.Model):
    pizza = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.pizza}"

class Toppings(models.Model):
    topping = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.topping}"

class RegPizzaPrices(models.Model):
    pizza = models.ForeignKey(Pizzas, on_delete=models.CASCADE, related_name="regular_price")
    small = models.DecimalField(max_digits=5, decimal_places=2)
    large = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"Regular {self.pizza} pizza - Small:{self.small} Large:{self.large}"

class SiciPizzaPrices(models.Model):
    pizza = models.ForeignKey(Pizzas, on_delete=models.CASCADE, related_name="sicilian_price")
    small = models.DecimalField(max_digits=5, decimal_places=2)
    large = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"Sicilian {self.pizza} pizza - Small:{self.small} Large:{self.large}"


class Additions(models.Model):
    addition = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.addition}"

class Subs(models.Model):
    sub = models.CharField(max_length=30)
    small = models.DecimalField(max_digits=5, decimal_places=2)
    large = models.DecimalField(max_digits=5, decimal_places=2)
    additions = models.ManyToManyField(Additions, related_name="subs", blank=True)

    def __str__(self):
        return f"Sub {self.sub} - Small:{self.small} Large:{self.large}"


class Pastas(models.Model):
    pasta = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.pasta} - Price:{self.price}"

class Salads(models.Model):
    salad = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.salad} - Price:{self.price}"

class DinnerPlatters(models.Model):
    dinner = models.CharField(max_length=40)
    small = models.DecimalField(max_digits=5, decimal_places=2)
    large = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.dinner} - Small:{self.small} Large:{self.large}"

class Orders(models.Model):
    dish = models.CharField(max_length=40)
    pizza_type = models.CharField(max_length=40, null=True, blank=True)
    size = models.CharField(max_length=15, null=True, blank=True)
    pizza_toppings = models.ManyToManyField(Toppings, related_name="orders", blank=True)
    sub_additions = models.ManyToManyField(Additions, related_name="orders", blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    username = models.CharField(max_length=30)
    time = models.DateTimeField(auto_now=True)
    order_status = models.CharField(max_length=10, default='Draft')

    def to_tuple(self, query, object):
        list = query
        output = []
        if object == 'topping':
            for elem in list:
                output.append(elem.topping)
        else:
            for elem in list:
                output.append(elem.addition)
        return tuple(output)

    def __str__(self):
        return f"{self.id} | {self.dish} Type: {self.pizza_type} Size: {self.size} Toppings: {self.to_tuple(self.pizza_toppings.all(), 'topping')}\
        Additions: {self.to_tuple(self.sub_additions.all(), 'addition')} Price: {self.price} For: {self.username} At: {self.time.hour}:{self.time.minute}-{self.time.day}/{self.time.month}/{self.time.year} Status: {self.order_status}"



class Confirmations(models.Model):
    dish = models.CharField(max_length=40)
    pizza_type = models.CharField(max_length=40, null=True, blank=True)
    size = models.CharField(max_length=15, null=True, blank=True)
    pizza_toppings = models.ManyToManyField(Toppings, related_name="confirmations", blank=True)
    sub_additions = models.ManyToManyField(Additions, related_name="confirmations", blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    username = models.CharField(max_length=30)
    time = models.DateTimeField(auto_now=True)
    order_status = models.CharField(max_length=10, default='Draft')

    def to_tuple(self, query, object):
        list = query
        output = []
        if object == 'topping':
            for elem in list:
                output.append(elem.topping)
        else:
            for elem in list:
                output.append(elem.addition)
        return tuple(output)

    def __str__(self):
        return f"{self.id} | {self.dish} Type: {self.pizza_type} Size: {self.size} Toppings: {self.to_tuple(self.pizza_toppings.all(), 'topping')}\
        Additions: {self.to_tuple(self.sub_additions.all(), 'addition')} Price: {self.price} For: {self.username} At: {self.time.hour}:{self.time.minute}-{self.time.day}/{self.time.month}/{self.time.year} Status: {self.order_status}"
