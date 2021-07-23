from django.db import models

# Create your models here.

class BookModel(models.Model):
    image = models.ImageField(upload_to = 'media',null=True,blank=True)
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    price = models.CharField(max_length=10)
    



