from django.contrib import admin
from .models import Food, Order_Number, Order

# Register your models here.
admin.site.register(Food)
admin.site.register(Order_Number)
admin.site.register(Order)