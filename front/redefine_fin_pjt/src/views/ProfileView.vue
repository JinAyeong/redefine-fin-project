<template>
    <div v-if="profilestore.token">
        <h1>Profile Page</h1>
        <p>아이디 : {{ userProfile.username }}</p>
        <p>이름 : {{ userProfile.name }}</p>
        <p>이메일 : {{ userProfile.email }}</p>
        <p>나이 : {{ userProfile.age }}</p>
        <p>자산 : {{ userProfile.money }}</p>
        <p>연봉 : {{ userProfile.salary }}</p>
        <p v-if="userProfile.financial_products">가입 상품 리스트 : {{ userProfile.financial_products }}</p>
        <p v-else>아직 가입한 상품이 없습니다.</p>
        <RouterLink :to="{name: 'profileupdate'}"><button>회원정보 수정</button></RouterLink>
        <RouterLink :to="{name: 'passwordupdate'}"><button>비밀번호 변경</button></RouterLink>
        <button>내가 쓴 글 보기</button>

        <h1>좋아요한 게시글 리스트</h1>
        <div v-if="likedArticles.length">
        <div v-for="article in likedArticles" :key="article.id" class="article">
            <h2>{{ article.title }}</h2>
            <p>{{ article.content }}</p>
            <p>작성자: {{ article.user_name }}</p>
            <p>작성시간: {{ article.created_at }}</p>
            <hr>
        </div>
        </div>
        <div v-else>좋아요한 게시글 없음</div>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { RouterLink } from 'vue-router';
import { useProfileStore } from '@/stores/profile';
import axios from 'axios';

const profilestore = useProfileStore()
const userProfile = profilestore.userProfile
const likedArticles = ref([])
const loading = ref(true)

const fetchLikedArticles = () => {
  axios.get('http://127.0.0.1:8000/articles/liked_articles/', {
    headers: {
      Authorization: `Token ${profilestore.token}`
    }
  })
  .then(response => {
    likedArticles.value = response.data
  })
  .catch(error => {
    console.error('좋아요한 게시글 리스트를 가져오는 중 에러 발생:', error)
  })
}

onMounted(() => {
  fetchLikedArticles()
})

</script>

<style scoped>

</style>