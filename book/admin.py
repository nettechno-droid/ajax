from django.contrib import admin
from book.models import  BookModel
# Register your models here.

@admin.register(BookModel)
class GetBookAdmin(admin.ModelAdmin):
    list_display=['id','name','price']
