from django import forms
from .models import Order
from jalali_date.widgets import AdminJalaliDateWidget, AdminSplitJalaliDateTime
from jalali_date.fields import JalaliDateField, SplitJalaliDateTimeField
class DateInput(forms.DateInput):
    input_type = "date"

class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ['height']
        
