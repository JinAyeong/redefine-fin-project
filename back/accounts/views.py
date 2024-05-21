from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from dj_rest_auth.views import UserDetailsView

from .models import User
from .serializers import ProfileSerializer, UserInfoserializer, CustomRegisterSerializer


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
def add_product(request, product_cd):
    user = request.user
    
    if not user.financial_products:
        products = []
    else:
        products = user.financial_products.split(',')
    print(products)

    if product_cd in products:
        products.remove(product_cd)
    else:
        products.append(product_cd)
    
    user.financial_products = ','.join(products)

    user.save()
    return Response({'message': 'Product added to favorites'}, status=status.HTTP_201_CREATED)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_cart_status(request, fin_pdt):
    product = get_object_or_404(User, pk=fin_pdt)
    is_cart = fin_pdt in product.financial_products.all()
    return Response({'is_cart': is_cart})
