# Generated by Django 4.2.2 on 2024-02-21 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0028_rename_customer_addressuser_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='furniturerent',
            name='rentproduct',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='furniturerent',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
