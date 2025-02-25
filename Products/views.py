from django.shortcuts import render
from django.views.generic import View
from .models import Products,Category


# Create your views here.
class ProductsListView(View):
    template_name = 'Products/products_list.html'

    def get(self, request):
        products = Products.objects.all()
        for product in products:
            if product.price_buy == 0:
                product.price_buy = product.price_original * (product.offer/100)
                product.save()
        return render(request, self.template_name, {'products': products, "category": Category.objects.all()})