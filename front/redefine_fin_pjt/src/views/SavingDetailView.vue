<template>
  <div>
    <h1>적금 정보</h1>
    <div>
      <p>회사명: {{ product.kor_co_nm }}</p>
      <p>상품명: {{ product.fin_prdt_nm }}</p>
      <p>상품 설명: {{ product.etc_note }}</p>
      <p v-if="product.join_deny === 1">가입 제한: 제한없음</p>
      <p v-if="product.join_deny === 2">가입 제한: 서민전용</p>
      <p v-if="product.join_deny === 3">가입 제한: 일부제한</p>
      <p>가입 대상: {{ product.join_member }}</p>
      <p>가입 방법: {{ product.join_way }}</p>
      <p>우대 조건: {{ product.spcl_cnd }}</p>
    </div>
    <div>
      <hr>
      <h3>상품 옵션</h3>
      <SavingOptionItem 
        v-for="savingOption in savingOptions"
        :key="savingOption.id"
        :savingOption="savingOption"/>
    </div>
  </div>
</template>

<script setup>

import axios from 'axios';
import { ref, computed, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router';
import { useDepositStore } from '@/stores/deposit';
import SavingOptionItem from '@/components/SavingOptionItem.vue'

const route = useRoute()
const router = useRouter()
const depositstore = useDepositStore()
const savingOptions = ref(null)

// 상품 가져오기
const productCd = route.params.fin_prdt_cd;
const product = computed(() => {
  return depositstore.savingProducts?.filter(
    (product) => product.fin_prdt_cd === productCd
  )[0];
});

// 해당 상품의 옵션 가져오기
axios({
  method: 'get',
  url: `${depositstore.API_URL}/finances/saving-products-options/${productCd}`,
})
  .then((response) => {
    savingOptions.value = response.data
    console.log(response.data)
  })
  .catch((error) => {
    console.log(error)
  })

</script>

<style scoped>

</style>