from django.urls import path
from django.urls.resolvers import URLPattern
from .views import *
urlpatterns = [
     path("ProductCategory",ListProductCategory.as_view(),name = "ProductCategory"),
     path("Product",ListProduct.as_view(),name = "Product"),
     path("Orders",ListOrder.as_view(),name = "Orders"),
     path("OrderDetails",ListOrderDetails.as_view(),name = "OrderDetails"),
     path("Users",ListUsers.as_view(),name = "Users"),

]

