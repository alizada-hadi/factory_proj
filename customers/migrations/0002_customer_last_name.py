# Generated by Django 4.0.2 on 2022-02-13 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='last_name',
            field=models.CharField(default='', max_length=200, verbose_name='اسم مشتری'),
            preserve_default=False,
        ),
    ]