from django.shortcuts import render
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import UpdateModelMixin
from app.models import Product, UserProduct
from rest_framework.views import APIView
from app.serializers import ProductDetailSerializers, ReviewCreateSerializer, UserProductSerializers


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializers


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializers


class ReviewCreateView(APIView):
    """Добавление отзыва к продукту"""
    def post(self, request):
        review = ReviewCreateSerializer(data=request.data)
        if review.is_valid():
            review.save()
        return Response(status=201)


class UserProductView(UpdateModelMixin, GenericViewSet):
    queryset = UserProduct.objects.all()
    serializer_class = UserProductSerializers


