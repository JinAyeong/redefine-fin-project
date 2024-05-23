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
            <!-- Profile card section -->
            <div class="col-lg-3 mx-5" v-if="profilestore.token">
              <div class="card custom-card">
                <div class="card-body p-5">
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
                  <div @click="router.push({ name: 'profileproduct' })" class="d-grid mb-2">
                    <a class="btn btn-secondary" href="#!">나의 관심상품 보러 가기</a>
                  </div>
                  <div @click="router.push({ name: 'profileupdate' })" class="d-grid mb-2">
                    <a class="btn btn-light" href="#!">나의정보 수정</a>
                  </div>
                  <div @click="router.push({ name: 'passwordupdate' })" class="d-grid mb-2">
                    <a class="btn btn-light" href="#!">비밀번호 변경</a>
                  </div>
                </div>
              </div>
            </div>
            <!-- articles section -->
            <div class="col-lg-7 mx-5">
              <div v-if="profilestore.token">
                <h4 class="fw-bolder">좋아요한 게시글</h4>
                <div v-if="likedArticles.length">
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
                      <tr
                        v-for="article in likedArticles"
                        :key="article.id"
                        class="article"
                        @click="router.push({ name: 'articledetail', params: { id: article.id } })"
                      >
                        <th scope="col" class="col-1">{{ article.id }}</th>
                        <th scope="col" class="col-6">{{ article.title }}</th>
                        <th
                          v-if="article.created_at === article.updated_at"
                          scope="col"
                          class="col-2"
                        >{{ formatDate(article.created_at) }}</th>
                        <th v-else scope="col" class="col-2">{{ formatDate(article.updated_at) }}</th>
                        <th scope="col" class="col-3">{{ article.user_name }}</th>
                      </tr>
                    </tbody>
                  </table>
                </div>
                <div v-else>좋아요한 게시글 없음</div>
              </div>
            </div>
          </div>
        </div>
      </section>
    </main>
  </body>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import { useProfileStore } from '@/stores/profile';
import axios from 'axios';

const profilestore = useProfileStore();
const userProfile = profilestore.userProfile;
const likedArticles = ref([]);
const router = useRouter();

onMounted(() => {
  fetchLikedArticles();
  profilestore.getProfile();
});

// 좋아요한 게시글 불러오기
const fetchLikedArticles = async () => {
  try {
    const response = await axios.get('http://127.0.0.1:8000/articles/liked_articles/', {
      headers: {
        Authorization: `Token ${profilestore.token}`
      }
    });
    console.log('좋아요한 게시글 리스트:', response.data);  // 콘솔 로그로 확인
    likedArticles.value = response.data;
  } catch (error) {
    console.error('좋아요한 게시글 리스트를 가져오는 중 에러 발생:', error);
  }
};

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
.article {
  margin-bottom: 1rem;
}

.custom-card {
  width: 125%;
}

.mx-3 {
  margin-left: 1rem !important;
  margin-right: 1rem !important;
}
</style>
