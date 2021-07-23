from django.contrib import admin
from relationships.models import Account, Person,Adhar, Products

# Register your models here.
admin.site.register(Person)
admin.site.register(Adhar)
admin.site.register(Account)
admin.site.register(Products)
