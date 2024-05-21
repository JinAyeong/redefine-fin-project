<template>
  <div>
    <div>
      <label for="filter">필터: </label>
      <select v-model="selectedBank" id="filter">
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
      <button type="submit" @click="fetchDepositProducts">검색</button>
    </div>

    <DepositListItem 
      v-for="depositProduct in depositProducts"
      :key="depositProduct.fin_prdt_cd"
      :depositProduct="depositProduct"/>
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue'
import { useDepositStore } from '@/stores/deposit';
import DepositListItem from './DepositListItem.vue';
import { useProfileStore } from '@/stores/profile';
import { useRouter } from 'vue-router'

const router = useRouter()
const profilestore = useProfileStore()
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
</style>
