from django.contrib import admin

# Register your models here.
from .models import CustomerEvent, FinanceDetail

admin.site.register(CustomerEvent)
admin.site.register(FinanceDetail)