from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from app.models import Product
from app.serializers import ProductDetailSerializers


class ProductList(APIView):
    def get(self,request):
        products = Product.objects.all()
        serializer = ProductDetailSerializers(products,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ProductDetail(APIView):
    def get(self,request,pk):
        product = Product.objects.get(pk)
        serializer = ProductDetailSerializers(product)
        return Response(serializer.data, status=status.HTTP_200_OK)