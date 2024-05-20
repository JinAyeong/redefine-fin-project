from django.db import models


# 예금 상품 목록
class DepositProducts(models.Model):
    fin_prdt_cd = models.TextField(unique=True)  # 금융 상품 코드
    kor_co_nm = models.TextField(null=True)      # 금융회사명
    fin_prdt_nm = models.TextField(null=True)    # 금융 상품명
    etc_note = models.TextField(null=True)       # 금융 상품 설명
    join_deny = models.IntegerField(null=True)   # 가입 제한 (1:제한없음, 2:서민전용, 3:일부제한)
    join_member = models.TextField(null=True)    # 가입대상
    join_way = models.TextField(null=True)       # 가입 방법
    spcl_cnd = models.TextField(null=True)       # 우대조건


# 예금 상품 옵션
class DepositOptions(models.Model):
    product = models.ForeignKey(DepositProducts, on_delete=models.CASCADE, null=True) # 외래키 (DepositProducts 참조)
    fin_prdt_cd = models.TextField(null=True)                        # 금융 상품 코드
    intr_rate_type_nm = models.CharField(max_length=100, null=True)  # 저축금리 유형명
    intr_rate = models.FloatField(null=True)                         # 저축금리
    intr_rate2 = models.FloatField(null=True)                        # 최고우대금리
    save_trm = models.IntegerField(null=True)                        # 저축기간 (단위: 개월)


# # 적금 상품 목록
# class SavingProducts(models.Model):
#     dcls_month = models.TextField(null=True)       # 공시 제출월
#     fin_co_no = models.TextField(null=True)        # 금융회사 코드
#     kor_co_nm = models.TextField(null=True)        # 은행 이름          
#     fin_prdt_cd = models.TextField(unique=True)    # 금융상품 코드
#     fin_prdt_nm = models.TextField(null=True)      # 금융 상품명     
#     join_way = models.TextField(null=True)         # 가입 방법
#     mtrt_int = models.TextField(null=True)         # 만기 후 이자율
#     spcl_cnd = models.TextField(null=True)         # 우대 조건
#     join_deny = models.IntegerField(null=True)     # 가입 제한
#     join_member = models.TextField(null=True)      # 가입 대상
#     etc_note = models.TextField(null=True)         # 기타 유의 사항
#     max_limit = models.TextField(null=True)        # 최고한도
#     dcls_strt_day = models.TextField(null=True)    # 공시 시작일
#     fin_co_subm_day = models.TextField(null=True)  # 금융회사 제출일
        

# # 적금 상품 옵션
# class SavingOptions(models.Model):
#     product = models.ForeignKey(SavingProducts, on_delete = models.CASCADE)
#     fin_prdt_cd = models.TextField(null=True)                       # 상품 코드
#     intr_rate_type = models.TextField(null=True)                    # 저축 금리 유형
#     intr_rate_type_nm = models.CharField(max_length=100, null=True) # 저축 금리 유형명
#     rsrv_type = models.TextField(null=True)                         # 적립 유형
#     rsrv_type_nm = models.TextField(null=True)                      # 적립 유형명
#     save_trm = models.IntegerField(null=True)                       # 저축 기간
#     intr_rate = models.FloatField(null=True)                        # 저축 금리
#     intr_rate2 = models.FloatField(null=True)                       # 최대 우대 금리