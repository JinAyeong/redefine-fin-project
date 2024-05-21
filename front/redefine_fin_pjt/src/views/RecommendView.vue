<template>
  <div>
    <h1>상품 추천받기!</h1>
    <h3>나와 비슷한 사람들이 많이 가입한 상품</h3>
    {{ recommendstore.productAuto }}
  </div>
</template>

<script setup>

import { ref, onMounted } from 'vue'
import axios from 'axios';
import { useRecommendStore } from '@/stores/recommend'
import { useProfileStore } from '@/stores/profile';

const recommendstore = useRecommendStore()
const profilestore = useProfileStore()

onMounted(() => {
  recommendstore.recommendAuto(profilestore.token)
})

</script>

<style scoped>

</style>