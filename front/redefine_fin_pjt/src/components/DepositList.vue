<template>
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
</style>

