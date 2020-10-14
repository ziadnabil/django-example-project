from django.db import models

# Create your models here.
class Product(models.Model):
    id = models.AutoField()
    name = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    description = models.TextField(null=True, blank=True)