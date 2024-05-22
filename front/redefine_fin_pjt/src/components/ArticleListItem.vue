<template>
  <tr>

    <th scope="col">{{ article.id }}</th>
    <th scope="col">
    <RouterLink :to="{
      name: 'articledetail',
      params: {id: article.id}}">
      {{ article.title }}
    </RouterLink></th>
    <th scope="col">{{ article.created_at }}</th>
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

import { RouterLink } from 'vue-router';

defineProps({
  article: Object
})

</script>

<style scoped>

</style>