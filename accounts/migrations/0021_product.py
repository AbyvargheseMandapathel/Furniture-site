# Generated by Django 4.2.2 on 2023-09-08 06:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0020_delete_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=255, null=True)),
                ('product_name', models.CharField(max_length=255, null=True)),
                ('material_description', models.TextField(max_length=255, null=True)),
                ('product_description', models.TextField(max_length=255, null=True)),
                ('price', models.CharField(max_length=255, null=True)),
                ('quantity', models.CharField(max_length=255, null=True)),
                ('category', models.CharField(max_length=255, null=True)),
                ('subcategory', models.CharField(max_length=255, null=True)),
                ('product_images1', models.FileField(blank=True, max_length=255, null=True, upload_to='sample/')),
                ('product_images2', models.FileField(blank=True, max_length=255, null=True, upload_to='sample/')),
                ('product_images3', models.FileField(blank=True, max_length=255, null=True, upload_to='sample/')),
                ('product_images4', models.FileField(blank=True, max_length=255, null=True, upload_to='sample/')),
                ('status', models.BooleanField(default=False)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
