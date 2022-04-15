from django.db import models
from customers.models import Customer
from django_jalali.db import models as jmodels
from employees.models import Employee
# Create your models here.



class Category(models.Model):
    name = models.CharField(max_length=200)


    def __str__(self):
        return f"{self.id}"



class Order(models.Model):
    DIRECTION = (
        ("راست", "راست"),
        ("چپ", "چپ"),
    )
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    service_name = models.ForeignKey(Category, on_delete=models.CASCADE)
    height = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="قد", null=True, blank=True)
    width = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="بر", null=True, blank=True)
    depth = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="عمق", null=True, blank=True)
    direction = models.CharField(max_length=30, choices=DIRECTION, default="راست", null=True,  blank=True)
    quantity = models.DecimalField(max_digits=6, decimal_places=2, default=0, verbose_name="مقدار / تعداد")
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="قیمت فی واحد")
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="مجموع")
    paid_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="مقدار پرداخت شده")
    remain_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="مقدار باقی مانده")
    type = models.CharField(max_length=200, verbose_name="نوعیت کار")
    order_date = jmodels.jDateField(auto_now_add=True)


    def save(self, *args, **kwargs):
        if not self.total:
            self.total = float(self.quantity) * float(self.price)
        if not self.remain_amount:
            self.remain_amount = float(self.quantity) * float(self.price) - float(self.paid_amount)

        super().save(*args, **kwargs)


    def __str__(self):
        return f"{self.service_name.name}"


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, verbose_name="توضیح پرداخت", null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=4, default=0, verbose_name="قیمت فی واحد")
    total = models.DecimalField(max_digits=4, decimal_places=2, default=0, verbose_name="مجموع")
    paid_amount = models.DecimalField(max_digits=4, decimal_places=2, default=0, verbose_name="مقدار پرداخت شده")
    remain_amount = models.DecimalField(max_digits=4, decimal_places=2, default=0, verbose_name="مقدار باقی مانده")

    def save(self, *args, **kwargs):
        if not self.total:
            self.total = self.order.quantity * self.price_per_unit
        if not self.remain_amount:
            self.remain_amount = self.total - self.paid_amount
    
        super().save(*args, **kwargs)

    
    def __str__(self):
        return f"order detail {self.id}"