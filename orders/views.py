from django.shortcuts import redirect, render
from .models import Order
from .forms import OrderForm
from django.contrib import messages
# Create your views here.



def order_update_view(request, pk):
    order = Order.objects.get(pk=pk)
    if request.method == "POST":
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            messages.success(request, "فرمایش فوق موفقانه ویرایش گردید.")
            return redirect("customer-order-create", order.customer.pk)
    else:
        form = OrderForm(instance=order)
    context = {
        "order" : order, 
        "form" : form
    }
    return render(request, "orders/update.html", context)




def order_delete_view(request, pk):


    order = Order.objects.get(pk=pk)

    if request.method == "POST":
        obj = Order.objects.get(pk=request.POST.get("obj"))
        obj.delete()
        messages.success(request, "فرمایش شما موفقانه از سیستم حذف گردید.")
        return redirect("customer-order-create", order.customer.pk)
    context = {
        "order" : order
    }

    return render(request, "orders/delete.html", context)


