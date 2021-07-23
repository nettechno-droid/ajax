from django.contrib import admin
from person.models import PersonModel

# Register your models here.

@admin.register(PersonModel)
class GetPersonAdmin(admin.ModelAdmin):
  list_display=['id','name','phone']
