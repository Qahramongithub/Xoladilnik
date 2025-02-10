from rest_framework import serializers
from apps.models import Product, Brand


class BrandCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'

