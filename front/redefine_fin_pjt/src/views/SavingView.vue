<template>
  <div>
    <h2>적금 상품</h2>
    <SavingList />
  </div>
</template>

<script setup>

import { ref, onMounted } from 'vue'
import { useDepositStore } from '@/stores/deposit';
import SavingList from '@/components/SavingList.vue';

const depositstore = useDepositStore()

onMounted(() => {
  depositstore.saveSaving()
  depositstore.getSavings()
})

</script>

<style scoped>

</style>