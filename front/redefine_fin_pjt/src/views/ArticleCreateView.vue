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
import { useProfileStore } from '@/stores/profile';
import { useRouter } from 'vue-router';
import axios from 'axios';

const title = ref(null)
const content = ref(null)
const profilestore = useProfileStore()
const router = useRouter()


const createArticle = function () {

    axios({
      method: 'post',
      url: `${profilestore.API_URL}/articles/`,
      data: {
        title: title.value,
        content: content.value,
      },
      headers: {
        Authorization: `Token ${profilestore.token}`,
      }
    })
      .then(response => {
        console.log('게시글 생성 완료!')
        router.push({name: 'article'})
      })
      .catch(error => {
        console.log(error)
        console.log(profilestore.token)
      })
  }

</script>

<style scoped>

</style>