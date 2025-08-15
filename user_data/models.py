
from django.db import models

class User(models.Model):
	username = models.CharField(max_length=150, unique=True)
	email = models.EmailField(unique=True)
	password = models.CharField(max_length=128)
	confirm_password = models.CharField(max_length=128)
	verification_code = models.CharField(max_length=6, blank=True, null=True)
	is_verified = models.BooleanField(default=False)

	def __str__(self):
		return self.username
