# Generated by Django 4.0.2 on 2022-03-04 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0005_alter_customerevent_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerevent',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='customerevent',
            name='event_finish_at',
            field=models.DateTimeField(verbose_name='تاریخ ختم فرصت'),
        ),
    ]
