from django.db import models

class Customer(models.Model):
	first_name = models.CharField()
	last_name = models.CharField()
	email = models.EmailField(unique=True)
	phone = models.CharField()

class Item(models.Model):
	title = models.CharField()
	description = models.TextField()
	unit_price = models.DecimalField(decimal_places=2)
	SKU = models.CharField()

class Payment(models.Model):
	credit_card_company = models.CharField()
	credit_card_number = models.CharField()
	credit_card_ccv = models.CharField()

class Address(models.Model):
	address1 = models.CharField()
	address2 = models.CharField()
	city = models.CharField()
	state = models.CharField()
	zipcode = models.CharField()
	country = models.CharField(default='USA')

class Order(models.Model):
	customer = models.ForeignKey(Customer)
	shipping_address = models.ForeignKey(Address)
	billing_address = models.ForeignKey(Address)
	payment_details = models.ForeignKey(Payment)
	total_price = models.DecimalField(decimal_places=2)
	subtotal_price = models.DecimalField(decimal_places=2)
	total_tax = models.DecimalField(decimal_places=2)
	order_date = models.DateTimeField(auto_now_add=True)

class OrderItem(models.Model):
	item = models.ForeignKey(Item)
	quantity = models.IntegerField(default=1)
	order = models.ForeignKey(Order, related_name='items')