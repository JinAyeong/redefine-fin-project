<template>
  <div v-if="product">
    <h1>정기 예금 정보</h1>
    <div>
      <p>회사명: {{ product.kor_co_nm }}</p>
      <p>상품명: {{ product.fin_prdt_nm }}</p>
      <p>상품 설명: {{ product.etc_note }}</p>
      <p v-if="product.join_deny === 1">가입 제한: 제한없음</p>
      <p v-if="product.join_deny === 2">가입 제한: 서민전용</p>
      <p v-if="product.join_deny === 3">가입 제한: 일부제한</p>
      <p>가입 대상: {{ product.join_member }}</p>
      <p>가입 방법: {{ product.join_way }}</p>
      <p>우대 조건: {{ product.spcl_cnd }}</p>
    </div>
    <div>
      <hr>
      <h3>상품 옵션</h3>
      <DepositOptionItem 
        v-for="depositOption in depositOptions"
        :key="depositOption.id"
        :depositOption="depositOption"/>
    </div>
  </div>
  <div v-else>
    <p>정기예금상품 정보 가져오는중...</p>
  </div>
</template>

<script setup>
import axios from 'axios';
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router';
import { useDepositStore } from '@/stores/deposit';
import DepositOptionItem from '@/components/DepositOptionItem.vue'

const route = useRoute()
const depositstore = useDepositStore()
const depositOptions = ref(null)
const product = ref(null)

// 상품 가져오기
const productCd = route.params.fin_prdt_cd;

onMounted(async () => {
   // 정기예금 상품 목록 가져오기
  await depositstore.getDeposits();
  product.value = depositstore.depositProducts.find(
    (product) => product.fin_prdt_cd === productCd
  );
  if (product.value) {
    // 해당 상품의 옵션 가져오기
    try {
      const response = await axios.get(`${depositstore.API_URL}/finances/deposit-products-options/${productCd}`);
      depositOptions.value = response.data;
      console.log(response.data);
    } catch (error) {
      console.log(error);
    }
  }
});
</script>

<style scoped>
</style>
