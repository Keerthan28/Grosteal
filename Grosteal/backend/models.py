from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from re import T

# Create your models here.
class Users(models.Model):
	userId = models.CharField(null = False, max_length = 12 ,unique = True, blank = False,primary_key = True)
	userName = models.CharField(null = False, blank = False, max_length = 100)
	email = models.EmailField(null = False, blank = False, unique = True)
	phno = PhoneNumberField(null = False,blank = False,unique = True)
	address = models.TextField(null = False,blank = False)
	def __str__(self):
		return self.userId+" "+self.userName

class ProductCategory(models.Model):
	categoryId = models.CharField(null = False,unique = True,blank = False,max_length = 12,primary_key = True)
	categoryName = models.CharField(unique=True,null=False,blank=False,max_length=200)
	def __str__(self):
		return self.categoryId+" "+self.categoryName

class Product(models.Model):
	productId = models.CharField(null = False,unique = True,blank = False,max_length = 12,primary_key = True)
	productName = models.CharField(null=False,max_length = 200)
	productCategory = models.ForeignKey(ProductCategory,on_delete = models.CASCADE)
	productPrice = models.FloatField(null = False,blank = False)
	productStock = models.PositiveIntegerField(blank = False,null = True)
	productDesc = models.TextField(null = False, blank = False)
	productLoc = models.TextField(null = True, blank = True)
	def __str__(self):
		return self.productId+" "+self.productName

class Orders(models.Model):
	orderId = models.CharField(null = False,unique = True, blank = False, max_length = 64,primary_key = True)
	user = models.ForeignKey(Users,on_delete=models.CASCADE)
	orderQuantity = models.IntegerField(null=False,blank = False)
	orderDate = models.DateTimeField(null = False,blank = False)
	orderPhone = models.PositiveBigIntegerField(null = False, blank = False)
	orderStatus = models.BooleanField(null = True, blank = False)
	def __str__(self):
		return self.orderId

class OrderDetails(models.Model):
	product = models.ForeignKey(Product,on_delete = models.CASCADE)
	order = models.ForeignKey(Orders,on_delete = models.CASCADE)


