from django.db import models
from django.utils.translation import gettext as _

from common.models import NameTimeStamp


class Category(NameTimeStamp):
    
    def __str__(self):
        return f'{self.id}-{self.name}'


class Brand(NameTimeStamp):
    

    def __str__(self):
        return f'{self.id}-{self.name}'



