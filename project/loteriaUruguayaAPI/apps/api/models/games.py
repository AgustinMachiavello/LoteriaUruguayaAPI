"""Game abstract model"""

# Models
from django.db import models

# Date and time
from django.utils import timezone


class Game(models.Model):
	"""Game model

	Represents de lottery game
	"""
	game_id = models.AutoField(primary_key=True)
	game_name = models.CharField(max_length=50, unique=True)
	game_created_at = models.DateTimeField(default=timezone.now, editable=False)
	game_updated_at = models.DateTimeField(default=timezone.now, editable=False)
	game_has_unique_result_per_day = models.BooleanField(null=False, blank=False)

	def __str__(self):
		return "{0}".format(self.game_name)

	def save(self, *args, **kwargs):
		if not self.game_id:
			self.created_at = timezone.now()
		self.updated_at = timezone.now()
		return super(Game, self).save(*args, **kwargs)

	class Meta:
		ordering = ["-game_id", "-game_created_at", ]