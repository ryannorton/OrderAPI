from django.db import models

class Customer(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	email = models.EmailField(unique=True)
	phone = models.CharField(max_length=12)

class Item(models.Model):
	title = models.CharField(max_length=1000)
	description = models.TextField()
	unit_price = models.DecimalField(max_digits=9, decimal_places=2)
	SKU = models.CharField(max_length=1000)

class Payment(models.Model):
	credit_card_company = models.CharField(max_length=50)
	credit_card_number = models.CharField(max_length=100)
	credit_card_ccv = models.CharField(max_length=5)

class BillingAddress(models.Model):
	address1 = models.CharField(max_length=1000)
	address2 = models.CharField(max_length=1000)
	city = models.CharField(max_length=100)
	state = models.CharField(max_length=2)
	zipcode = models.CharField(max_length=15)
	country = models.CharField(max_length=100, default='USA')

class ShippingAddress(models.Model):
	address1 = models.CharField(max_length=1000)
	address2 = models.CharField(max_length=1000)
	city = models.CharField(max_length=100)
	state = models.CharField(max_length=2)
	zipcode = models.CharField(max_length=15)
	country = models.CharField(max_length=100, default='USA')

class Order(models.Model):
	customer = models.ForeignKey(Customer)
	shipping_address = models.ForeignKey(ShippingAddress)
	billing_address = models.ForeignKey(BillingAddress)
	payment_details = models.ForeignKey(Payment)
	total_price = models.DecimalField(max_digits=9 ,decimal_places=2)
	subtotal_price = models.DecimalField(max_digits=9, decimal_places=2)
	total_tax = models.DecimalField(max_digits=9, decimal_places=2)
	order_date = models.DateTimeField(auto_now_add=True)

class OrderItem(models.Model):
	item = models.ForeignKey(Item)
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

