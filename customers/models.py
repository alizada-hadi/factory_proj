from django.db import models



class Customer(models.Model):
    name = models.CharField(max_length=200, verbose_name="اسم مشتری")
    last_name = models.CharField(max_length=200, verbose_name="تخلص مشتری")
    phone_number  = models.CharField(max_length=15, verbose_name="شماره تماس مشتری")
    social_number = models.CharField(max_length=15, verbose_name="شماره واتساپ", null=True, blank=True)
    address = models.CharField(max_length=200, verbose_name="آدرس مشتری")
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created', )

    def __str__(self):
        return self.name


class CustomerEvent(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, verbose_name="عنوان واقعه")
    event_finish_at = models.DateTimeField(verbose_name="تاریخ ختم فرصت")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class FinanceDetail(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    title = models.CharField(max_length=250, verbose_name="مقدار به حروف")
    pay_amount = models.PositiveBigIntegerField(default=0, verbose_name="مبلغ پرداخت شد")
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    

