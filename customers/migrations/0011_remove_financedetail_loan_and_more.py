# Generated by Django 4.0.2 on 2022-03-05 14:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0010_financedetail_loan_alter_financedetail_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='financedetail',
            name='loan',
        ),
        migrations.RemoveField(
            model_name='financedetail',
            name='remain',
        ),
        migrations.RemoveField(
            model_name='financedetail',
            name='total_pre_loan',
        ),
    ]