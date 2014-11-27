from django.shortcuts import render
from django.http import HttpResponse
from app.models import Order
import json

orders = []

testOrder = {
	'orderID' : '1',
	'customerID' : '3471328947',
	'items' : [
		{
			'quantity' : 4,
			'price' : 10.00,
			'SKU' : 'sadofj',
		},
	],
	'createdTime' : 'testDate',
	'shippingLocation' : {
		'street' : 'testStreet',
		'zipcode' : '93843',
	},
	'billingLocation' : {
		'street' : 'testStreet',
		'zipcode' : '93843',
	},
	'price' : {
		'totalPrice' : '4.0',
		'tax' : '2.0',
		'shipping' : '1.0',
		'subTotal' : '3.0',
	},
}

orders.append(testOrder)

def index(request):
	return HttpResponse("it works")

def orderSummary(request, orderID):
	order = Order.objects.get(orderID=orderID)
	return HttpResponse(json.dumps(order), content_type="application/json")

	# for order in orders:
	# 	if order['orderID'] == orderID:
	# 		return HttpResponse(json.dumps(order), content_type="application/json")
	return HttpResponse("nope")
