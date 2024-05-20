<template>
  <div>
    <h1>금리 비교</h1>
    <RouterLink :to="{name: 'deposit'}">예금</RouterLink>
    <RouterLink :to="{name: 'saving'}">적금</RouterLink>
    
    <RouterView />
  </div>
</template>

<script setup>

import { RouterLink } from 'vue-router'

</script>

<style scoped>

</style>