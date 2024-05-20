<template>
  <div>
    <h1>상품 리스트</h1>
    <DepositListItem 
      v-for="product in products"
      :key="product.id"
      :product="product"/>
  </div>
</template>

<script setup>

import DepositListItem from './DepositListItem.vue';
import { useDepositStore } from '@/stores/deposit'

const depositstore = useDepositStore()

const products = depositstore.saving_products

</script>

<style scoped>

</style>