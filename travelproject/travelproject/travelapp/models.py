from django.db import models


# Create your models here.
class time (models.Model):
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='pics')
    desc = models.IntegerField()
