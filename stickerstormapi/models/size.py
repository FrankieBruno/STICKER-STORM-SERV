from django.db import models


class Size(models.Model):
    id = models.AutoField(primary_key=True)
    sticker_size = models.IntegerField()