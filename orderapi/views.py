from django.shortcuts import render
from django.http import HttpResponse
from orderapi.models import Order, Customer
from orderapi.serializers import OrderSerializer, CustomerSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

def index(request):
	return HttpResponse("it works")

@api_view(['GET', 'POST'])
def orderList(request, format=None):
	"""
	List all orders, or create a new order.
	"""
	if request.method == 'GET':
		orders = Order.objects.all()
		serializer = OrderSerializer(orders, many=True)
		return Response(serializer.data)

	elif request.method == 'POST':
		serializer = OrderSerializer(data=request.DATA)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def orderDetailed(request, pk, format=None):
	"""
	Retrieve, update, or delete an order instance 
	"""
	try:
		order = Order.objects.get(id=pk)
	except:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer = OrderSerializer(order)
		return Response(serializer.data)

	elif request.method == 'PUT':
		serializer = OrderSerializer(order, data=request.DATA)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	elif request.method == 'DELETE':
		order.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def customerList(request, format=None):
	"""
	List all customers, or create a new customer.
	"""
	if request.method == 'GET':
		customers = Customer.objects.all()
		serializer = CustomerSerializer(customers, many=True)
		return Response(serializer.data)

	elif request.method == 'POST':
		serializer = CustomerSerializer(data=request.DATA)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def customerDetailed(request, pk, format=None):
	"""
	Retrieve, update, or delete a customer instance 
	"""
	try:
		customer = Customer.objects.get(id=pk)
	except:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer = CustomerSerializer(customer)
		return Response(serializer.data)

	elif request.method == 'PUT':
		serializer = CustomerSerializer(customer, data=request.DATA)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	elif request.method == 'DELETE':
		customer.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
