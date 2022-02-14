from django.shortcuts import redirect, render

from customers.models import Customer
from .forms import CustomerForm
from django.contrib import messages
# Create your views here.



def customer_list_view(request):
    customers = Customer.objects.all()
    context = {
        "customers" : customers
    }
    return render(request, "customers/list.html", context)


def customer_create_view(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "مشتری جدید موفقانه ثبت سیستم گردید. ")
            return redirect("customer-list")
    else:
        form = CustomerForm()
    context = {
        "form" : form
    }
    return render(request, "customers/form.html", context)



def customer_update_view(request, pk):
    customer = Customer.objects.get(pk=pk)
    if request.method == "POST":
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            messages.success(request, "معلومات مشتری موفقانه تغییر و دوباره ثبت سیتم گردید. ")
            return redirect("customer-list")

    else:
        form = CustomerForm(instance=customer)
    context = {
        "form" : form, 
        "customer" : customer
    }

    return render(request, "customers/form.html", context)



def customer_delete_view(request, pk):
    customer = Customer.objects.get(pk=pk)
    if request.method == "POST":
        customer.delete()
        messages.success(request, f"{customer.name} - {customer.last_name} موفقانه از سیستم حذف گردید.")
        return redirect("customer-list")

    context = {
        "customer" : customer
    }
    return render(request, "customers/delete.html", context)

