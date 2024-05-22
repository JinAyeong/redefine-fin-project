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
      <button @click="addProduct(product.options.fin_prdt_cd, product.options.id)">관심 상품 등록 취소</button>
    </div>
    <canvas id="interestRateChart"></canvas>
    </div>
    <div v-else>
    <p>관심 상품이 없습니다.</p>
    <button @click="router.push({name: 'finance'})">상품 보러 가기 !</button>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, nextTick } from 'vue';
import axios from 'axios';
import { useProfileStore } from '@/stores/profile';
import { useDepositStore } from '@/stores/deposit';
import { useRouter } from 'vue-router';
import { Chart } from 'chart.js/auto';

const profilestore = useProfileStore();
const depositstore = useDepositStore()
const router = useRouter()
const products = ref([]);
let chartInstance = null;  // 기존 차트를 참조할 변수

const fetchProducts = () => {
  axios.get('http://127.0.0.1:8000/accounts/profile/get_added_product/', {
    headers: {
      Authorization: `Token ${profilestore.token}`
    }
  })
  .then(response => {
    products.value = response.data;
    nextTick(() => {
      if (products.value.length > 0) {
        renderChart();
      } else if (chartInstance) {
        chartInstance.destroy();
        chartInstance = null;
      }
    });
  })
  .catch(error => {
    console.error('관심 상품을 가져오는 중 에러 발생:', error);
  });
}

// 관심상품 등록 취소
const addProduct = function (product_cd, option_trm) {
  depositstore.addProduct(product_cd, option_trm)
  alert('구매가 취소되었습니다.');
  fetchProducts();
  router.go(0)
}

const renderChart = () => {
  const ctx = document.getElementById('interestRateChart').getContext('2d');
  const labels = products.value.map(product => product.product.fin_prdt_nm);
  const intrRates = products.value.map(product => product.options.intr_rate);
  const intrRates2 = products.value.map(product => product.options.intr_rate2);

  // 기존 차트가 존재하면 파괴
  if (chartInstance) {
    chartInstance.destroy();
  }

  // 새로운 차트 생성
  chartInstance = new Chart(ctx, {
    type: 'bar',
    data: {
      labels: labels,
      datasets: [
        {
          label: '저축 금리 (%)',
          data: intrRates,
          backgroundColor: 'rgba(75, 192, 192, 0.2)',
          borderColor: 'rgba(75, 192, 192, 1)',
          borderWidth: 1
        },
        {
          label: '최고 우대 금리 (%)',
          data: intrRates2,
          backgroundColor: 'rgba(255, 99, 132, 0.2)',
          borderColor: 'rgba(255, 99, 132, 1)',
          borderWidth: 1
        }
      ]
    },
    options: {
      scales: {
        y: {
          beginAtZero: true
        }
      }
    }
  });
};

onMounted(() => {
  fetchProducts();
});



</script>

<style scoped>
.product {
  margin-bottom: 1rem;
}
</style>
