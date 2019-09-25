"""Custom user model"""

# Base User model
from django.contrib.auth.models import AbstractUser

# Models
from django.db import models

# Date and time
from django.utils import timezone

# random
import random

# hash libraries
import base64
import hashlib


class User(AbstractUser):
	user_id = models.AutoField(primary_key=True)
	# Why is email not ''user_email'? Because it should overwrite the abstract user field
	email = models.EmailField('Email', null=False, blank=False, editable=True, unique=True)
	user_is_verified = models.BooleanField(
		'Verified',
		default=True,
		help_text='Set to true when the user have verified its email address.')
	user_email_verification_token = models.TextField(blank=False, null=False, default="default", unique=True)
	is_administrator = models.BooleanField(default=False, editable=False)
	user_created_at = models.DateTimeField(default=timezone.now, editable=False)
	user_updated_at = models.DateTimeField(default=timezone.now, editable=False)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username', ]

	@staticmethod
	def generate_email_confirmation_token(email):
		"""Generates a pseudo-random token based on an email
		for email verification"""
		string_to_hash = email + str(timezone.now())
		hash_function = hashlib.sha1(string_to_hash.encode('utf-8'))
		hash_code = base64.urlsafe_b64encode(hash_function.digest())
		random_string_numbers = "{0}{1}{2}".format(
			str(random.randint(0, 999999)),
			str(random.randint(0, 999999)),
			str(random.randint(0, 999999)))
		return str(hash_code) + str(random_string_numbers)

	def deactivate(self):
		"""Invalidates token and verifies user"""
		self.user_is_verified = True
		self.save()
		return

	def save(self, *args, **kwargs):
		if not self.user_id:
			self.created_at = timezone.now()
			self.token = self.generate_email_confirmation_token(str(self.email))
		self.updated_at = timezone.now()
		return super(User, self).save(*args, **kwargs)

	def __str__(self):
		return self.username

	class Meta:
		verbose_name = "User"
		verbose_name_plural = "Users"