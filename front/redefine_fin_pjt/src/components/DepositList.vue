<template>
  <div>
    <DepositListItem 
      v-for="depositProduct in depositstore.depositProducts"
      :key="depositProduct.fin_prdt_cd"
      :depositProduct="depositProduct"/>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useDepositStore } from '@/stores/deposit';
import DepositListItem from './DepositListItem.vue';

const depositstore = useDepositStore()
// const depositProducts = ref(depositstore.depositProducts)


</script>

<style scoped>

</style>
