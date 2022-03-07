from django.db import models
from django.utils import timezone
# Create your models here.



class Employee(models.Model):
    first_name = models.CharField(max_length=200, verbose_name="نام کارمند")
    last_name = models.CharField(max_length=200, verbose_name="تخلص کارمند")
    father_name = models.CharField(max_length=200, verbose_name="نام پدر")
    position = models.CharField(max_length=200, verbose_name="وظیفه")
    phone_number = models.CharField(max_length=15, verbose_name="شماره تماس کارمند")
    salary = models.IntegerField(default=0, verbose_name="معاش کارمند")
    head = models.BooleanField(default=False, verbose_name="سرگروپ")

    def __str__(self):
        return f"{self.first_name} - {self.last_name}"



class EmployeeAttendance(models.Model):
    ATTEND = (
        ("حاضر", "حاضر"),
        ("غایب", "غایب")
    )
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)
    attend = models.CharField(max_length=20, choices=ATTEND, default="حاضر")
    date = models.DateField()


    



