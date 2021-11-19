from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import NetflixUser

class UserRegisterForm(UserCreationForm):
	email = forms.EmailField(
		error_messages={
		'invalid': 'آدرس ایمیل درست نیست!',
		'required': 'لطفا آدرس ایمیل را وارد کنید!',
		'unique': 'آدرس ایمیل تکراری است!',
		})
	first_name = forms.CharField(required=False)
	last_name = forms.CharField(required=False)
	user_type = forms.CharField()

	class Meta:
		model = NetflixUser
		fields = ['email', 'password1', 'password2', 'first_name', 'last_name', 'user_type']

class CustomUserChangeForm(UserChangeForm):
	email = forms.EmailField()
	first_name = forms.CharField(required=False)
	last_name = forms.CharField(required=False)
	user_type = forms.CharField()

	class Meta:
		model = NetflixUser
		fields = ['email', 'first_name', 'last_name', 'user_type']