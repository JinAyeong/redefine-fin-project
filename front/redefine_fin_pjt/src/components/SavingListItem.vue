<template>
  <div>
    <p>금융 회사명 : {{ savingProduct.kor_co_nm }}</p>
    <p>상품명 : <span>{{ savingProduct.fin_prdt_nm }}</span></p>
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
</style>