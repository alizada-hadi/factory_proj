# Generated by Django 4.0.2 on 2022-03-05 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0009_alter_financedetail_pay_amount_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='financedetail',
            name='loan',
            field=models.PositiveBigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='financedetail',
            name='title',
            field=models.CharField(max_length=250, verbose_name='مقدار به حروف'),
        ),
    ]