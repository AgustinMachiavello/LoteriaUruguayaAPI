"""Result model"""

# Models
from django.db import models

# Date and time
from django.utils import timezone

# Fields
from ..fields import fields


class Result(models.Model):
	"""Result model

	Stores the in day result of a lottery game
	"""
	result_id = models.AutoField(primary_key=True)
	result_game_id = models.ForeignKey('api.Game', on_delete=models.CASCADE, related_name='results')
	result_date = models.DateField(default=timezone.now)
	result_created_at = models.DateTimeField(default=timezone.now, editable=False)
	result_updated_at = models.DateTimeField(default=timezone.now, editable=False)

	def save(self, *args, **kwargs):
		if not self.result_id:
			self.created_at = timezone.now()
		self.updated_at = timezone.now()
		return super(Result, self).save(*args, **kwargs)


class VespertineNocturneResult(Result):
	"""Vespertine and nocturne result model

	Specialization of Result model where two lottery results are played in the same day"""
	vn_result_is_vespertine = models.BooleanField(null=False, blank=False)


class CincoDeOroResult(Result):
	"""Cinco de oro results

	Represents the lottery result format for the game 'Cinco de oro' """
	first_ball = fields.IntegerRangeField(min_value=1, max_value=48)
	second_ball = fields.IntegerRangeField(min_value=1, max_value=48)
	third_ball = fields.IntegerRangeField(min_value=1, max_value=48)
	fourth_ball = fields.IntegerRangeField(min_value=1, max_value=48)
	fifth_ball = fields.IntegerRangeField(min_value=1, max_value=48)
	sixth_ball = fields.IntegerRangeField(min_value=1, max_value=48)

	def __str__(self):
		return "{0} {1} {2} {3} {4} {5}".format(
			self.first_ball,
			self.second_ball,
			self.third_ball,
			self.fourth_ball,
			self.fifth_ball,
			self.sixth_ball,
		)
