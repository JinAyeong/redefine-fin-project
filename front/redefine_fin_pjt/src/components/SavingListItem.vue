<template>
  <div>
    <p>금융 회사명 : {{ savingProduct.kor_co_nm }}</p>
    <p>상품명 : <span>{{ savingProduct.fin_prdt_nm }}</span></p>
    <div>
      <p v-for="savingOption in savingOptions" :key="savingOption.id">
        이율 종류: {{ savingOption.intr_rate_type_nm }} / 기본 이율: {{ savingOption.intr_rate }} / 우대 이율: {{ savingOption.intr_rate2 }} / 기간: {{ savingOption.save_trm }}
      </p>
    </div>
    <RouterLink :to="{ name: 'savingdetail', params: { fin_prdt_cd: savingProduct.fin_prdt_cd } }">
      <button>자세히보기</button>
    </RouterLink>
    <hr>
  </div>
</template>

<script setup>
import axios from 'axios';
import { ref, onMounted, watch } from 'vue';
import { useDepositStore } from '@/stores/deposit';
import { RouterLink } from 'vue-router';

const depositstore = useDepositStore();
const savingOptions = ref([]);

defineProps({
  savingProduct: Object,
});

onMounted(
  () => savingProduct,
  (newProduct) => {
    if (newProduct && newProduct.fin_prdt_nm) {
      fetchSavingOptions(newProduct.fin_prdt_nm);
    }
  },
  { immediate: true } // immediate를 true로 설정하여 초기 로드시에도 호출되도록 함
);

const fetchSavingOptions = (finPrdtNm) => {
  axios({
    method: 'get',
    url: `${depositstore.API_URL}/finances/saving-products-options/${finPrdtNm}`,
  })
    .then((response) => {
      savingOptions.value = response.data;
      console.log(response.data);
    })
    .catch((error) => {
      console.log(error);
    });
};
</script>

<style scoped>
/* 스타일 정의 */
</style>
