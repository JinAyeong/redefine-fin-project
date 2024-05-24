<template>
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
            <option value="농협은행주식회사">농협은행 주식회사</option>
            <option value="하나은행">하나은행</option>
            <option value="주식회사 케이뱅크">주식회사 케이뱅크</option>
            <option value="수협은행">수협은행</option>
            <option value="주식회사 카카오뱅크">주식회사 카카오뱅크</option>
            <option value="토스뱅크 주식회사">토스뱅크 주식회사</option>
          </select>
          <button @click="fetchDepositProducts" type="button" class="btn btn-outline-secondary">검색</button>
        </div>
      </nav>
  <h2 style="margin: 50px 0 30px 10px;">예금 상품 목록</h2>
  <hr>
  <div class="row">
    <DepositListItem 
      v-for="depositProduct in depositProducts"
      :key="depositProduct.fin_prdt_cd"
      :depositProduct="depositProduct"
    />
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue'
import { useDepositStore } from '@/stores/deposit';
import DepositListItem from './DepositListItem.vue';

const depositstore = useDepositStore()

const selectedBank = ref("");
const depositProducts = ref([]); // 로컬 상태로 관리

const fetchDepositProducts = async () => {
  try {
    const params = selectedBank.value ? { bank_name: selectedBank.value } : {};
    await depositstore.getDeposit(params); // 비동기 함수로 변경하여 완료 후 상태를 업데이트
    depositProducts.value = depositstore.depositProducts; // Pinia 상태를 로컬 상태에 반영
  } catch (error) {
    console.error('Error fetching deposit products:', error);
  }
};

onMounted(() => {
  fetchDepositProducts(); // 컴포넌트가 마운트될 때 데이터 가져오기
});

watch(() => depositstore.depositProducts, (newProducts) => {
  depositProducts.value = newProducts; // Pinia 상태 변경을 감지하여 로컬 상태 업데이트
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

.nav-link h5 span.active {
  color: var(--bs-primary); /* 활성화된 예금 항목의 텍스트 색상을 primary로 설정 */
}
</style>

