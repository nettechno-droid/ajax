from django.db import models

# Create your models here.

class PersonModel(models.Model):
    image  = models.ImageField(upload_to='media/person',null=True,blank=True)
    name   = models.CharField(max_length=100)
    phone  = models.IntegerField()

