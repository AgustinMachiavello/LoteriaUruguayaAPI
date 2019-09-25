"""Request log model"""

# Models
from django.db import models

# Date and time
from django.utils import timezone


class RequestLog(models.Model):
	"""Request log model

	Represents a request made by a user"""
	request_log_id = models.AutoField(primary_key=True)
	request_log_history_id = models.ForeignKey(
		'accounts.History',
		on_delete=models.CASCADE,
		related_name='requestlogs')
	request_log_game_id = models.ForeignKey('api.Game', on_delete=models.CASCADE, related_name='requestlogs')
	request_log_date = models.DateField(default=timezone.datetime.today)
	request_log_time = models.TimeField(default=timezone.now)

	def __str__(self):
		return "{0} | {1}".format(self.request_log_history_id, self.request_log_date)