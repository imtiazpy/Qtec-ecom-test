from django.urls import path
from .views import product_index, ProductListView


urlpatterns = [
    path('', product_index, name='index'),
    path('products/', ProductListView.as_view(), name='product-list'),
]