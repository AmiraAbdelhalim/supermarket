# Generated by Django 3.1.1 on 2020-09-22 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supermarket_app', '0005_auto_20200922_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
    ]
