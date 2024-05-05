from django.db import models

# Create your models here.

class Destination(models.Model): # converting class to models
    
    name = models.CharField(max_length=100) # type: ignore
    img = models.ImageField(upload_to='pics') # type: ignore
    desc = models.TextField() # type: ignore
    prise = models.IntegerField() # type: ignore
    review = models.IntegerField() # type: ignore
    days = models.IntegerField() # type: ignore