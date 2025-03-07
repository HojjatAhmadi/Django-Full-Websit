from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from .models import Products, Category, CartProduct


# Create your views here.
class ProductsListView(View):
    template_name = 'Products/products_list.html'

    def get(self, request):
        products = Products.objects.all()
        for product in products:
            if product.price_buy == 0:
                product.price_buy = product.price_original * (product.offer / 100)
                product.save()
        return render(request, self.template_name, {'products': products, "category": Category.objects.all()})


class ProductView(View):
    template_name = 'Products/product.html'

    def get(self, request, pk):
        product = get_object_or_404(Products, pk=pk)
        products = Products.objects.all()
        return render(request, self.template_name, {'product': product, 'products': products})


class AddToCartView(View):
    def post(self, request, pk, quantity):
        product = get_object_or_404(Products, pk=pk)
        message_type = "success"
        if CartProduct.objects.filter(product=product, user=request.user).exists():
            cart = get_object_or_404(CartProduct, product=product, user=request.user)
            cart.quantity += quantity
            cart.save()
            message_msg = "your cart was update successfully"
        else:
            CartProduct.objects.create(product=product, user=request.user, quantity=quantity)
            message_msg = "new product was added successfully"
        messages.success(request, message_msg, "success")
        return redirect(request.META.get('HTTP_REFERER'))
