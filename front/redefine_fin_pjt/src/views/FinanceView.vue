<template>
  <section class="py-5">
    <div class="container px-5">
      <nav class="navbar navbar-expand-lg bg-body-tertiary">
        <div class="container-fluid">
          <div class="collapse navbar-collapse" id="navbarNavDropdown">
            <RouterLink
              class="navbar-brand"
              style="margin-left: 10px; display: flex; align-items: center; height: 100%;"
              :to="{ path: '/finance/' }"
            >
              <span :class="{ active: $route.path === '/finance/' }">상품 조회</span>
            </RouterLink>
            <h5 style="margin: 0; display: flex; align-items: center; height: 100%;">|</h5>
            <div style="margin-left: 20px;">
              <ul class="navbar-nav" style="display: flex; align-items: center; height: 100%;">
                <li class="nav-item">
                  <RouterLink
                    class="nav-link"
                    :to="{ path: '/finance/deposit' }"
                  >
                    <h5 style="margin: 0; display: flex; align-items: center; height: 100%;">
                      <span :class="{ active: $route.path === '/finance/deposit' }">예금</span>
                    </h5>
                  </RouterLink>
                </li>
                <li class="nav-item">
                  <RouterLink
                    class="nav-link"
                    :to="{ path: '/finance/saving' }"
                  >
                    <h5 style="margin: 0; display: flex; align-items: center; height: 100%;">
                      <span :class="{ active: $route.path === '/finance/saving' }">적금</span>
                    </h5>
                  </RouterLink>
                </li>
              </ul>
            </div>
          </div>
        </div>
        <div class="d-flex" style="margin-right: 20px;">
          <select v-model="selectedBank" class="form-select me-2 custom-select-width" aria-label="은행을 선택해주세요">
            <option value="우리은행">우리은행</option>
            <option value="한국스탠다드차타드은행">한국스탠다드차타드은행</option>
            <option value="대구은행">대구은행</option>
            <option value="부산은행">부산은행</option>
            <option value="광주은행">광주은행</option>
            <option value="제주은행">제주은행</option>
            <option value="전북은행">전북은행</option>
            <option value="경남은행">경남은행</option>
            <option value="중소기업은행">중소기업은행</option>
            <option value="한국산업은행">한국산업은행</option>
            <option value="국민은행">국민은행</option>
            <option value="신한은행">신한은행</option>
            <option value="농협은행 주식회사">농협은행 주식회사</option>
            <option value="하나은행">하나은행</option>
            <option value="주식회사 케이뱅크">주식회사 케이뱅크</option>
            <option value="수협은행">수협은행</option>
            <option value="주식회사 카카오뱅크">주식회사 카카오뱅크</option>
            <option value="코스뱅크 주식회사">코스뱅크 주식회사</option>
          </select>
          <button @click="fetchDepositProducts" type="button" class="btn btn-outline-secondary">검색</button>
        </div>
      </nav>
      <RouterView />
    </div>
  </section>
</template>

<script setup>
import { RouterLink, RouterView, useRoute } from 'vue-router';
import { ref, onMounted } from 'vue';
import { useDepositStore } from '@/stores/deposit';

const depositstore = useDepositStore();
const selectedBank = ref(null);

// onMounted(async () => {
//   await depositstore.getDeposits();
//   await depositstore.getSavings();
// });
</script>

<style scoped>
.navbar-nav .nav-link span {
  color: black;
}

.navbar-nav .nav-link span.active {
  color: cornflowerblue;
}

.navbar-brand span {
  color: black;
}

.navbar-brand span.active {
  color: cornflowerblue;
}
</style>
