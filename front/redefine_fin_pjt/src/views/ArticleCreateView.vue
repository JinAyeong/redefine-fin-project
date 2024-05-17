<template>
  <div>
    <h1>게시글 생성 페이지</h1>
    <form @submit.prevent="createArticle">
      <label for="title">제목 : </label>
      <input type="text" v-model.trim="title"><br>
      <label for="content">내용 : </label>
      <input type="text" v-model.trim="content"><br>
      <input type="submit" value="게시글 작성">
    </form>
  </div>
</template>

<script setup>

import { ref } from 'vue'
// import { useArticleStore } from '@/stores/article';
import { useProfileStore } from '@/stores/profile';
import axios from 'axios';

// const store = useArticleStore()
const store = useProfileStore()

const title = ref(null)
const content = ref(null)

const createArticle = function () {

    axios({
      method: 'post',
      url: `${store.API_URL}/articles/`,
      data: {
        title: title.value,
        content: content.value
      },
      headers: {
        Authorization: `Token ${store.token}`
      }
    })
      .then(response => {
        console.log('게시글 생성 완료!')
      })
      .catch(error => {
        console.log(error)
        console.log(store.token)
      })
  }

// const createArticle = function () {
//     const payload = {
//         title: title.value,
//         content: content.value
//     }
//     store.createArticle(payload)
// }

</script>

<style scoped>

</style>