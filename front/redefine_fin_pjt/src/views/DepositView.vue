<template>
  <div>
    <h1>예적금 금리 비교</h1>
  </div>
</template>

<script setup>

import { ref, onMounted } from 'vue'
import { useDepositStore } from '@/stores/deposit';

const depositstore = useDepositStore()

onMounted(() => {
  depositstore.saveDeposit()
})

</script>

<style scoped>

</style>