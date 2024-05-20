<template>
  <div>
    <h1>정기 예금</h1>
    <DepositList />
  </div>
</template>

<script setup>

import { ref, onMounted } from 'vue'
import { RouterLink } from 'vue-router'
import { useDepositStore } from '@/stores/deposit';
import DepositList from '@/components/DepositList.vue';

const depositstore = useDepositStore()

onMounted(() => {
  depositstore.saveDeposit()
  depositstore.getDeposits()
})

</script>

<style scoped>

</style>