from django.db import models

# Model to hold all the food items for the menu.
class Food(models.Model):
    """
    Model representing a food on the menu (but not a specific copy of a food).
    """
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    MY_SIZES = (
        ('S', 'Small'),
        ('L', 'Large'),
    )
    size = models.CharField(max_length=20, choices=MY_SIZES, default='S')
    MY_FOOD_TYPES = (
        ('PIZZA', 'pizza'),
        ('SUB', 'sub'),
        ('SALAD', 'salad'),
        ('PASTA', 'pasta'),
        ('DINNER', 'dinner platter'),
    )
    food_type = models.CharField(max_length=10, choices=MY_FOOD_TYPES, default='PIZZA')
    CHOOSE_TOPPINGS = (
        ('ONE', '1'),
        ('TWO', '2'),
        ('THREE', '3'),
        ('NO', 'no'),
    )
    choose_toppings = models.CharField(max_length=50, choices=CHOOSE_TOPPINGS, default='NO')
    TOPPINGS = (
        ('NONE', 'none'),
        ('PEPPERONI', 'pepperoni'),
        ('SAUSAGE', 'sausage'),
        ('MUSHROOMS', 'mushrooms'),
        ('ONIONS', 'onions'),
        ('HAM', 'ham'),
        ('CANADIAN BACON', 'canadian bacon'),
        ('PINEAPPLE', 'pineapple'),
        ('EGGPLANT', 'egglplant'),
        ('TOMATO & BASIL', 'tomato & basil'),
        ('GREEN PEPPERS', 'green peppers'),
        ('HAMBURGER', 'hamburger'),
        ('SPINACH', 'spinach'),
        ('ARTICHOKE', 'artichoke'),
        ('BUFFALO CHICKEN', 'buffalo chicken'),
        ('BARBECUE CHICKEN', 'barbecue chicken'),
        ('ANCHOVIES', 'anchovies'),
        ('BLACK OLIVES', 'black olives'),
        ('FRESH GARLIC', 'fresh garlic'),
        ('ZUCCHINI', 'zucchini'),
    )
    toppings = models.CharField(max_length=50, choices=TOPPINGS, default='NONE')
    # Foreign Key used because food can only have one price
    # Author as a string rather than object because it hasn't been declared yet in the file.
    summary = models.TextField(max_length=1000, blank=True, help_text='Enter a brief description of the food item')
    # ManyToManyField used because genre can contain many foods. Foods can cover many genres.
    # Genre class has already been defined so we can specify the object above.

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.title

# Model to have the one to many order number, each order number
# can have 1+ orders associated with it.
class Order_Number(models.Model):
       def __int__(self):
        """
        String for representing the Model object.
        """
        return self.id
# Model to hold items ordered off the menu, associated with
# an order number.
class Order(models.Model):
    """
    Model representing the ordered items on the menu.
    """
    #order_id corresponds to the Order_Number primary key
    order_number = models.ForeignKey(Order_Number, on_delete=models.CASCADE)
    username = models.CharField(max_length=200, default='')
    name = models.CharField(max_length=200, default='')
    email = models.CharField(max_length=200, default='')
    MY_STATUSES = (
        ('INCOMPLETE', 'incomplete'),
        ('SUBMITTED', 'submitted'),
        ('FILLED', 'filled'),
    )
    order_status = models.CharField(max_length=20, choices=MY_STATUSES, default='INCOMPLETE')
    quantity_ordered = models.CharField(max_length=200, default='1')
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    MY_SIZES = (
        ('S', 'Small'),
        ('L', 'Large'),
    )
    size = models.CharField(max_length=20, choices=MY_SIZES, default='S')
    MY_FOOD_TYPES = (
        ('PIZZA', 'pizza'),
        ('SUB', 'sub'),
        ('SALAD', 'salad'),
        ('PASTA', 'pasta'),
        ('DINNER', 'dinner platter'),
    )
    food_type = models.CharField(max_length=10, choices=MY_FOOD_TYPES, default='PIZZA')

    toppings = models.CharField(max_length=200)

    def __str__(self):
        """
        String for representing the Model object.
        """
        return f"order number: {self.order_number.id} {self.title}"
