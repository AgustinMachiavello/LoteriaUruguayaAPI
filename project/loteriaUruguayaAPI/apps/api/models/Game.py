"""Game abstract model"""

# Models
from django.db import models

# Date and time
from django.utils import timezone


class Game(models.Model):
	game_update_day_choices = (
		(1, "Monday"),
		(2, "Tuesday"),
		(3, "Wednesday"),
		(4, "Thursday"),
		(5, "Friday"),
		(6, "Saturday"),
		(7, "Sunday"),
	)
	game_id = models.AutoField(primary_key=True)
	game_name = models.CharField(primary_key=True, max_length=50)
	game_update_date = models.PositiveIntegerField(choices=game_update_day_choices)
	game_update_time = models.TimeField()
	game_created_at = models.DateTimeField(default=timezone.now, editable=False)
	game_updated_at = models.DateTimeField(default=timezone.now, editable=False)
	game_has_unique_result_per_day = models.BooleanField(null=False, blank=False)

	class Meta:
		abstract = True
