from django.db import models
from users.models import NetflixUser

class Customer(models.Model):
	email = models.EmailField(unique=True)
	cell_number = models.CharField(max_length=13, null=True, blank=True)
	name = models.CharField(max_length=100, null=True, blank=True)
	introducer = models.ForeignKey(NetflixUser, on_delete=models.SET_NULL, null=True, blank=True)

	def __str__(self):
		return self.email