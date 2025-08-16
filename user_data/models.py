
from django.db import models

class User(models.Model):
	username = models.CharField(max_length=150, unique=True)
	email = models.EmailField(unique=True)
	password = models.CharField(max_length=128)
	confirm_password = models.CharField(max_length=128)
	verification_code = models.CharField(max_length=6, blank=True, null=True)
	is_verified = models.BooleanField(default=False)
	profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
	bio = models.TextField(blank=True, null=True)
	birthdate = models.DateField(blank=True, null=True)
	birth_time = models.TimeField(blank=True, null=True)

	def __str__(self):
		return self.username
