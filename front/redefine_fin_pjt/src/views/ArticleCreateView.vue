<template>
  <div>
    <h1>게시글 생성 페이지</h1>
    <form @submit.prevent="articleCreate">
      제목 : <input v-model.trim="title" type="text">
      내용 : <input v-model.trim="content" type="text">
      <input type="submit" value="제출">
    </form>
  </div>
</template>

<script setup>

import { ref } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'
import { useArticleStore } from '@/stores/article'

const router = useRouter()
const title = ref(null)
const content = ref(null)
const store = useArticleStore()

const articleCreate = function () {
  axios({
    method: 'post',
    url: `${store.API_URL}/api/v1/articles/`,
    data: {
      title: title.value,
      content: content.value
    }
      .then(() => {
        
      })
  })
}

</script>

<style scoped>

</style>