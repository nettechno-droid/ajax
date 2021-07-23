from django.urls import path
from relationships.views import *
urlpatterns = [
    path('',Relation.as_view(),name='relaion'),
]