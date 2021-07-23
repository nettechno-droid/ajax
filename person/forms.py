from django import forms
from django.forms import fields
from person.models import PersonModel

class PersonForm(forms.ModelForm):
    class Meta:
        model = PersonModel
        fields = ('image','name','phone')