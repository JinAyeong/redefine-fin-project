<template>
    <section class="py-5">
      <div class="container px-5">
        <h2 style="margin: 50px 0 30px 10px;">나에게 꼭 맞는 추천상품</h2>
        <hr>
        <div class="row">
          <div
            class="col-lg-4 col-md-6 mb-4"
            v-for="product in recommendstore.recommendedProducts"
            :key="product"
          >
            <div class="card h-100 shadow border-30">
              <div class="card-body p-4">
                <div class="badge bg-primary bg-gradient rounded-pill mb-2">
                  {{ product.kor_co_nm }}
                </div>
                <a class="text-decoration-none link-dark stretched-link" href="#!">
                  <div class="h5 card-title mb-3">
                    {{ product.fin_prdt_nm }}
                  </div>
                <hr>
                <p>{{ product.etc_note }}</p>
                </a>
              </div>
            </div>
          </div>
          <button @click="router.push({name: 'deposit'})" class="btn btn-outline-secondary">더 많은 상품 보러 가기</button>
          </div>
        </div>
    </section>
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
const depositstore = useDepositStore()
const route = useRoute();
const router = useRouter()

onMounted(() => {
  recommendstore.recommendAuto(profilestore.token)
})

const productCd = route.params.id;

const product = computed(() => {
  return depositstore.deposit_products?.filter(
    (product) => product.fin_prdt_cd === productCd
  )[0];
});


</script>

<style scoped>

button {
  white-space: nowrap;
}

/* select와 button의 높이를 동일하게 맞추기 위한 추가 스타일 */
.form-select,
.btn {
  height: calc(2.25rem + 2px); /* Bootstrap 기본 높이와 동일 */
  padding: 0.375rem 0.75rem;   /* Bootstrap 기본 패딩 */
  font-size: 1rem;            /* Bootstrap 기본 폰트 크기 */
}

.custom-select-width {
  width: 300px; /* 원하는 가로 길이로 설정 */
}

.option-item {
  margin-bottom: 1rem;
  position: relative;
}

.card-title {
  font-weight: bold;
  margin-bottom: 1rem;
}

.card-text {
  margin-bottom: 0.5rem;
}

.btn-outline-navy {
  color: #001f3f;
  border-color: #001f3f;
  background-color: transparent;
}

.btn-outline-navy:hover {
  color: white;
  background-color: #001f3f;
  border-color: #001f3f;
}

.fixed-button {
  position: absolute;
  bottom: 2rem;
  right: 2rem;
}

</style>