<template>
  <div>
    <h5>적금 상품 옵션 정보</h5>
    <span>저축 금리 유형 : {{ savingOption.intr_rate_type_nm }}</span>
    <span>저축 금리 : {{ savingOption.intr_rate }}</span>
    <span>최고 우대 금리 : {{ savingOption.intr_rate2 }}</span>
    <span>저축 기간 (단위: 개월) : {{ savingOption.save_trm }}</span>
    <hr>
  </div>
</template>

<script setup>

defineProps({
  savingOption: Object
})


</script>

<style scoped>

</style>