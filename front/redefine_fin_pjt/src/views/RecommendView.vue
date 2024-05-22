<template>
  <div>
    <h1>상품 추천받기!</h1>
    <h3>나와 비슷한 사람들이 많이 가입한 상품</h3>

    <ul v-if="recommendstore.recommendedProducts.length">
      <li v-for="product in recommendstore.recommendedProducts" :key="product">
        <!-- {{ product }} -->
        <p>은행명:{{ product.kor_co_nm }}</p>
        <p>금융코드:{{ product.fin_prdt_cd }}</p>
        <p>금융 상품명:{{ product.fin_prdt_nm }}</p>
        <p>금융 상품 설명:{{ product.spcl_cnd }}</p>
        <a href="http://localhost:5173/deposit/detail/{{ product.fin_prdt_cd }}">가입</a>
      </li>
    </ul>
    <!-- {{ recommendstore.productAuto }} -->
  </div>
</template>

<script setup>

import { ref, onMounted, computed } from 'vue'
import axios from 'axios';
import { useRecommendStore } from '@/stores/recommend'
import { useProfileStore } from '@/stores/profile';
import { useDepositStore } from '@/stores/deposit';
import { useRouter, useRoute } from "vue-router";

const recommendstore = useRecommendStore()
const profilestore = useProfileStore()
const route = useRoute();

onMounted(() => {
  recommendstore.recommendAuto(profilestore.token)
})

const productCd = route.params.id;
const product = computed(() => {
  return profilestore.deposit_products?.filter(
    (product) => product.fin_prdt_cd === productCd
  )[0];
});

</script>

<style scoped>

</style>