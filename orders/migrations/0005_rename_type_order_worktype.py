# Generated by Django 4.0.2 on 2022-03-01 12:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_order_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='type',
            new_name='workType',
        ),
    ]