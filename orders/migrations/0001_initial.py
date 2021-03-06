# Generated by Django 4.0.2 on 2022-04-04 08:10

from django.db import migrations, models
import django.db.models.deletion
import django_jalali.db.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customers', '0001_initial'),
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('height', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='قد')),
                ('width', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='بر')),
                ('depth', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='عمق')),
                ('direction', models.CharField(choices=[('راست', 'راست'), ('چپ', 'چپ')], default='راست', max_length=30)),
                ('quantity', models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='مقدار / تعداد')),
                ('price', models.DecimalField(decimal_places=4, default=0, max_digits=10, verbose_name='قیمت فی واحد')),
                ('paid', models.DecimalField(decimal_places=4, default=0, max_digits=10, verbose_name='مقدار رسید')),
                ('remain', models.DecimalField(decimal_places=4, default=0, max_digits=10, verbose_name='مقدار باقی مانده')),
                ('total_amount', models.DecimalField(decimal_places=4, default=0, max_digits=10, verbose_name='مجموع پول')),
                ('type', models.CharField(max_length=200, verbose_name='نوعیت کار')),
                ('order_date', django_jalali.db.models.jDateField(verbose_name='تاریخ فرمایش')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.customer')),
                ('service_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.category')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True, verbose_name='توضیح پرداخت')),
                ('price_per_unit', models.DecimalField(decimal_places=2, default=0, max_digits=4, verbose_name='میزان دستمزد')),
                ('total', models.DecimalField(decimal_places=2, default=0, max_digits=4, verbose_name='مجموع')),
                ('paid_amount', models.DecimalField(decimal_places=2, default=0, max_digits=4, verbose_name='مقدار پرداخت شده')),
                ('remain_amount', models.DecimalField(decimal_places=2, default=0, max_digits=4, verbose_name='مقدار باقی مانده')),
                ('employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='employees.employee', verbose_name='نام مشتری')),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='orders.order')),
            ],
        ),
    ]
