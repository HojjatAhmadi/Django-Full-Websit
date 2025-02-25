from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

class Products(models.Model):
    img = models.ImageField(upload_to='products/products_image/', default="products/default_products")
    name = models.CharField(max_length=100)
    description = models.TextField()
    price_original = models.PositiveIntegerField()
    offer = models.PositiveIntegerField(null=True, blank=True, default=0)
    price_buy = models.PositiveIntegerField(null=True, blank=True, default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)