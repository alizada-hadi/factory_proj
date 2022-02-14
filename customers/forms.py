

from django import forms
from .models import Customer



class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ["name", "last_name", "phone_number", "social_number", "address"]