from django.db import models
from musician.models import *
# Create your models here.
class Album (models.Model):
    album_name = models.CharField(max_length=30)
    musician = models.ForeignKey(Musician,on_delete=models.CASCADE)
    release=models.DateField(auto_now_add=True)
    rating =models.IntegerField()
