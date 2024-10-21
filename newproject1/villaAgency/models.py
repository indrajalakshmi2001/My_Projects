from django.db import models

# Create your models here.
class Destination(models.Model):
    
    name = models.CharField(max_length=100)
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    area = models.IntegerField()
    floor = models.IntegerField()
    parking = models.IntegerField()
    price = models.IntegerField()
    img = models.ImageField(upload_to='pics')
    offer = models.BooleanField(default=False) 