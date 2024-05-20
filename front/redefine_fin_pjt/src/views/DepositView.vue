<template>
  <div>
    <h1>예적금 금리 비교</h1>
    <DepositList />
  </div>
</template>

<script setup>

import { ref, onMounted } from 'vue'
import { useDepositStore } from '@/stores/deposit';
import DepositList from '@/components/DepositList.vue';

const depositstore = useDepositStore()

onMounted(() => {
  depositstore.saveDeposit()
})

</script>

<style scoped>

</style>