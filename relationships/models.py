from django.db import models

# Create your models here.
class Person(models.Model):
    name=models.TextField(max_length=100)
    email = models.EmailField()

    def __str__(self) -> str:
        return self.name

class Adhar(models.Model):
    person = models.OneToOneField("Person",on_delete=models.CASCADE)
    signature = models.TextField(max_length=100)
    adhar_no = models.TextField(max_length=100)

    def __str__(self) -> str:
        return self.id


class  Account(models.Model):
    person = models.ForeignKey("Person",on_delete=models.CASCADE)
    acc_no = models.TextField(max_length=100)

    def __str__(self) -> str:
        return self.acc_no


class Products(models.Model):
    person = models.ManyToManyField("Person")
    product_name=models.TextField(max_length=100)
    product_quantity = models.TextField(max_length=100)

    def __str__(self):
        return self.product_name
    



    