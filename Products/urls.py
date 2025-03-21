from django.urls import path
from .views import ProductsListView, ProductView, AddToCartView, SearchView

app_name = 'products'

urlpatterns = [
    path("", ProductsListView.as_view(), name="products_list"),
    path("product/<int:pk>", ProductView.as_view(), name="product_view"),
    path("product/add/<int:pk>/<int:quantity>", AddToCartView.as_view(), name="add_cart_view"),
    path("product/search", SearchView.as_view(), name="search_view"),
]
