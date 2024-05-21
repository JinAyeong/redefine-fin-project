from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from dj_rest_auth.views import UserDetailsView

from .models import User
from .serializers import ProfileSerializer, UserInfoserializer, CustomRegisterSerializer
from finances.serializers import *


# 회원정보 조회
@api_view(['GET'])
# @authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def profile(request):
    user = request.user
    serializer = ProfileSerializer(user)
    return Response(serializer.data)


# 회원정보 수정
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def profile_update(request):
    user = request.user
    serializer = UserInfoserializer(user, data=request.data, partial=True)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        # serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# 회원 탈퇴
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def profile_delete(request):
    request.user.delete()
    return Response({'delete': '탈퇴가 완료되었습니다.'}, status=status.HTTP_204_NO_CONTENT)


# 관심상품 버튼 클릭
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_product(request, product_cd, option_trm):
    user = request.user
    
    if not user.financial_products:
        products = []
    else:
        products = user.financial_products.split(',')

    elem = f'{product_cd}/{option_trm}'

    if elem in products:
        products.remove(elem)
    else:
        products.append(elem)
    
    user.financial_products = ','.join(products)

    user.save()
    return Response({'message': 'Product added to favorites'}, status=status.HTTP_201_CREATED)


# 관심상품 출력
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_added_product(request):
    user = request.user

    if not user.financial_products:
        products = []
    else:
        products = user.financial_products.split(',')

    product_details = []
    
    for product in products:
        product_cd, option_trm = product.split('/')
        try:
            # DepositProducts에서 제품을 찾으려고 시도
            deposit_product = DepositProducts.objects.get(fin_prdt_cd=product_cd)
            deposit_options = DepositOptions.objects.get(product=deposit_product, save_trm=option_trm)

            product_data = {
                'product': DepositProductsSerializer(deposit_product).data,
                'options': DepositOptionsSerializer(deposit_options).data,
            }
            product_details.append(product_data)

        except DepositProducts.DoesNotExist:
            # DepositProducts에 제품이 없으면 SavingProducts에서 찾음
            try:
                saving_product = SavingProducts.objects.get(fin_prdt_cd=product_cd)
                saving_options = SavingOptions.objects.filter(product=saving_product, save_trm=option_trm).first()

                product_data = {
                    'product': SavingProductsSerializer(saving_product).data,
                    'options': SavingOptionsSerializer(saving_options).data,
                }
                product_details.append(product_data)
            except SavingProducts.DoesNotExist:
                continue

    return Response(product_details, status=status.HTTP_200_OK)


# 관심상품 등록 유무 확인
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def check_product(request, product_cd, option_trm):
    user = request.user
    
    if not user.financial_products:
        return Response(False)
    else:
        products = user.financial_products.split(',')

    elem = f'{product_cd}/{option_trm}'

    if elem in products:
        return Response(True)
    return Response(False)