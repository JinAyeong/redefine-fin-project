<template>
  <div class="option-item">
    <h5>적금 상품 옵션 정보</h5>
    <p>유형: {{ savingOption.intr_rate_type_nm }}</p>
    <p>저축 단위: {{ savingOption.save_trm }} 개월</p>
    <p>저축금리: {{ savingOption.intr_rate }} %</p>
    <p>최고 우대 금리: {{ savingOption.intr_rate2 }} %</p>
    <button @click="addOrCancelProduct(savingOption.fin_prdt_cd, savingOption.id)">
      {{ isProductAdded(savingOption.fin_prdt_cd, savingOption.id) ? '가입 취소 하기' : '상품 가입하기' }}
    </button>   
    <hr>
  </div>
</template>

<script setup>
import { ref, watch } from 'vue';
import axios from 'axios';
import { useDepositStore } from '@/stores/deposit'
import { useProfileStore } from '@/stores/profile';
import { useRouter } from 'vue-router';

const depositstore = useDepositStore()
const profilestore = useProfileStore()
const router = useRouter()

const props = defineProps({
  savingOption: {
    type: Object,
    required: true
  }
});


const isProductAdded = (product_cd, option_trm) => {
  const products = profilestore.userProfile?.financial_products || [];
  const elem = `${product_cd}/${option_trm}`;
  return products.includes(elem);
};

const addOrCancelProduct = (product_cd, option_trm) => {
  const elem = `${product_cd}/${option_trm}`;
  if (isProductAdded(product_cd, option_trm)) {
    cancelProduct(elem);
  } else {
    addProduct(product_cd, option_trm);
  }
};

const addProduct = (product_cd, option_trm) => {
  axios.post(`${depositstore.API_URL}/accounts/profile/add_product/${product_cd}/${option_trm}`, {}, {
    headers: {
      Authorization: `Token ${profilestore.token}`
    }
  })
  .then(response => {
    console.log(response.data);
    profilestore.getProfile();
    if (confirm("관심상품 목록을 확인하시겠습니까?") == true) {
      router.push({name: 'profile'})
    }
  })
  .catch(error => {
    console.error(error);
  });
};

const cancelProduct = (elem) => {
  axios.post(`${depositstore.API_URL}/accounts/profile/add_product/${elem}`, {}, {
    headers: {
      Authorization: `Token ${profilestore.token}`
    }
  })
  .then(response => {
    console.log(response.data);
    profilestore.getProfile();
  })
  .catch(error => {
    console.error(error);
  });
};


</script>


<style scoped>
.option-item {
  margin-bottom: 1rem;
}
</style>
