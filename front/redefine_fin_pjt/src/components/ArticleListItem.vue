<template>
  <tr @click="router.push({name: 'articledetail', params: {id: article.id}})">
    <th scope="col">{{ article.id }}</th>
    <th scope="col">{{ article.title }}</th>
    <th v-if="article.created_at === article.updated_at" scope="col">{{ formatDate(article.created_at) }}</th>
    <th v-else scope="col">{{ formatDate(article.updated_at) }}</th>
    <th scope="col">{{ article.user_name }}</th>

    <!-- <RouterLink :to="{
      name: 'articledetail',
      params: {id: article.id}}">
      <p>{{ article.id }}번 게시글</p>
    </RouterLink>
    <p>제목 : {{ article.title }}</p>
    <p>내용 : {{ article.content }}</p>
    <hr> -->
  </tr>
</template>

<script setup>

import router from '@/router';
import { RouterLink } from 'vue-router';

defineProps({
  article: Object
})

const formatDate = (dateString) => {
  const date = new Date(dateString);
  return date.toLocaleString('ko-KR', {
    year: 'numeric',
    month: '2-digit',
    day: '2-digit',
  });
};

</script>

<style scoped>

</style>