from django.urls import path
from person.views import *

app_name = "person"

urlpatterns = [

    path('person-view/',PersonView.as_view(),name='person-view'),
    path('person-view/<int:id>/',PersonDelete.as_view(),name='person-delete')
    
]
