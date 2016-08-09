from __future__ import unicode_literals

from django.db import models

class Item(models.Model):
	description = models.CharField(max_length=255)
	brand = models.CharField(max_length=255)
	code = models.CharField(max_length=30)
	picture = models.ImageField(upload_to="media/items")
	price = models.DecimalField(max_digits=6, decimal_places=2)
	weight = models.DecimalField(max_digits=6, decimal_places=2)
	
	def __unicode__(self):
		return self.description
