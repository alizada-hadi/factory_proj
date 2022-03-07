from django import forms
from .models import Order
from jalali_date.widgets import AdminJalaliDateWidget, AdminSplitJalaliDateTime
from jalali_date.fields import JalaliDateField, SplitJalaliDateTimeField
class DateInput(forms.DateInput):
    input_type = "date"

class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = (
            'service_name',
            'height',
            'width',
            'depth',
            'direction',
            'quantity',
            'price',
            'paid',
            'order_date'
        )
        widgets = {
            'order_date': forms.DateInput(attrs={'type' : 'date'})
        }

        def __init__(self, *args, **kwargs):
            super(OrderForm, self).__init__(*args, **kwargs)
            self.fields['order_date'] = SplitJalaliDateTimeField(label="تاریخ مراجعه", widget=AdminSplitJalaliDateTime)