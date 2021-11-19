from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager
import uuid


class NetflixUser(AbstractBaseUser, PermissionsMixin):
	email = models.EmailField(_('email address'), unique=True)
	is_staff = models.BooleanField(default=False)
	is_active = models.BooleanField(default=True)
	date_joined = models.DateTimeField(default=timezone.now)
	user_token = models.CharField(max_length=8, primary_key=True, default=str(uuid.uuid4().hex[:8]), editable=False)
	score = models.IntegerField(default=0, null=True, blank=True)
	user_type = models.CharField(max_length=100, default=None, null=True, blank=True)
	first_name = models.CharField(max_length=100, default=None, null=True, blank=True)
	last_name = models.CharField(max_length=100, default=None, null=True, blank=True)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []

	objects = CustomUserManager()

	def __str__(self):
		return self.user_token

	def save(self, *args, **kwargs):
		super(NetflixUser, self).save(*args, **kwargs)

	@property
	def earn_score(self):
		score = self.score + 1
		return score