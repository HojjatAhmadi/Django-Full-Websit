# Generated by Django 5.1.6 on 2025-02-25 09:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(default='products/default_products', upload_to='products/products_image/')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price_original', models.PositiveIntegerField()),
                ('offer', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('price_buy', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Products.category')),
            ],
        ),
    ]
