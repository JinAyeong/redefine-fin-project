<template>
  <body class="d-flex flex-column">
    <main class="flex-shrink-0">
      <!-- Pricing section-->
      <section class="bg-light py-5">
        <div class="container px-5 my-5">
          <div class="text-center mb-5">
            <h1 class="fw-bolder">나의 관심 상품</h1>
            <p class="lead fw-normal text-muted mb-0">
              <i class="bi bi-check text-primary"></i>나의 관심상품을 비교해보세요!
            </p>
          </div>
          <div class="row gx-5 justify-content-center">
            <!-- Pricing card enterprise-->
            <div v-if="products.length" class="row gx-5">
              <div class="col-lg-4 col-md-6 mb-4" v-for="product in products" :key="product.product.fin_prdt_cd">
                <div class="card h-100">
                  <div class="card-body p-4">
                    <div class="h5 card-title mb-3">
                      {{ product.product.fin_prdt_nm }}
                    </div>
                    <hr>
                    <div class="mb-3 d-flex justify-content-between">
                      <strong>저축 금리</strong>
                      <div>
                        <span class="text-muted">{{ product.options.intr_rate }} / </span>
                        <span class="display-4 fw-bold">{{ product.options.intr_rate2 }} %</span>
                      </div>
                    </div>
                    <ul class="list-unstyled mb-4">
                      <li class="mb-2 d-flex justify-content-between">
                        <strong>금리 유형</strong>
                        <span>{{ product.options.intr_rate_type_nm }}</span>
                      </li>
                      <li class="mb-2 d-flex justify-content-between">
                        <strong>저축 금리</strong>
                        <span>{{ product.options.intr_rate }} %</span>
                      </li>
                      <li class="mb-2 d-flex justify-content-between">
                        <strong>최고 우대 금리</strong>
                        <span>{{ product.options.intr_rate2 }} %</span>
                      </li>
                      <li class="mb-2 d-flex justify-content-between">
                        <strong>금리 유형</strong>
                        <span>{{ product.options.intr_rate_type_nm }}</span>
                      </li>
                      <li class="mb-2 d-flex justify-content-between">
                        <strong>저축 기간</strong>
                        <span>{{ product.options.save_trm }} 개월</span>
                      </li>
                    </ul>
                    <div @click="addProduct(product.options.fin_prdt_cd, product.options.id)" class="d-grid">
                      <a class="btn btn-light" href="#!">관심 상품 등록 취소</a>
                    </div>
                  </div>
                </div>
              </div>
              <hr style="margin-top: 50px;">
              <div class="col-12" style="margin-top: 70px;">
                <h3 class="fw-bolder">나의 관심 상품 비교</h3>
                <canvas id="interestRateChart"></canvas>
              </div>
            </div>
            <div v-else class="row gx-5">
              <p>관심 상품이 없습니다.</p>
              <button @click="router.push({name: 'deposit'})" class="btn btn-outline-secondary">상품 보러 가기 !</button>
            </div>
          </div>
        </div>
      </section>
    </main>
  </body>
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
  alert('관심상품 등록이 취소되었습니다.');
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
          backgroundColor: 'rgba(75, 192, 192, 0.7)', // 그래프 색상 변경
          borderColor: 'rgba(75, 192, 192, 1)',
          borderWidth: 1
        },
        {
          label: '최고 우대 금리 (%)',
          data: intrRates2,
          backgroundColor: 'rgba(255, 99, 132, 0.7)', // 그래프 색상 변경
          borderColor: 'rgba(255, 99, 132, 1)',
          borderWidth: 1
        }
      ]
    },
    options: {
      scales: {
        y: {
          beginAtZero: true,
          // y축 레이블 스타일 변경
          ticks: {
            font: {
              size: 14, // 폰트 크기 변경
              color: 'black' // 폰트 색상 변경
            }
          }
        },
        x: {
          // x축 레이블 스타일 변경
          ticks: {
            font: {
              size: 14, // 폰트 크기 변경
              color: 'black' // 폰트 색상 변경
            }
          }
        }
      },
      // 그래프 배경색 변경
      plugins: {
        legend: {
          labels: {
            font: {
              size: 14 // 범례 폰트 크기 변경
            }
          }
        },
        tooltip: {
          bodyFont: {
            size: 14 // 툴팁 폰트 크기 변경
          }
        },
        layout: {
          padding: {
            left: 20, // 그래프 좌측 여백 추가
            right: 20, // 그래프 우측 여백 추가
            top: 20, // 그래프 상단 여백 추가
            bottom: 20 // 그래프 하단 여백 추가
          }
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
  margin-bottom: 2rem; /* 카드 사이 간격을 조정 */
}

.card {
  width: 100%; /* 카드 너비를 100%로 설정하여 그리드 시스템에 맞게 조정 */
}
</style>
