from django.db.models import Count
from django.views.generic import ListView

from .models import Product, ProductType
from product_categories.models import Brand, Category
from sellers.models import Seller


class ProductListView(ListView):
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'

    queryset = Product.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        selected_categories = self.request.GET.getlist('category')
        selected_brands = self.request.GET.getlist('brand')
        selected_product_types = self.request.GET.getlist('type')
        selected_warranty = self.request.GET.getlist('warranty')
        selected_sellers = self.request.GET.getlist('seller')
        min_price = self.request.GET.get('min_price')
        max_price = self.request.GET.get('max_price')

        context['brands'] = Brand.objects.all()
        context['categories'] = Category.objects.all()
        context['product_types'] = ProductType.choices
        context['warranty_values'] = self.queryset.values_list('warranty', flat=True).distinct().order_by('warranty')
        context['sellers'] = Seller.objects.all()

        context['selected_brands'] = [int(i) for i in selected_brands]
        context['selected_categories'] = [int(i) for i in selected_categories]
        context['selected_product_types'] = selected_product_types
        context['selected_warranty'] = selected_warranty
        context['selected_sellers'] = [int(i) for i in selected_sellers]
        context['min_price'] = min_price
        context['max_price'] = max_price

        # Calculate the product count based on the selected filters
        product_count = self.get_queryset().count()
        context['product_count'] = product_count

        # Get the selected sort value from the request
        selected_sort = self.request.GET.get('sort_by', '')
        context['selected_sort'] = selected_sort

        return context

    def get_queryset(self):
        queryset = super().get_queryset()

        filters = {}

        brands = self.request.GET.getlist('brand')
        categories = self.request.GET.getlist('category')
        types = self.request.GET.getlist('type')
        warranties = self.request.GET.getlist('warranty')
        sellers = self.request.GET.getlist('seller')
        min_price = self.request.GET.get('min_price')
        max_price = self.request.GET.get('max_price')

        if brands:
            filters['brand__in'] = brands
        if categories:
            filters['category__in'] = categories
        if types:
            filters['type__in'] = types
        if warranties:
            filters['warranty__in'] = warranties
        if sellers:
            filters['seller__in'] = sellers
        if min_price and max_price:
            filters['price__range'] = (min_price, max_price)

        if filters:
            queryset = queryset.filter(**filters)

        # Apply sorting logic based on the selected sort criteria
        sort_by = self.request.GET.get('sort_by', '')
        if sort_by == 'name':
            queryset = queryset.order_by('name')
        elif sort_by == 'price':
            queryset = queryset.order_by('price')

        return queryset
 