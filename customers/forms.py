

from django import forms
from .models import Customer, CustomerEvent, FinanceDetail



class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ["name", "last_name", "phone_number", "social_number", "address"]




class CustomerEventForm(forms.ModelForm):
    class Meta:
        model = CustomerEvent
        fields = [
            "title", 
            "event_finish_at"
        ]


class FinanceDetailForm(forms.ModelForm):
    class Meta:
        model = FinanceDetail
        fields = [
            "title", 
            "pay_amount", 
        ]



