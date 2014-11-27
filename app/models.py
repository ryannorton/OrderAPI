from django.db import models

class Order(models.Model):
	orderID = models.CharField(blank=False, null=False)
	orderTime = models.DateTimeField()
