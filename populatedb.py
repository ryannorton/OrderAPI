from app.models import Order, Customer, Item, Payment, BillingAddress, ShippingAddress, OrderItem

def populate():
	customer = Customer()
	item = Item()
	payment = Payment()
	billingaddress = BillingAddress()
	shippingaddress = ShippingAddress()
	order = Order()
	orderitem = OrderItem()
	customer.first_name = 'Ryan'
	customer.last_name = 'Norton'
	customer.email = 'a'
	customer.email = 'nort.ryan@gmail.com'
	customer.phone = '915-630-2890'
	item.title = 'laptop'
	item.description = 'New 2012 Macbook Pro'
	item.unit_price = 2500.00
	item.SKU = 'ky4t234bil'
	payment.credit_card_company = 'VISA'
	payment.credit_card_number = '**** **** **** 4288'
	payment.credit_card_ccv = '**2'
	billingaddress.zipcode = '78705'
	billingaddress.city = 'Austin'
	billingaddress.state = 'TX'
	orderitem.item = item
	orderitem.order = order
	order.customer = customer
	order.shipping_address = shippingaddress
	order.billing_address = billingaddress
	order.payment_details = payment
	order.total_price = 2510.50
	order.subtotal_price = 2500.00
	order.total_tax = 10.50

	payment.save()
	customer.save()
	item.save()
	billingaddress.save()
	shippingaddress.save()
	order.customer = customer
	order.shipping_address = shippingaddress
	order.billing_address = billingaddress
	order.payment_details = payment
	order.save()
	orderitem.order = order
	orderitem.item = item
	orderitem.save()

populate()