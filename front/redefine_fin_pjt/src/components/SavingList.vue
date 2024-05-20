<template>
  <div>
    <SavingListItem 
      v-for="savingProduct in depositstore.savingProducts"
      :key="savingProduct.fin_prdt_cd"
      :savingProduct="savingProduct"/>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useDepositStore } from '@/stores/deposit';
import SavingListItem from './SavingListItem.vue';

const depositstore = useDepositStore()
// const depositProducts = ref(depositstore.depositProducts)


</script>

<style scoped>

</style>
