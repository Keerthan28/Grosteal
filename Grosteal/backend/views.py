from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework import generics

# Create your views here.
class ListProductCategory(generics.ListCreateAPIView):
	queryset = ProductCategory.objects.all()
	serializer_class = ProductCategorySerializer

class DetailProductCategory(generics.RetrieveUpdateDestroyAPIView):
	queryset = ProductCategory.objects.all()
	serializer_class = ProductCategorySerializer

class ListProduct(generics.ListCreateAPIView):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer

class DetailProduct(generics.RetrieveUpdateDestroyAPIView):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer

class ListOrder(generics.ListCreateAPIView):
	queryset = Orders.objects.all()
	serializer_class = OrderSerializer

class DetailOrder(generics.RetrieveUpdateDestroyAPIView):
	queryset = Orders.objects.all()
	serializer_class = OrderSerializer

class ListOrderDetails(generics.ListCreateAPIView):
	queryset = OrderDetails.objects.all()
	serializer_class = OrderDetailSerializer

class DetailOrderDetails(generics.RetrieveUpdateDestroyAPIView):
	queryset = OrderDetails.objects.all()
	serializer_class = OrderDetailSerializer

class ListUsers(generics.ListCreateAPIView):
	queryset = Users.objects.all()
	serializer_class = UserSerializer

class DetailUsers(generics.RetrieveUpdateDestroyAPIView):
	queryset = Users.objects.all()
	serializer_class = UserSerializer