from multiprocessing import Event
from django.shortcuts import redirect, render

from customers.models import Customer, CustomerEvent, FinanceDetail
from orders.models import Order, OrderDetail, Category
from .forms import CustomerForm, CustomerEventForm
from orders.forms import OrderForm
from django.contrib import messages
from django.views  import View
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
            customer = form.save()
            messages.success(request, "مشتری جدید موفقانه ثبت سیستم گردید. ")
            return redirect("customer-order-create", customer.pk)
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



def customer_order_view(request, pk):
    customer = Customer.objects.get(pk=pk)
    orders = customer.order_set.all()
    categories = Category.objects.all()
    if request.method == "POST":
        category = Category.objects.get(name = request.POST.get("categories"))
        quantity = request.POST.get("qty")
        price = request.POST.get("price")
        paid  = request.POST.get("paid_amount")
        work_type = request.POST.get("type")
        direction = request.POST.get("direction")
        height = request.POST.get("height")
        if height == "":
            height = float(0)
        print(f"height is one {height}")
        width = request.POST.get("width")
        if width == "":
            width = float(0)
        depth = request.POST.get("depth")
        if depth == "":
            depth = float(0)
        try:
            Order.objects.create(
            customer=customer, 
            service_name=category, 
            height = height, 
            width=width, 
            depth=depth, 
            direction=direction, 
            quantity=quantity, 
            price=price, 
            type=work_type, 
            paid_amount = paid
            )
            messages.success(request, "فرمایش جدید ثبت سیستم گردید. ")
        except:
            messages.error(request, "مشکلی رخ داد، لطفا دوباره تلاش کنید.")
            
        return redirect("customer-order-create", customer.pk)
    context = {
        "customer" : customer, 
        "orders" : orders, 
        "categories" : categories
    }
    return render(request, "customers/orders/create.html", context)




def customer_report_view(request,pk):
    customer = Customer.objects.get(pk=pk)
    orders = customer.order_set.all()
    count = orders.count()
    total_amount = 0
    paid = 0
    remain = 0
    for order in orders:
        total_amount += order.total
        paid += order.paid_amount
        remain += order.remain_amount
    context = {
        "customer" : customer, 
        "count" : count, 
        "total_amount" : total_amount, 
        "paid" : paid, 
        "remain" : remain, 
        "orders" : orders
    }

    return render(request, "customers/report.html", context)



def customer_event_update_view(request, pk):
    event = CustomerEvent.objects.get(pk=pk)
    customer = event.customer
    if request.method == "POST":
        form = CustomerEventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            messages.success(request, "تغییرات موفقانه ایجاد گردید.")
            return redirect("customer-report", customer.pk)
    else:
        form = CustomerEventForm(instance=event)
    context = {
        "event" : event, 
        "form" : form
    }

    return render(request, "customers/event_update.html", context)



def customer_event_delete_view(request, pk):

    event = CustomerEvent.objects.get(pk=pk)
    if request.method == "POST":
        e =  CustomerEvent.objects.get(pk=request.POST.get("event"))
        if event.pk == e.pk:
            event.delete()
            messages.success(request, f"رویداد {event.title} موفقانه از لیست رویدادها حذف گردید.")
            return redirect("customer-report", event.customer.pk)
    else:
        pass

    
    context = {
        "event" : event
    }
    return render(request, "customers/event_delete.html", context)



def add_finance_detail_view(request, pk):

    customer = Customer.objects.get(pk=pk)
    order = customer.order_set.last()

    if request.method == "POST":
        bussin = request.POST.get('alphabet')
        amount = request.POST.get("amount")


        obj = FinanceDetail.objects.create(
            customer=customer, 
            title=bussin, 
            pay_amount=int(amount)
        )
        if obj:
            messages.success(request, f"شما به مقدار {amount} افغانی از مشتری {customer.name} دریافت کردید.")
            return redirect("customer-report", customer.pk)









