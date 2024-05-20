<template>
  <div>
    <p>금융 회사명 : {{ product.kor_co_nm }}</p>
    <p>상풍명 : {{ product.fin_prdt_nm }}</p>
    <hr>
  </div>
</template>

<script setup>

defineProps({
  product: Object
})

</script>

<style scoped>

</style>