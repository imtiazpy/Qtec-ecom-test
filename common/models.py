from django.db import models
from django.utils.translation import gettext as _

class NameTimeStamp(models.Model):
    name = models.CharField(_('Name'), max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True