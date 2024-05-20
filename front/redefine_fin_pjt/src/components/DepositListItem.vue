<template>
  <div>
    <p>금융 회사명 : {{ depositProduct.kor_co_nm }}</p>
    <p>상풍명 : <span>{{ depositProduct.fin_prdt_nm }}</span></p>
    <RouterLink :to="{
      name: 'depositdetail',
      params: {fin_prdt_cd: depositProduct.fin_prdt_cd}}">
      <button>자세히보기</button>
    </RouterLink>
    <hr>
  </div>
</template>

<script setup>

import { RouterLink } from 'vue-router';
import { useRouter } from 'vue-router';

defineProps({
  depositProduct: Object
})

const router = useRouter()


</script>

<style scoped>

</style>