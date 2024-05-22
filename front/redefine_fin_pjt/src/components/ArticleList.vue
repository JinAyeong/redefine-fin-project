<template>
    <table class="table table-hover">
    <thead>
      <tr>
        <th scope="col" class="col-1">#</th>
        <th scope="col" class="col-6">제목</th>
        <th scope="col" class="col-3">작성시간</th>
        <th scope="col" class="col-2">작성자</th>
      </tr>
    </thead>
    <tbody>
      <template v-if="store.articles">
        <ArticleListItem 
          v-for="article in store.articles"
          :key="article.id"
          :article="article"/>
      </template>
    </tbody>
  </table>
</template>

<script setup>
import { onMounted } from 'vue'
import { useArticleStore } from '@/stores/article';
import ArticleListItem from '@/components/ArticleListItem.vue'

const store = useArticleStore()

onMounted(() => {
  store.getArticles()
})
</script>

<style scoped>
/* 원하는 추가 스타일을 정의할 수 있습니다 */
</style>
