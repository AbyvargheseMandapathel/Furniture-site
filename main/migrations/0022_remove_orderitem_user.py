# Generated by Django 4.2.2 on 2023-10-11 04:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_orderitem_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='user',
        ),
    ]
