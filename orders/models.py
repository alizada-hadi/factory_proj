from django.db import models
from customers.models import Customer
from django_jalali.db import models as jmodels
from employees.models import Employee
# Create your models here.



class Order(models.Model):
    SERVICES = (
        ("دروازه", "دروازه"),
        ("کلکین", "کلکین"),
        ("سی ان سی", "سی ان سی"),
        ("پرس", "پرس"),
        ("ضد سرقت", "ضد سرفت"),
    )
    DIRECTION = (
        ("راست", "راست"),
        ("چپ", "چپ"),
    )
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    service_name = models.CharField(max_length=50, choices=SERVICES, verbose_name="خدمات")
    width = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="عرض", null=True, blank=True)
    height = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="قد", null=True, blank=True)
    depth = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="عمق", null=True, blank=True)
    direction = models.CharField(max_length=30, choices=DIRECTION, default="راست")
    quantity = models.DecimalField(max_digits=6, decimal_places=2, default=0, verbose_name="مقدار / تعداد")
    price = models.DecimalField(max_digits=10, decimal_places=4, default=0, verbose_name="قیمت فی واحد")
    paid = models.DecimalField(max_digits=10, decimal_places=4, default=0, verbose_name="مقدار رسید")
    remain = models.DecimalField(max_digits=10, decimal_places=4, default=0, verbose_name="مقدار باقی مانده")
    total_amount = models.DecimalField(max_digits=10, decimal_places=4, default=0, verbose_name="مجموع پول")
    order_date = jmodels.jDateField()
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)


    def save(self, *args, **kwargs):
        if not self.total_amount:
            self.total_amount = self.quantity * self.price
        if not self.remain:
            self.remain = self.total_amount - self.paid
        super().save(*args, **kwargs)

    def __str__(self):
        return self.type.customer.name
