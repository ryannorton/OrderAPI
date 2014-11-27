from django.shortcuts import render
from django.http import HttpResponse
from orderapi.models import Order

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from orderapi.serializers import OrderSerializer

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


