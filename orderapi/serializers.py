from rest_framework import serializers
from orderapi.models import Order, Customer, Item, Payment, BillingAddress, ShippingAddress, OrderItem

class CustomerSerializer(serializers.ModelSerializer):

	class Meta:
		model = Customer
		fields = ('first_name', 'last_name', 'email', 'phone')

class ItemSerializer(serializers.ModelSerializer):
	class Meta:
		model = Item
		fields = ('title', 'description', 'unit_price', 'SKU')

class PaymentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Payment
		fields = ('credit_card_company', 'credit_card_number', 'credit_card_ccv')

class BillingAddressSerializer(serializers.ModelSerializer):
	class Meta:
		model = BillingAddress
		fields = ('address1', 'address2', 'city', 'state', 'zipcode', 'country')

class ShippingAddressSerializer(serializers.ModelSerializer):
	class Meta:
		model = ShippingAddress
		fields = ('address1', 'address2', 'city', 'state', 'zipcode', 'country')

class OrderItemSerializer(serializers.HyperlinkedModelSerializer):
	item = ItemSerializer() 

	title = serializers.Field(source = 'title')
	description = serializers.Field(source = 'description')
	unit_price = serializers.Field(source = 'unit_price')
	SKU = serializers.Field(source = 'SKU')

	class Meta:
		model = OrderItem
		fields = ('quantity', 'title', 'description', 'unit_price', 'SKU')

class OrderSerializer(serializers.ModelSerializer):
	customer = CustomerSerializer()
	shipping_address = ShippingAddressSerializer()
	billing_address = BillingAddressSerializer()
	payment_details = PaymentSerializer()
	items = OrderItemSerializer(many=True)

	class Meta:
		model = Order
		fields = ('id', 'customer', 'items', 'total_price', 'subtotal_price', 'total_tax', 'order_date', 'shipping_address', 'billing_address', 'payment_details')		
