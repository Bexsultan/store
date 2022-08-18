from rest_framework import serializers
from .models import Product, Review, UserProduct


class FilterReviewListSerializer(serializers.ListSerializer):
    """Фильтр комментариев, только parents"""
    def to_representation(self, data):
        data = data.filter(parent=None)
        return super().to_representation(data)


class RecursiveSerializer(serializers.Serializer):
    """Вывод рекурсивно children"""
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class ReviewCreateSerializer(serializers.ModelSerializer):
    """Добавление отзыва"""

    class Meta:
        model = Review
        fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):
    """Вывод отзыво"""
    children = RecursiveSerializer(many=True)

    class Meta:
        list_serializer_class = FilterReviewListSerializer
        model = Review
        fields = ("name", "text","children")


class UserProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProduct
        fields = "__all__"


class ProductDetailSerializers(serializers.ModelSerializer):
    # reviews = ReviewSerializer(many=True, read_only=True)
    # rates = UserProductSerializers(many=True, read_only=True)
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['reviews'] = ReviewSerializer(instance.reviews.all(), many=True, context=self.context).data
        representation['rates'] = UserProductSerializers(instance.rates.all(), many=True, context=self.context).data
        return representation
    class Meta:
        model = Product
        fields = '__all__'







