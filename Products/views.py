from django.shortcuts import render
from django.views.generic import View
from .models import Products


# Create your views here.
class ProductsListView(View):
    template_name = 'Products/products_list.html'

    def get(self, request):
        products = Products.objects.all()
        return render(request, self.template_name, {'products': products})