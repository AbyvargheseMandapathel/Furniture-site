# Generated by Django 4.2.2 on 2023-10-02 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0035_alter_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='admincontrol',
            field=models.BooleanField(default=False, max_length=555),
        ),
    ]
