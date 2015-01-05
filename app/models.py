"""
Definition of models.
"""

from django.db import models
from django.utils import timezone

# Create your models here.
class Url(models.Model):
	link = models.CharField(max_length =200)
	description = models.CharField(max_length = 200)
	created_date = models.DateTimeField(
		default = timezone.now)

	def __str__(self):
		return self.description