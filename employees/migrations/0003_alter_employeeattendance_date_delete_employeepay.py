# Generated by Django 4.0.2 on 2022-02-13 16:16

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0002_alter_employeeattendance_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeeattendance',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 2, 13, 16, 16, 9, 35101, tzinfo=utc)),
        ),
        migrations.DeleteModel(
            name='EmployeePay',
        ),
    ]
