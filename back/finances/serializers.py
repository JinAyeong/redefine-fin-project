from rest_framework import serializers
from .models import DepositProducts, DepositOptions


# 예금 상품
class DepositProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositProducts
        fields = '__all__'

# 예금 옵션
class DepositOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositOptions
        fields = '__all__'
        read_only_fields = ('product',)  # 읽기전용으로 열기
