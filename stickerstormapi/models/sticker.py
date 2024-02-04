from django.db import models
from django.contrib.auth.models import User

class Sticker(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    image = models.URLField()
    finish_type = models.ForeignKey("Finish", on_delete=models.CASCADE)
    sticker_size = models.ForeignKey("Size", on_delete=models.CASCADE)
    price = models.IntegerField()