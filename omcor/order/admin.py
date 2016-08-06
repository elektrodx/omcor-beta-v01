from django.contrib import admin
from .models import *

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
	list_display = ('client', 'date_order', 'status', 'amount_total', 'weight')

@admin.register(OrderDetail)
class OrderDetailAdmin(admin.ModelAdmin):
	list_display = ('order', 'item', 'qty', 'price')

@admin.register(OrderLog)
class OrderLogAdmin(admin.ModelAdmin):
	list_display = ('order', 'date', 'event', 'reference', 'note')

@admin.register(OrderPayments)
class OrderPaymentsAdmin(admin.ModelAdmin):
	list_display = ('order', 'date', 'amount', 'concept', 'consignee')

@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
	list_display = ('state',)