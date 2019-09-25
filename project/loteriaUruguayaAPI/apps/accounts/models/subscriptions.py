"""Subscription model"""

# Django
from django.db import models


class Subscription(models.Model):
	plans = (('FREE', 'Free Plan'), ('MONTHLY', 'Monthly Basic ($3/Mo)'), )
	subscription_id = models.AutoField(primary_key=True)
	subscription_stripe_customer_id = models.ForeignKey(
		'accounts.User',
		on_delete=models.CASCADE,
		related_name='subscriptions')
	subscription_is_active = models.BooleanField(default=False)
	subscription_plan_type = models.CharField(max_length=15, choices=plans, default='FREE')
	subscription_initiated_on = models.DateTimeField(null=True, blank=True)
	subscription_terminated_on = models.DateTimeField(null=True, blank=True)

	def __str__(self):
		return "{0} | {1}".format(self.subscription_stripe_customer_id, self.subscription_plan_type)