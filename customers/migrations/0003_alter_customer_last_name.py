# Generated by Django 4.0.2 on 2022-02-14 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0002_customer_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='last_name',
            field=models.CharField(max_length=200, verbose_name='تخلص مشتری'),
        ),
    ]