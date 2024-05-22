from django.db.models import Q
import requests
from django.conf import settings
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from accounts.models import User
from .serializers import DepositProductsSerializer, DepositOptionsSerializer, SavingProductsSerializer, SavingOptionsSerializer
from .models import DepositProducts, DepositOptions, SavingProducts, SavingOptions
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
        
        # 이미 존재하는지 확인
        if DepositProducts.objects.filter(fin_prdt_cd=fin_prdt_cd).exists():
            continue  # 이미 존재하면 건너뛰기

        dcls_month = products.get('dcls_month')
        fin_co_no = products.get('fin_co_no')
        kor_co_nm = products.get('kor_co_nm')
        fin_prdt_nm = products.get('fin_prdt_nm')
        join_way = products.get('join_way')
        mtrt_int = products.get('mtrt_int')
        spcl_cnd = products.get('spcl_cnd')
        join_deny = products.get('join_deny')
        join_member = products.get('join_member')
        etc_note = products.get('etc_note')
        max_limit = products.get('max_limit')
        dcls_strt_day = products.get('dcls_strt_day')
        dcls_end_day = products.get('dcls_end_day')
        fin_co_subm_day = products.get('fin_co_subm_day')
        

        save_data = {
            'dcls_month': dcls_month,
            'fin_co_no': fin_co_no,
            'kor_co_nm': kor_co_nm,
            'fin_prdt_cd': fin_prdt_cd,
            'fin_prdt_nm': fin_prdt_nm,
            'join_way': join_way,
            'mtrt_int': mtrt_int,
            'spcl_cnd': spcl_cnd,
            'join_deny': join_deny,
            'join_member': join_member,
            'etc_note': etc_note,
            'max_limit': max_limit,
            'dcls_strt_day': dcls_strt_day,
            'dcls_end_day': dcls_end_day,
            'fin_co_subm_day': fin_co_subm_day,
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

        # 이미 존재하는지 확인
        if DepositOptions.objects.filter(fin_prdt_cd=fin_prdt_cd, intr_rate_type_nm=intr_rate_type_nm, intr_rate=intr_rate, intr_rate2=intr_rate2, save_trm=save_trm).exists():
            continue  # 이미 존재하면 건너뛰기

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



# get: 전체 정기예금 상품 목록 반환
@api_view(['GET'])
def deposit_products(request):
    deposit_products = DepositProducts.objects.all()
    serializers = DepositProductsSerializer(deposit_products, many=True)
    return Response(serializers.data)



# 특정 예금 상품의 옵션 리스트 반환
@api_view(['GET'])
def deposit_products_options(request, fin_prdt_cd):
    deposit_options = DepositOptions.objects.filter(fin_prdt_cd=fin_prdt_cd)
    serializers = DepositOptionsSerializer(deposit_options, many=True)
    return Response(serializers.data)


# # 특정 예금 상품의 옵션 리스트 반환 (은행 필터)
# @api_view(['GET'])
# def deposit_option_filter(request, cor_co_nm):
#     deposit_options = DepositOptions.objects.filter(cor_co_nm=cor_co_nm)
#     serializers = DepositOptionsSerializer(deposit_options, many=True)
#     return Response(serializers.data)


import logging

logger = logging.getLogger(__name__)

@api_view(['GET'])
def deposit_products_filter(request):
    bank_name = request.GET.get('bank_name', None)
    logger.debug(f"Received bank_name: {bank_name}")
    try:
        if bank_name:
            products = DepositProducts.objects.filter(kor_co_nm=bank_name)
        else:
            products = DepositProducts.objects.all()
        serializer = DepositProductsSerializer(products, many=True)
        return Response(serializer.data)
    except Exception as e:
        logger.error(f"Error fetching deposit products: {e}")
        return Response({"error": str(e)}, status=500)


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


# 적금 상품 목록 데이터를 get -> 적금 상품 목록과 옵션 목록 -> DB에 저장
@api_view(['GET'])
def save_saving_products(request):
    url = f'http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json?auth={DEPOSIT_API}&topFinGrpNo=020000&pageNo=1'
    response = requests.get(url).json()

    # 적금 상품 목록 저장
    for products in response.get('result').get('baseList'):
        fin_prdt_cd = products.get('fin_prdt_cd')
        
        # 이미 존재하는지 확인
        if SavingProducts.objects.filter(fin_prdt_cd=fin_prdt_cd).exists():
            continue  # 이미 존재하면 건너뛰기

        dcls_month = products.get('dcls_month')
        fin_co_no = products.get('fin_co_no')
        kor_co_nm = products.get('kor_co_nm')
        fin_prdt_nm = products.get('fin_prdt_nm')
        join_way = products.get('join_way')
        mtrt_int = products.get('mtrt_int')
        spcl_cnd = products.get('spcl_cnd')
        join_deny = products.get('join_deny')
        join_member = products.get('join_member')
        etc_note = products.get('etc_note')
        max_limit = products.get('max_limit')
        dcls_strt_day = products.get('dcls_strt_day')
        fin_co_subm_day = products.get('fin_co_subm_day')
        

        save_data = {
            'dcls_month': dcls_month,
            'fin_co_no': fin_co_no,
            'kor_co_nm': kor_co_nm,
            'fin_prdt_cd': fin_prdt_cd,
            'fin_prdt_nm': fin_prdt_nm,
            'join_way': join_way,
            'mtrt_int': mtrt_int,
            'spcl_cnd': spcl_cnd,
            'join_deny': join_deny,
            'join_member': join_member,
            'etc_note': etc_note,
            'max_limit': max_limit,
            'dcls_strt_day': dcls_strt_day,
            'fin_co_subm_day': fin_co_subm_day,
        }

        serializer = SavingProductsSerializer(data=save_data)
        # 유효성 검증
        if serializer.is_valid(raise_exception=True):
            # 유효하다면, 저장
            serializer.save()

    # 적금 옵션 목록 저장
    for options in response.get('result').get('optionList'):
        fin_prdt_cd = options.get('fin_prdt_cd')
        intr_rate_type = options.get('intr_rate_type')
        intr_rate_type_nm = options.get('intr_rate_type_nm')
        rsrv_type = options.get('rsrv_type')
        rsrv_type_nm = options.get('rsrv_type_nm')
        save_trm = options.get('save_trm')
        intr_rate = options.get('intr_rate')
        intr_rate2 = options.get('intr_rate2')


        # 이미 존재하는지 확인
        if SavingOptions.objects.filter(fin_prdt_cd=fin_prdt_cd, intr_rate_type_nm=intr_rate_type_nm, intr_rate=intr_rate, intr_rate2=intr_rate2, save_trm=save_trm).exists():
            continue  # 이미 존재하면 건너뛰기

        save_data = {
            'fin_prdt_cd': fin_prdt_cd,
            'intr_rate_type': intr_rate_type,
            'fin_prdt_cd': fin_prdt_cd,
            'intr_rate_type_nm': intr_rate_type_nm,
            'rsrv_type': rsrv_type,
            'rsrv_type_nm': rsrv_type_nm,
            'intr_rate': intr_rate,
            'intr_rate2': intr_rate2,
            'save_trm': save_trm,
        }

        product = SavingProducts.objects.get(fin_prdt_cd=fin_prdt_cd)
        serializer = SavingOptionsSerializer(data=save_data)
        # 유효성 검증
        if serializer.is_valid(raise_exception=True):
            # 유효하다면, 저장
            serializer.save(product=product)

    return JsonResponse(response)


# get: 전체 적금 상품 목록 반환, post: 상품 데이터 저장
@api_view(['GET'])
def saving_products(request):
    saving_products = SavingProducts.objects.all()
    serializers = SavingProductsSerializer(saving_products, many=True)
    return Response(serializers.data)



# 특정 예금 상품의 옵션 리스트 반환
@api_view(['GET'])
def saving_products_options(request, fin_prdt_cd):
    deposit_options = SavingOptions.objects.filter(fin_prdt_cd=fin_prdt_cd)
    serializers = SavingOptionsSerializer(deposit_options, many=True)
    return Response(serializers.data)



# 특정 예금 상품의 옵션 리스트 반환 (filter)
import logging

logger = logging.getLogger(__name__)

@api_view(['GET'])
def saving_products_filter(request):
    bank_name = request.GET.get('bank_name', None)
    logger.debug(f"Received bank_name: {bank_name}")
    try:
        if bank_name:
            products = SavingProducts.objects.filter(kor_co_nm=bank_name)
        else:
            products = SavingProducts.objects.all()
        serializer = SavingProductsSerializer(products, many=True)
        return Response(serializer.data)
    except Exception as e:
        logger.error(f"Error fetching saving products: {e}")
        return Response({"error": str(e)}, status=500)
    

# 나와 비슷한 사람들이 많이 가입한 상품 찾기
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def recommend_similar_product(request):
    age = request.user.age
    money = request.user.money
    salary = request.user.salary
    age_scope = 5
    money_scope = 1000000
    salary_scope = 1500000

    correct_users = User.objects.filter(
        Q(age__range=(age - age_scope, age + age_scope)) &
        Q(money__range=(money - money_scope, money + money_scope)) &
        Q(salary__range=(salary - salary_scope, salary + salary_scope)) &
        ~Q(id=request.user.id)  # 나 자신을 제외
    )

    # 가입한 상품 목록 리스트로 변환
    product_lists = correct_users.values_list('financial_products', flat=True)
    
    # 상품 목록을 하나의 리스트로 통합
    all_products = []
    for product_list in product_lists:
        if product_list:
            all_products.extend(product_list.split(','))

    # 상품별 가입자 수를 계산
    from collections import Counter
    product_counter = Counter(all_products)

    # 가장 많이 가입한 상품 상위 5개 반환
    most_common_products = product_counter.most_common(5)

    return Response({
        'most_common_products': most_common_products
    })