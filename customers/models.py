from django.db import models




class Customer(models.Model):
    name = models.CharField(max_length=200, verbose_name="اسم مشتری")
    phone_number  = models.CharField(max_length=15, verbose_name="شماره تماس مشتری")
    social_number = models.CharField(max_length=15, verbose_name="شماره واتساپ", null=True, blank=True)
    address = models.TextField(verbose_name="آدرس مشتری")

    def __str__(self):
        return self.name

