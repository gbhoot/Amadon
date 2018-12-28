from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=45)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image_link = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()