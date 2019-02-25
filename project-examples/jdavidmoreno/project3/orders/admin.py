from django.contrib import admin

from .models import Pizzas, Toppings, RegPizzaPrices, SiciPizzaPrices, Subs, Additions, Pastas, Salads, DinnerPlatters, Orders, Confirmations

class OrderAdmin(admin.ModelAdmin):
    filter_horizontal = ("pizza_toppings", "sub_additions")

# Register your models here.
admin.site.register(Pizzas)
admin.site.register(Toppings)
admin.site.register(RegPizzaPrices)
admin.site.register(SiciPizzaPrices)
admin.site.register(Subs)
admin.site.register(Additions)
admin.site.register(Pastas)
admin.site.register(Salads)
admin.site.register(DinnerPlatters)
admin.site.register(Orders, OrderAdmin)
admin.site.register(Confirmations)
