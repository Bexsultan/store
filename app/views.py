from django.shortcuts import render
from rest_framework import status
from rest_framework import generics
from app.models import Product
from app.serializers import ProductDetailSerializers



class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializers

class ProductDetail(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializers