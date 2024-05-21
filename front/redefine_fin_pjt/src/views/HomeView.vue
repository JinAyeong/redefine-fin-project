<template>
  <div>
    <h1>메인페이지</h1>
    <button @click="findProduct">상품 추천받기!</button>
  </div>
</template>

<script setup>

import { onMounted } from 'vue';
import { useDepositStore } from '@/stores/deposit';
import { useRouter } from 'vue-router';

const depositstore = useDepositStore();
const router = useRouter()

if (depositstore.saveDeposit.length === 0) {
  onMounted(async () => {
    await depositstore.saveDeposit();
    await depositstore.saveSaving();
    await depositstore.getDeposits();
    await depositstore.getSavings();
    await depositstore.getAllProducts();
  });
}

const findProduct = function () {
  router.push({name: 'recommend'})
}

</script>

<style scoped>

</style>