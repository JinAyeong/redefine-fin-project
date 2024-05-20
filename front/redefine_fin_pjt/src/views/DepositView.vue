<template>
  <div>
    <h2>정기 예금 상품</h2>
    <DepositList />
  </div>
</template>

<script setup>

import { ref, onMounted } from 'vue'
import { useDepositStore } from '@/stores/deposit';
import DepositList from '@/components/DepositList.vue';

const depositstore = useDepositStore()


</script>

<style scoped>

</style>