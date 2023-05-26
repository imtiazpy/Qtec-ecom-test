from django.db import models
from common.models import NameTimeStamp


class Seller(NameTimeStamp):
    
    def __str__(self):
        return f'{self.id}-{self.name}'