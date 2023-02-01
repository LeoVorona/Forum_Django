from django.db import models
from django.db.models.fields import CharField


class CheckBox(models.Model):
    name = models.CharField(max_length=250)
    is_cheked = models.BooleanField(default=False)
    
