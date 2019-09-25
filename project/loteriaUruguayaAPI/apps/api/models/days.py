"""Day model"""

# Models
from django.db import models


class Day(models.Model):
	day_id = models.AutoField(primary_key=True)
	day_name = models.CharField(max_length=10, unique=True)

	def __str__(self):
		return self.day_name