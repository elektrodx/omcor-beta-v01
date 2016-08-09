from __future__ import unicode_literals

from django.db import models
from clients.models import Client
from items.models import Item

class Status(models.Model):
	state = models.CharField(max_length=30)
	def __unicode__(self):
		return self.state

class Order(models.Model):
	client = models.ForeignKey(Client)
	date_order = models.DateField(auto_now=True)
	status = models.ForeignKey(Status)
	amount_total = models.DecimalField(max_digits=6, decimal_places=2)
	weight = models.DecimalField(max_digits=6, decimal_places=2)
	def __unicode__(self):
		return str(self.pk)

class OrderDetail(models.Model):
	order = models.ForeignKey(Order)
	item = models.ForeignKey(Item)
	qty = models.IntegerField()
	price = models.DecimalField(max_digits=6, decimal_places=2)

class OrderLog(models.Model):
	order = models.ForeignKey(Order)
	date = models.DateTimeField(auto_now_add=True)
	event = models.CharField(max_length=255)
	reference = models.CharField(max_length=255)
	document = models.ImageField(upload_to="media/order-log", blank=True)
	note = models.TextField(blank=True, null=True)

class OrderPayments(models.Model):
	order = models.ForeignKey(Order)
	date = models.DateTimeField(auto_now_add=True)
	amount = models.DecimalField(max_digits=6, decimal_places=2)
	concept = models.CharField(max_length=255)
	consignee = models.CharField(max_length=255)
	document = models.ImageField(upload_to="media/order-payment", blank=True)

