# Generated by Django 4.2.16 on 2024-09-22 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0004_product_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
