<template>
  <div>
    <h1>금리 비교</h1>
    <RouterLink :to="{name: 'deposit'}">예금</RouterLink>
    <RouterLink :to="{name: 'saving'}">적금</RouterLink>
    <RouterView />
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router';
import { onMounted } from 'vue';
import { useDepositStore } from '@/stores/deposit';

const depositstore = useDepositStore();

// onMounted(async () => {
//   await depositstore.getDeposits();
//   await depositstore.getSavings();
// });
</script>

<style scoped>
</style>
