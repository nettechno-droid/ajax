from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import User


class UserForm(forms.ModelForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password")

class LoginForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ("email", "password")