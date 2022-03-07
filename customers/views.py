from multiprocessing import Event
from django.shortcuts import redirect, render

from customers.models import Customer, CustomerEvent, FinanceDetail
from orders.models import Order
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



def customer_order_view(request, pk):
    customer = Customer.objects.get(pk=pk)
    orders = customer.order_set.all()
    if request.method == "POST":
        work_type = request.POST.get("service_name")
        height = request.POST.get("height")
        width = request.POST.get("width")
        depth = request.POST.get("depth")
        direction = request.POST.get("direction")
        quantity = request.POST.get("quantity")
        price = request.POST.get("price")
        paid = request.POST.get("paid")
        type_of_work = request.POST.get("type")
        date = request.POST.get("order_date")


        service_name = "دروازه"
        if work_type == "door":
            service_name = "دروازه"
        elif work_type == "window":
            service_name = "کلکین"
        elif work_type == "cnc":
            service_name = "سی ان سی"
        elif work_type == "press":
            service_name = "پرس"
        elif work_type == "zdoor":
            service_name = 'ضد سرقت'
        else:
            service_name = ""
        obj = Order.objects.create(
            customer=customer, 
            service_name=service_name,
            height=height,
            width=width, 
            depth=depth, 
            direction=direction, 
            quantity=float(quantity),
            price=float(price), 
            paid=float(paid), 
            type=type_of_work, 
            order_date=date
        )
        if obj:
            messages.success(request, f"فرمایش جدید برای مشتری {customer.name} اضافه شد.")


        return redirect("customer-order-create", customer.pk)
    context = {
        "customer" : customer, 
        "orders" : orders
    }
    return render(request, "customers/orders/create.html", context)




def customer_report_view(request,pk):
    customer = Customer.objects.get(pk=pk)
    orders = customer.order_set.all()
    count = orders.count()
    total_amount = 0
    paid = 0
    remain = 0

    events = customer.customerevent_set.all()
    financeDetails = customer.financedetail_set.all()
    for i in orders:
        total_amount += i.total_amount
        paid += i.paid
        remain += i.remain


    if request.method == "POST":
        title = request.POST.get("title")
        date = request.POST.get("date")
        event = CustomerEvent.objects.create(
            customer=customer, 
            title=title, 
            event_finish_at=date
        )
        if event:
            messages.success(request, "واقعه جدید برای مشتری فوق ثبت شد. ")
            return redirect("customer-report", customer.pk)
    context = {
        "customer" : customer, 
        "count" : count, 
        "total" : total_amount, 
        "paid" : paid, 
        'remain' : remain, 
        "events" : events, 
        "details" : financeDetails
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









