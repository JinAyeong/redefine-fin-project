<template>
  <div>
    <p>금융 회사명 : {{ savingProduct.kor_co_nm }}</p>
    <p>상품명 : <span>{{ savingProduct.fin_prdt_nm }}</span></p>
    <div>
      <p v-for="savingOption in savingOptions" :key="savingOption.id">
        이율 종류: {{ savingOption.intr_rate_type_nm }} / 기본 이율: {{ savingOption.intr_rate }} / 우대 이율: {{ savingOption.intr_rate2 }} / 기간: {{ savingOption.save_trm }}
      </p>
    </div>
    <RouterLink :to="{ 
      name: 'savingdetail', 
      params: { fin_prdt_cd: savingProduct.fin_prdt_cd }}">
      <button>자세히보기</button>
    </RouterLink>
    <hr>
  </div>
</template>

<script setup>
import { useDepositStore } from '@/stores/deposit';
import { RouterLink } from 'vue-router';

defineProps({
  savingProduct: Object,
});

</script>

<style scoped>
/* 스타일 정의 */
</style>