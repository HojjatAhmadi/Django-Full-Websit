# Generated by Django 5.1.6 on 2025-02-25 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0004_alter_products_offer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='price_buy',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]
