<template>
  <div>
    <RouterLink :to="{
      name: 'articledetail',
      params: {id: article.id}}">
      <p>{{ article.id }}번 게시글</p>
    </RouterLink>
    <p>제목 : {{ article.title }}</p>
    <p>내용 : {{ article.content }}</p>
    <hr>
  </div>
</template>

<script setup>

import { RouterLink } from 'vue-router';

defineProps({
  article: Object
})

</script>

<style scoped>

</style>