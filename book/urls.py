from django.urls import path
from book.views import Book,DeleteBook

app_name = "book"

urlpatterns = [
    path('',Book.as_view(),name='book'),
    path('books/<int:id>/' , DeleteBook.as_view() , name='deletebook')
]