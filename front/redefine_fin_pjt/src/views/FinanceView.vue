<template>
  <section class="py-5">
    <div class="container px-5">
      <RouterView />
    </div>
  </section>
</template>

<script setup>
import { RouterLink, RouterView, useRoute } from 'vue-router';
import { ref, onMounted } from 'vue';
import { useDepositStore } from '@/stores/deposit';

const depositstore = useDepositStore();
const selectedBank = ref(null);

// onMounted(async () => {
//   await depositstore.getDeposits();
//   await depositstore.getSavings();
// });
</script>

<style scoped>

</style>
