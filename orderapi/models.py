from django.db import models

class Customer(models.Model):
	first_name = models.CharField(max_length=100, null=True, blank=True)
	last_name = models.CharField(max_length=100, null=True, blank=True)
	email = models.EmailField(unique=True)
	phone = models.CharField(max_length=12, null=True, blank=True)

class Item(models.Model):
	title = models.CharField(max_length=1000, null=True, blank=True)
	description = models.TextField(null=True, blank=True)
	unit_price = models.DecimalField(max_digits=9, decimal_places=2, default=0)
	SKU = models.CharField(max_length=1000, null=True, blank=True)

class Payment(models.Model):
	credit_card_company = models.CharField(max_length=50, null=True, blank=True)
	credit_card_number = models.CharField(max_length=100, null=True, blank=True)
	credit_card_ccv = models.CharField(max_length=5, null=True, blank=True)

class BillingAddress(models.Model):
	address1 = models.CharField(max_length=1000, null=True, blank=True)
	address2 = models.CharField(max_length=1000, null=True, blank=True)
	city = models.CharField(max_length=100, null=True, blank=True)
	state = models.CharField(max_length=2, null=True, blank=True)
	zipcode = models.CharField(max_length=15, null=True, blank=True)
	country = models.CharField(max_length=100, default='USA')

class ShippingAddress(models.Model):
	address1 = models.CharField(max_length=1000, null=True, blank=True)
	address2 = models.CharField(max_length=1000, null=True, blank=True)
	city = models.CharField(max_length=100, null=True, blank=True)
	state = models.CharField(max_length=2, null=True, blank=True)
	zipcode = models.CharField(max_length=15, null=True, blank=True)
	country = models.CharField(max_length=100, default='USA')

class Order(models.Model):
	customer = models.ForeignKey(Customer, default=None, null=True)
	shipping_address = models.ForeignKey(ShippingAddress, default=None, null=True)
	billing_address = models.ForeignKey(BillingAddress, default=None, null=True)
	payment_details = models.ForeignKey(Payment, default=None, null=True)
	total_price = models.DecimalField(max_digits=9, decimal_places=2, default=0, null=True)
	subtotal_price = models.DecimalField(max_digits=9, decimal_places=2, default=0, null=True)
	total_tax = models.DecimalField(max_digits=9, decimal_places=2, default=0, null=True)
	order_date = models.DateTimeField(auto_now_add=True)

class OrderItem(models.Model):
	item = models.ForeignKey(Item, null=True, blank=True)
	quantity = models.IntegerField(default=1)
	order = models.ForeignKey(Order, related_name='items')

	@property
	def title(self):
		return self.item.title

	@property
	def description(self):
		return self.item.description

	@property
	def unit_price(self):
		return self.item.unit_price

	@property
	def SKU(self):
		return self.item.SKU

