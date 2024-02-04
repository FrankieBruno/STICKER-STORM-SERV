from django.db import models

class Finish(models.Model):
    id = models.AutoField(primary_key=True)
    finish_type = models.CharField(max_length=55)