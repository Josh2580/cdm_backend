from django.db import models
from django.utils import timezone


class Mining(models.Model):
    name = models.CharField(default="CARDANO MAZE", max_length=20)
    quantity_mined = models.PositiveIntegerField(default=0)
    time_clicked = models.DateTimeField()
    date_joined = models.DateTimeField(default=timezone.now)
    mineral_extracted = models.CharField(max_length=50, default="")
    extraction_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.name}"
