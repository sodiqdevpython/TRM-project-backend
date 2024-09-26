from django.db import models
from simple_history.models import HistoricalRecords

class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    history = HistoricalRecords(inherit=True)

    class Meta:
        abstract = True