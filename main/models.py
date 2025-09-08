import uuid
from django.db import models

# Model disini
class Cleats(models.Model):
    SURFACE_TYPES = [
        ('FG', 'Firm Ground'), 
        ('AG', 'Artificial Grass'),
        ('MG', 'Multi Ground'),
        ('turf', 'Turf'),
        ('indoor', 'Indoor')
    ]
    
    name = models.CharField(max_length=255) #Nama yang terlalu panjang akan diberi keterangan di deskripsi
    brand = models.CharField(max_length=70)
    size = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    stock = models.IntegerField(default=0)
    rating = models.FloatField(default=0.0)
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=25, choices=SURFACE_TYPES, default='MG')
    is_featured = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    