<template>
  <div>
    <h1>메인페이지</h1>
  </div>
</template>

<script setup>

import { onMounted } from 'vue';
import { useDepositStore } from '@/stores/deposit';

const depositstore = useDepositStore();

if (depositstore.saveDeposit.length === 0) {
  onMounted(async () => {
    await depositstore.saveDeposit();
    await depositstore.saveSaving();
    await depositstore.getDeposits();
    await depositstore.getSavings();
    await depositstore.getAllProducts();
  });
}


</script>

<style scoped>

</style>