<template>
  <div>
    <h3>관심상품</h3>
    <div v-if="products.length">
    <div v-for="product in products" :key="product.product.fin_prdt_cd" class="product">
      <h4>{{ product.product.fin_prdt_nm }}</h4>
      <p>금융 회사명: {{ product.product.kor_co_nm }}</p>
      <p>금리 유형: {{ product.options.intr_rate_type_nm }}</p>
      <p>저축 금리: {{ product.options.intr_rate }}%</p>
      <p>최고 우대 금리: {{ product.options.intr_rate2 }}%</p>
      <p>저축 기간: {{ product.options.save_trm }}개월</p>
      <button @click="addProduct(product.options.fin_prdt_cd, product.options.save_trm)">관심 상품 등록 취소</button>
    </div>
    </div>
    <div v-else>
    <p>관심 상품이 없습니다.</p>
    <button @click="router.push({name: 'finance'})">상품 보러 가기 !</button>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import { useProfileStore } from '@/stores/profile';
import { useDepositStore } from '@/stores/deposit';
import { useRouter } from 'vue-router';

const profilestore = useProfileStore();
const depositstore = useDepositStore()
const router = useRouter()
const products = ref([]);

const fetchProducts = () => {
  axios.get('http://127.0.0.1:8000/accounts/profile/get_added_product/', {
    headers: {
      Authorization: `Token ${profilestore.token}`
    }
  })
  .then(response => {
    products.value = response.data;
  })
  .catch(error => {
    console.error('관심 상품을 가져오는 중 에러 발생:', error);
  });
}

// 관심상품 등록 취소
const addProduct = function (product_cd, option_trm) {
  depositstore.addProduct(product_cd, option_trm)
}


onMounted(() => {
  fetchProducts();
});
</script>

<style scoped>
.product {
  margin-bottom: 1rem;
}
</style>
