from django.db.models import fields
from rest_framework import serializers
from .models import *

class ProductCategorySerializer(serializers.ModelSerializer) :
	class Meta:
		fields = '__all__'
		model = ProductCategory

class ProductSerializer(serializers.ModelSerializer) :
	class Meta:
		fields = '__all__'
		model = Product
class OrderSerializer(serializers.ModelSerializer) :
	class Meta:
		fields = '__all__'
		model = Orders
class OrderDetailSerializer(serializers.ModelSerializer) :
	class Meta:
		fields = '__all__'
		model = OrderDetails

class UserSerializer(serializers.ModelSerializer) :
	class Meta:
		fields = '__all__'
		model = Users
