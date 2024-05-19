import requests
from django.conf import settings
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import DepositProductsSerializer, DepositOptionsSerializer
from .models import DepositProducts, DepositOptions
from redefine_fin_project.settings import DEPOSIT_API
# from django.db.models import Max

# 정기예금 상품 목록 데이터를 get -> 정기예금 상품 목록과 옵션 목록 -> DB에 저장
@api_view(['GET'])
def save_deposit_products(request):
    url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={DEPOSIT_API}&topFinGrpNo=020000&pageNo=1'
    response = requests.get(url).json()

    # 정기예금 상품 목록 저장
    for products in response.get('result').get('baseList'):
        fin_prdt_cd = products.get('fin_prdt_cd')
        kor_co_nm = products.get('kor_co_nm')
        fin_prdt_nm = products.get('fin_prdt_nm')
        etc_note = products.get('etc_note')
        join_deny = products.get('join_deny')
        join_member = products.get('join_member')
        join_way = products.get('join_way')
        spcl_cnd = products.get('spcl_cnd')

        save_data = {
            'fin_prdt_cd': fin_prdt_cd,
            'kor_co_nm': kor_co_nm,
            'fin_prdt_nm': fin_prdt_nm,
            'etc_note': etc_note,
            'join_deny': join_deny,
            'join_member': join_member,
            'join_way': join_way,
            'spcl_cnd': spcl_cnd,
        }

        serializer = DepositProductsSerializer(data=save_data)
        # 유효성 검증
        if serializer.is_valid(raise_exception=True):
            # 유효하다면, 저장
            serializer.save()

    # 정기예금 옵션 목록 저장
    for options in response.get('result').get('optionList'):
        fin_prdt_cd = options.get('fin_prdt_cd')
        intr_rate_type_nm = options.get('intr_rate_type_nm')
        intr_rate = options.get('intr_rate')
        intr_rate2 = options.get('intr_rate2')
        save_trm = options.get('save_trm')

        save_data = {
            'fin_prdt_cd': fin_prdt_cd,
            'intr_rate_type_nm': intr_rate_type_nm,
            'intr_rate': intr_rate,
            'intr_rate2': intr_rate2,
            'save_trm': save_trm,
        }

        product = DepositProducts.objects.get(fin_prdt_cd=fin_prdt_cd)
        serializer = DepositOptionsSerializer(data=save_data)
        # 유효성 검증
        if serializer.is_valid(raise_exception=True):
            # 유효하다면, 저장
            serializer.save(product=product)

    return JsonResponse(response)


# get: 전체 정기예금 상품 목록 반환, post: 상품 데이터 저장
@api_view(['GET', 'POST'])
def deposit_products(request):

    if request.method == 'GET':
        deposit_products = DepositProducts.objects.all()
        serializers = DepositProductsSerializer(deposit_products, many=True)
        return Response(serializers.data)
    
    elif request.method == 'POST':
        serializer = DepositProductsSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=201)
        
        else:
            return Response({"message": "이미 있는 데이터이거나, 데이터가 잘못 입력되었습니다."})


# 특정 상품의 옵력 리스트 반환
@api_view(['GET'])
def deposit_products_options(request, fin_prdt_cd):
    deposit_options = DepositOptions.objects.filter(fin_prdt_cd=fin_prdt_cd)
    serializers = DepositOptionsSerializer(deposit_options, many=True)
    return Response(serializers.data)


# 가입 기간에 상관없이 금리가 가장 높은 상품과 해당 상품의 옵션 리스트 출력
@api_view(['GET'])
def top_rate(request):
    # 금리가 가장 높은 옵션 찾기
    max_intr_rate2 = DepositOptions.objects.aggregate(intr_rate2=Max('intr_rate2'))
    deposit_options = DepositOptions.objects.filter(intr_rate2=max_intr_rate2['intr_rate2'])
    option_serializers = DepositOptionsSerializer(deposit_options, many=True)

    # 금리가 가장 높은 옵션의 상품 찾기
    product = DepositProducts.objects.get(fin_prdt_cd=deposit_options[0].fin_prdt_cd)
    product_serializers = DepositProductsSerializer(product)

    result = {
        'deposit_product': product_serializers.data,
        'options': option_serializers.data
    }

    return Response(result)
