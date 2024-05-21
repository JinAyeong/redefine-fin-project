from django.urls import path
from . import views

urlpatterns = [
    # 정기예금 상품 목록 DB에 저장
    path('save-deposit-products/', views.save_deposit_products),
    # 전체 정기예금 상품 목록 출력 & 데이터 삽입
    path('deposit-products/', views.deposit_products),
    # 특정 예금 상품의 옵션 리스트 출력
    path('deposit-products-options/<str:fin_prdt_cd>/', views.deposit_products_options),
    # 특정 예금 상품의 옵션 리스트 출력 (filter)
    path('deposit-products-filter/', views.deposit_products_filter),
    # 가입 기간에 상관없이 최고 금리가 가장 높은 금융 삼품과 해당 상품의 옵션 리스트 출력
    path('deposit-products/top_rate/', views.top_rate),

    # 적금 상품 목록 DB에 저장
    path('save-saving-products/', views.save_saving_products),
    # 전체 적금 상품 목록 출력 & 데이터 삽입
    path('saving-products/', views.saving_products),
    # 특정 예금 상품의 옵션 리스트 출력 (filter)
    path('saving-products-filter/', views.saving_products_filter),
    # 특정 적금 상품의 옵션 리스트 출력
    path('saving-products-options/<str:fin_prdt_cd>/', views.saving_products_options),
]