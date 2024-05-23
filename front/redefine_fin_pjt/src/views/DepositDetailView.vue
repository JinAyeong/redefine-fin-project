<template>
  <section class="py-5">
    <div class="container px-5">
      <div v-if="product">
        <h2 class="fw-bolder mb-4" style="margin-left: 20px;">상품 상세 정보</h2>
        <article class="card shadow-sm p-4 mb-4 text-center">
          <!-- Post title and category-->
          <header class="mb-4">
            <h1 class="fw-bolder mb-3">{{ product.fin_prdt_nm }}</h1>
            <a class="badge bg-primary text-decoration-none link-light" href="#!">{{ product.kor_co_nm }}</a>
          </header>
        </article>
        <div class="row">
          <div class="col-lg-12">
            <!-- Post content-->
            <article class="card shadow-sm p-4 mb-4">
              <!-- Post content-->
              <section class="mb-5">
                <div class="card shadow-sm p-4 mb-4">
                  <p class="fs-5 mb-4"><strong>상품 설명</strong><br><span class="content-detail">{{ product.etc_note }}</span></p>
                  <p class="fs-5 mb-4" v-if="product.join_deny === 1"><strong>가입 제한:</strong> <span class="content-detail">제한없음</span></p>
                  <p class="fs-5 mb-4" v-if="product.join_deny === 2"><strong>가입 제한:</strong> <span class="content-detail">서민전용</span></p>
                  <p class="fs-5 mb-4" v-if="product.join_deny === 3"><strong>가입 제한:</strong> <span class="content-detail">일부제한</span></p>
                  <div class="fs-5 mb-4">
                    <strong>가입 대상:</strong> <span class="content-detail">{{ product.join_member }}</span>
                  </div>
                  <div class="fs-5 mb-4">
                    <strong>가입 방법:</strong> <span class="content-detail">{{ product.join_way }}</span>
                  </div>
                  <div class="fs-5 mb-4">
                    <strong>우대 조건:</strong><br> <span class="content-detail">{{ product.spcl_cnd }}</span>
                  </div>
                </div>
              </section>
            </article>

            <h2 class="fw-bolder mb-3" style="margin: 50px 20px;">상품 옵션</h2>
            <div class="card shadow-sm p-4 mb-4" style="height: 800px; overflow-y: auto;">
              <hr>
              <div class="row">
                <div class="col-12 mb-4" v-for="depositOption in depositOptions" :key="depositOption.id">
                  <div class="card shadow-sm p-3 h-100">
                    <DepositOptionItem :depositOption="depositOption" />
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import axios from 'axios';
import { ref, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { useDepositStore } from '@/stores/deposit';
import { useProfileStore } from '@/stores/profile';
import DepositOptionItem from '@/components/DepositOptionItem.vue';

const route = useRoute();
const depositstore = useDepositStore();
const profilestore = useProfileStore();
const depositOptions = ref(null);
const product = ref(null);

// 상품 가져오기
const productCd = route.params.fin_prdt_cd;

onMounted(async () => {
  // 정기예금 상품 목록 가져오기
  await depositstore.getDeposits();
  product.value = depositstore.depositProducts.find(
    (product) => product.fin_prdt_cd === productCd
  );
  console.log(product.value);
  if (product.value) {
    // 해당 상품의 옵션 가져오기
    try {
      const response = await axios.get(`${depositstore.API_URL}/finances/deposit-products-options/${productCd}`);
      depositOptions.value = response.data;
      // console.log(response.data);
    } catch (error) {
      console.log(error);
    }
  }
});
</script>

<style scoped>
.card {
  border-radius: 0.75rem;
  background-color: #ffffff;
  padding: 1.5rem;
  box-shadow: 0 0.125rem 0.25rem rgba(0, 0, 0, 0.075);
}

.card header {
  background-color: #f8f9fa;
  padding: 1.5rem;
  border-bottom: 1px solid #e9ecef;
  border-top-left-radius: 0.75rem;
  border-top-right-radius: 0.75rem;
}

.card h1 {
  font-size: 2rem;
  margin-bottom: 0.5rem;
}

.card p {
  line-height: 1.5;
}

.card .badge {
  margin-top: 0.5rem;
}

.fs-5 {
  font-size: 1.25rem;
}

.mb-4 {
  margin-bottom: 1.5rem;
}

strong {
  font-weight: bold;
  color: #2c3e50;
  font-size: 1.15rem;
  display: inline-block;
  margin-bottom: 0.5rem;
}

.content-detail {
  display: block;
  margin-left: 10px;
  font-size: 1rem;
  color: #5a5a5a;
  line-height: 1.5;
}
</style>
