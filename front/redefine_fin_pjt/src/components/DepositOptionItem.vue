<template>
  <div class="option-item card shadow-sm p-3 mb-4 position-relative">
    <div class="card-body">
      <h5 class="card-title">예금 상품 옵션 정보</h5>
      <hr>
      <p class="card-text">유형: {{ depositOption.intr_rate_type_nm }}</p>
      <p class="card-text">저축 단위: {{ depositOption.save_trm }} 개월</p>
      <p class="card-text">저축금리: {{ depositOption.intr_rate }} %</p>
      <p class="card-text">최고 우대 금리: {{ depositOption.intr_rate2 }} %</p>
      <button v-if="profilestore.userName" class="btn btn-outline-navy fixed-button" @click="addOrCancelProduct(depositOption.fin_prdt_cd, depositOption.id)">
        {{ isProductAdded(depositOption.fin_prdt_cd, depositOption.id) ? '가입 취소 하기' : '상품 가입하기' }}
      </button>
    </div>
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
  depositOption: {
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
      router.push({name: 'profileproduct'})
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
