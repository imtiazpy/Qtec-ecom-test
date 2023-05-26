from django.db import models
from django.utils.translation import gettext as _

from common.models import NameTimeStamp
from product_categories.models import Category, Brand
from sellers.models import Seller


class ProductType(models.TextChoices):
    ELECTRONICS = 'ELECTRONICS', 'Electronics'
    LIFE_STYLE = 'LIFE_STYLE', 'Life_Style'
    MOBILE_PHONE_ACCESSORIES = 'MOBILE_PHONE_ACCESSORIES', 'Mobile_Phone_Accessories'


class Product(NameTimeStamp):
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='product_categories')
    type = models.CharField(_('Type'), max_length=100, choices=ProductType.choices, null=True, blank=False)
    price = models.DecimalField(_('Price'), max_digits=10, decimal_places=2, null=True, blank=True)
    photo = models.ImageField(_('Photo'), upload_to='images', null=True, blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='product_brands')
    warranty = models.CharField(_('Warranty'), max_length=255, null=True, blank=False)
    seller = models.ForeignKey(Seller, on_delete=models.PROTECT, related_name='product_seller')

    def __str__(self):
        return f'{self.id}-{self.name}'