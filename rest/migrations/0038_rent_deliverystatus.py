# Generated by Django 4.2.2 on 2024-03-14 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0037_rename_condition_furniturerent_stock'),
    ]

    operations = [
        migrations.AddField(
            model_name='rent',
            name='deliverystatus',
            field=models.BooleanField(default=False),
        ),
    ]
