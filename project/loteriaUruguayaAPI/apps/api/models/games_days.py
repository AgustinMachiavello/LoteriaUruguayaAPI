"""Game days model for (n, n) relationship"""

# Models
from django.db import models


class GameUpdate(models.Model):
	"""Game update model

	N to N relationship between game and day"""
	game_update_game_id = models.ForeignKey('api.Game', on_delete=models.CASCADE)
	game_update_day_id = models.ForeignKey('api.Day', on_delete=models.CASCADE)
	game_update_time = models.TimeField()

	def __str__(self):
		return "{0} | {1}".format(self.game_update_game_id, self.game_update_day_id)