<template>

  <body class="d-flex flex-column">
      <main class="flex-shrink-0">
        <!-- Pricing section-->
        <section class="bg-light py-5">
          <div class="container px-5 my-5">
            <div class="text-center mb-5">
              <h1 class="fw-bolder">나의 정보</h1>
              <p class="lead fw-normal text-muted mb-0">
                <i class="bi bi-check text-primary"></i>맞춤 상품 추천을 위한 나의 정보
              </p>
            </div>
            <div class="row gx-5 justify-content-center">
              <!-- Pricing card enterprise-->
              <div class="col-lg-6 col-xl-4" v-if="profilestore.token">
                <div class="card">
                  <div class="card-body p-5">
                    <!-- <div class="small text-uppercase fw-bold text-muted">profile</div>
                    <div class="mb-3">
                      <span class="display-4 fw-bold">$49</span>
                      <span class="text-muted">/ mo.</span>
                    </div> -->
                    <ul class="list-unstyled mb-4">
                      <li class="mb-2 d-flex justify-content-between">
                        <strong>이름</strong>
                        <span>{{ userProfile.name }}</span>
                      </li>
                      <li class="mb-2 d-flex justify-content-between">
                        <strong>아이디</strong>
                        <span>{{ userProfile.username }}</span>
                      </li>
                      <li class="mb-2 d-flex justify-content-between">
                        <strong>이메일</strong>
                        <span>{{ userProfile.email }}</span>
                      </li>
                      <li class="mb-2 d-flex justify-content-between">
                        <strong>나이</strong>
                        <span>{{ userProfile.age }}</span>
                      </li>
                      <li class="mb-2 d-flex justify-content-between">
                        <strong>자산</strong>
                        <span>{{ userProfile.money }}</span>
                      </li>
                      <li class="mb-2 d-flex justify-content-between">
                        <strong>연봉</strong>
                        <span>{{ userProfile.salary }}</span>
                      </li>
                    </ul>
                    <div @click="router.push({name: 'profileproduct'})" class="d-grid">
                      <a class="btn btn-secondary" href="#!">나의 관심상품 보러 가기</a>
                    </div>
                    <div @click="router.push({name: 'profileupdate'})" class="d-grid">
                      <a class="btn btn-light" href="#!">나의정보 수정</a>
                    </div>
                    <div @click="router.push({name: 'passwordupdate'})" class="d-grid">
                      <a class="btn btn-light" href="#!">비밀번호 변경</a>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </section>
      </main>
    </body>





  <div v-if="profilestore.token">    
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
import { useRouter } from 'vue-router';
import { useProfileStore } from '@/stores/profile';
import axios from 'axios';

const profilestore = useProfileStore();
const userProfile = profilestore.userProfile;
const likedArticles = ref([]);
const router = useRouter()
const loading = ref(true);

onMounted(() => {
  fetchLikedArticles();
  profilestore.getProfile();
});

// 좋아요한 게시글 불러오기
const fetchLikedArticles = () => {
  axios.get('http://127.0.0.1:8000/articles/liked_articles/', {
    headers: {
      Authorization: `Token ${profilestore.token}`
    }
  })
  .then(response => {
    likedArticles.value = response.data;
  })
  .catch(error => {
    console.error('좋아요한 게시글 리스트를 가져오는 중 에러 발생:', error);
  });
};
</script>

<style scoped>
.article {
  margin-bottom: 1rem;
}
</style>
