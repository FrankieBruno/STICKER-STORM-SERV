from django.db import models
from django.contrib.auth.models import User


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateField(null=True, blank=True,
                            auto_now=False, auto_now_add=False)
    completed_date = models.DateField(null=True, blank=True,
                            auto_now=False, auto_now_add=False)
    order_sticker = models.ManyToManyField(
        "Sticker", related_name="order_sticker_sticker")
    quantity = models.IntegerField()
    total = models.FloatField()