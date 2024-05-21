<template>
  <div>
    <h5>정기예금 상품 옵션 정보</h5>
    <span>저축 금리 유형 : {{ depositOption.intr_rate_type_nm }}</span>
    <span>저축 금리 : {{ depositOption.intr_rate }}</span>
    <span>최고 우대 금리 : {{ depositOption.intr_rate2 }}</span>
    <span>저축 기간 (단위: 개월) : {{ depositOption.save_trm }}</span>
    <span v-if="productStatus !== null && productStatus">
      <button @click="addProduct(depositOption.fin_prdt_cd, depositOption.save_trm)">관심 상품 삭제</button>
    </span>
    <span v-else>
      <button @click="addProduct(depositOption.fin_prdt_cd, depositOption.save_trm)">관심 상품 등록</button>
    </span>
    <hr>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useDepositStore } from '@/stores/deposit';
import { useProfileStore } from '@/stores/profile';
import axios from 'axios';

const depositOption = defineProps({
  depositOption: {
    type: Object,
    required: true
  }
});

const depositstore = useDepositStore();
const profilestore = useProfileStore();
const productStatus = ref(null);

// 관심상품 등록
const addProduct = async function (product_cd, option_trm) {
  try {
    await depositstore.addProduct(product_cd, option_trm);
    await checkProductStatus(product_cd, option_trm);
  } catch (error) {
    console.error(error);
  }
};

// 관심상품 등록 상태 확인
const checkProductStatus = async function (product_cd, option_trm) {
  try {
    const response = await axios({
      method: 'get',
      url: `${depositstore.API_URL}/accounts/profile/check_product/${product_cd}/${option_trm}`,
      headers: {
        Authorization: `Token ${profilestore.token}`
      },
    });
    productStatus.value = response.data;
    console.log(response.data);
  } catch (error) {
    console.error(error);
  }
};

// 컴포넌트가 마운트되면 관심상품 상태 확인
onMounted(() => {
  checkProductStatus(depositOption.fin_prdt_cd, depositOption.save_trm);
});
</script>

<style scoped>
</style>
