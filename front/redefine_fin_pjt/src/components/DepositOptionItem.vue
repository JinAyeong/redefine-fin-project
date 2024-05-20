<template>
  <div>
    <h5>정기예금 상품 옵션 정보</h5>
    <span>저축 금리 유형 : {{ depositOption.intr_rate_type_nm }}</span>
    <span>저축 금리 : {{ depositOption.intr_rate }}</span>
    <span>최고 우대 금리 : {{ depositOption.intr_rate2 }}</span>
    <span>저축 기간 (단위: 개월) : {{ depositOption.save_trm }}</span>
    <button>관심 상품 등록</button>
    <hr>
  </div>
</template>

<script setup>

defineProps({
  depositOption: Object
})

</script>

<style scoped>

</style>