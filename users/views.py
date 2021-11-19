from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import ListView
from django.views.generic.edit import ModelFormMixin
from django.http import JsonResponse
from .forms import UserRegisterForm
from .models import NetflixUser

class UserListView(ListView, ModelFormMixin):
	model = NetflixUser
	form_class = UserRegisterForm
	template_name = 'users/usersList.html'
	context_object_name = 'users'
	paginate_by = 1

	def get(self, request, *args, **kwargs):
		self.object = None
		self.form = self.get_form(self.form_class)
		return ListView.get(self, request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		self.object = None
		self.form = self.get_form(self.form_class)

		context = {'users': NetflixUser.objects.all()}
		if self.form.is_valid():
			user_token = str(self.form.save())
			print(user_token)
			data = f'http://localhost:8000/shop/{user_token}'
			messages.success(self.request, f"لینک معرفی: <a href='{data}'>{data}</a>")
			return redirect('users-list')
		else:
			context['form'] = self.form
			print(context['form'].errors)
			return render(request, self.template_name, context)