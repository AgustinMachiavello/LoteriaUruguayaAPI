"""History model"""

# Models
from django.db import models


class History(models.Model):
	"""History model

	Represents the history of requests made by a user"""
	history_id = models.AutoField(primary_key=True)
	history_user_id = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='histories')

	def __str__(self):
		return "{0} | {1}".format(self.history_id, self.history_user_id)

	class Meta:
		unique_together = ('history_id', 'history_user_id')
