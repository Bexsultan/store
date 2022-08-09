from rest_framework import serializers
from .models import Product, Review, UserProduct


class ReviewCreateSerializer(serializers.ModelSerializer):
    """Добавление отзыва"""

    class Meta:
        model = Review
        fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):
    """Вывод отзыво"""

    class Meta:
        model = Review
        fields = ("name", "text")


class UserProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProduct
        fields = ('like', 'rate')


class ProductDetailSerializers(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True)

    class Meta:
        model = Product
        fields = '__all__'







