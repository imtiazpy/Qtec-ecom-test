from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from django.conf import settings

from .models import Product


def product_index(request):
    return render(request, 'products/index.html')

class ProductListView(View):
    """Product List view. Returns Json for the frontend"""
     
    def get(self, request, *args, **kwargs):
        products = self.get_products()
        data = self.serialize_products(products)
        return JsonResponse(data, safe=False)

    def get_products(self):
        return Product.objects.all()

    def serialize_products(self, products):
        data = []
        for product in products:
            serialized_product = {
                'id': product.id,
                'name': product.name,
                'price': product.price,
                'photo_url': settings.MEDIA_URL + str(product.photo),
                'category': product.category.name,
                'type': product.type,
                'brand': product.brand.name,
                'warranty': product.warranty,
                'seller': product.seller.name,
            }
            data.append(serialized_product)
        return data
