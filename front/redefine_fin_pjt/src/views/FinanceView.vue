<template>
  <section class="py-5">
  <div class="container px-5">

    <RouterView />
  </div>
  </section>

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
