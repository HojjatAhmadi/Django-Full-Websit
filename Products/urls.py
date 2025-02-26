from django.urls import path
from .views import ProductsListView, ProductView

app_name = 'products'

urlpatterns = [
    path("", ProductsListView.as_view(), name="products_list"),
    path("product/<int:pk>", ProductView.as_view(), name="product_view"),
]
