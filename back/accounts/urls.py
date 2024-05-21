from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile), # 회원정보 조회
    path('update/', views.profile_update), # 회원정보 수정
    path('delete/', views.profile_delete), # 회원 탈퇴
    path('add_product/<str:product_cd>/<str:option_trm>', views.add_product), # 관심상품 등록
    path('get_added_product/', views.get_added_product), # 관심상품 불러오기
    path('check_product/<str:product_cd>/<str:option_trm>', views.check_product), # 관심상품 등록 유무 확인
]