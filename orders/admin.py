from django.contrib import admin
from .models import Category, Order, OrderDetail
# Register your models here.


admin.site.register(Category)
admin.site.register(Order)
admin.site.register(OrderDetail)
