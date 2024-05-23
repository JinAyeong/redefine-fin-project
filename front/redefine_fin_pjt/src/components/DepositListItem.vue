<template>
  <RouterLink :to="{
    name: 'depositdetail',
    params: { fin_prdt_cd: depositProduct.fin_prdt_cd }}"
    class="col-lg-4 col-md-6 mb-4"
  >
    <div class="card h-100 shadow border-30">
      <div class="card-body p-4">
        <div class="badge bg-primary bg-gradient rounded-pill mb-2">
          {{ depositProduct.kor_co_nm }}
        </div>
        <a class="text-decoration-none link-dark stretched-link" href="#!">
          <div class="h5 card-title mb-3">
            {{ depositProduct.fin_prdt_nm }}
          </div>
        <hr>
        <p>{{ depositProduct.etc_note }}</p>

        </a>
      </div>
    </div>
  </RouterLink>
</template>

<script setup>
import { RouterLink } from 'vue-router';
import { defineProps } from 'vue';

defineProps({
  depositProduct: Object
});
</script>
<style scoped>
a {
 text-decoration: none
}
</style>
