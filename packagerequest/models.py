from django.db import models
from django.conf import settings


class PackageRequest(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    item_name = models.CharField(max_length=64)
    item_description = models.TextField(max_length=256)
    weight = models.IntegerField(default=0)
    origin_country = models.CharField(max_length=64)
    destination_country = models.CharField(max_length=64)
    offer_price = models.FloatField(default=0)
    deadline_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.item_name
