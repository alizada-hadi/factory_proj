# Generated by Django 4.0.2 on 2022-02-13 14:30

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeeattendance',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 2, 13, 14, 30, 55, 126631, tzinfo=utc)),
        ),
    ]