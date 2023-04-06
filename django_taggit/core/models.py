from django.db import models
from taggit.managers import TaggableManager

# Create your models here.
class Items(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=500)
    brand= models.CharField(max_length=128)

    tags = TaggableManager()

    def __str__(self):
        return self.name
    