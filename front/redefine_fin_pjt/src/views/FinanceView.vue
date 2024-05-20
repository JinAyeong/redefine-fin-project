<template>
  <div>
    <h1>금리 비교</h1>
    <RouterLink :to="{name: 'deposit'}">예금</RouterLink>
    <RouterLink :to="{name: 'saving'}">적금</RouterLink>
    
    <RouterView />
  </div>
</template>

<script setup>
import { onMounted } from 'vue';
import { RouterLink } from 'vue-router';
import { useDepositStore } from '@/stores/deposit';

const depositstore = useDepositStore();

onMounted(async () => {
  await depositstore.saveDeposit();
  await depositstore.saveSaving();
  await depositstore.getDeposits();
  await depositstore.getSavings();
});
</script>

<style scoped>
</style>
