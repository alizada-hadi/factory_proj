# Generated by Django 4.0.2 on 2022-03-04 07:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0007_financedetail_total_remain'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='financedetail',
            name='total_remain',
        ),
    ]
