from __future__ import unicode_literals

from django.db import models

class Client(models.Model):
	name = models.CharField(max_length=100)
	fono = models.CharField(max_length=15)
	email = models.EmailField(max_length=254, blank=True)
	ci = models.CharField(max_length=15)
	address = models.CharField(max_length=256)
	def __unicode__(self):
		return self.name
