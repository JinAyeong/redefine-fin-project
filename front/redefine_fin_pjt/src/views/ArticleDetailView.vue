<template>
  <div>
    <body class="d-flex flex-column">
      <main class="flex-shrink-0">
        <!-- Page Content-->
        <section class="py-5">
          <div class="container px-5 my-5">
            <div class="row gx-5">
              <div class="col-lg-3">
                <div class="d-flex align-items-center mt-lg-5 mb-4">
                  <img class="img-fluid rounded-circle" src="https://dummyimage.com/50x50/ced4da/6c757d.jpg" alt="..." />
                  <div class="ms-3">
                    <div class="fw-bold">{{ article.user_name }}</div>
                    <div class="text-muted">{{ article.user_name_2 }}</div>
                  </div>
                </div>
              </div>
              <div class="col-lg-9">
                <!-- Post content-->
                <article>
                  <!-- Post header-->
                  <header class="mb-4">
                    <!-- Post title-->
                    <h1 class="fw-bolder mb-1">{{ article.title }}</h1>
                    <!-- Post meta content-->
                    <div class="text-muted fst-italic mb-2">
                      <p v-if="article.created_at === article.updated_at">{{ formatDate(article.created_at) }}</p>
                      <p v-else>수정시간 : {{ formatDate(article.updated_at) }}</p>
                    </div>
                  </header>
                  <!-- Post content-->
                  <section class="mb-5">
                    <p>{{ article.content }}</p>
                    <div v-if="userProfile.username === article.user_name" class="d-flex justify-content-end gap-2">
                      <button @click="deleteArticle" class="btn btn-outline-secondary">게시물 삭제</button>
                      <button @click="articleUpdate" class="btn btn-outline-secondary">게시물 수정</button>
                    </div>
                    <!-- 좋아요 버튼 (본인 게시물일 경우 좋아요 버튼 X) -->
                    <div v-if="userProfile.username != article.user_name" class="d-flex justify-content-center gap-2">
                      <button @click="toggleLike" class="btn btn-outline-secondary">
                        <span>{{ LikeUsers.length }} {{ isLiked ? '💙' : '🤍' }}</span>
                      </button>
                    </div>
                  </section>
                </article>
                <!-- Comments section-->
                <section>
                  <div class="card bg-light">
                    <div class="card-body">
                      <!-- Comment form-->
                      <form @submit.prevent="createComment" class="mb-4 d-flex flex-column">
                        <textarea v-model="commentContent" class="form-control mb-2 " rows="3" placeholder="댓글을 입력해주세요"></textarea>
                        <div class="d-flex justify-content-end">
                          <button type="submit" class="btn btn-secondary">댓글 작성</button>
                        </div>
                      </form>
                      <!-- Single comment-->
                      <div v-if="comments.length">
                        <div class="ms-3" v-for="comment in comments" :key="comment.id">
                          <div class="fw-bold">{{ comment.user.username }}</div>
                          {{ comment.content }}
                          <!-- 본인 댓글만 삭제 가능 -->
                          <button v-if="isCommentAuthor(comment)" @click="deleteComment(comment.id)" class="btn btn-outline-secondary btn-sm">X</button>
                        </div>
                      </div>
                    </div>
                  </div>
                </section>
              </div>
            </div>
          </div>
        </section>
      </main>
    </body>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router';
import axios from 'axios';
import { useArticleStore } from '@/stores/article';
import { useProfileStore } from '@/stores/profile';

const route = useRoute()
const router = useRouter()
const articlestore = useArticleStore()
const profilestore = useProfileStore()
const userProfile = profilestore.userProfile;
const isLiked = ref()
// 해당 article 가져오기
const articleId = route.params.id
const article = ref(
    articlestore.articles.find((product) => product.id == articleId)
)
const LikeUsers = ref([])

const formatDate = (dateString) => {
  const date = new Date(dateString);
  return date.toLocaleString('ko-KR', {
    year: 'numeric',
    month: '2-digit',
    day: '2-digit',
    hour: '2-digit',
    minute: '2-digit',
  });
};

// 게시물 삭제
const deleteArticle = function () {
  if (confirm("게시글을 삭제하시겠습니까?") == true) {
    axios({
      method: 'delete',
      url: `${profilestore.API_URL}/articles/${articleId}`,
      headers: {
        Authorization: `Token ${profilestore.token}`
      },
    })
    .then((response) => {
      console.log('게시물 삭제 완료!')
      router.push({name: 'article'})
    })
    .catch((error) => {
      console.log(profilestore.token)
      console.log(error)
    })
  }
}

// 게시글 수정 view로 이동
const articleUpdate = function () {
  router.push({name: 'articleupdate', params: {id: articleId}});
};

// 좋아요 상태를 가져오는 함수
const fetchLikeStatus = () => {
  axios.get(`http://127.0.0.1:8000/articles/${articleId}/like-status/`, {
    headers: {
      Authorization: `Token ${profilestore.token}`
    }
  })
  .then(response => {
    // 서버에서 받은 좋아요 상태를 반영
    isLiked.value = response.data.is_liked
  })
  .catch(error => {
    console.error('좋아요 상태 가져오기 실패:', error)
  })
}

// 좋아요 토글 함수
const toggleLike = () => {
  axios.post(`http://127.0.0.1:8000/articles/${articleId}/likes/`, {}, {
    headers: {
      Authorization: `Token ${profilestore.token}`
    }
  })
  .then(response => {
    // 서버에서 받은 좋아요 상태를 반영
    isLiked.value = response.data.is_liked
    if (isLiked.value === true) {LikeUsers.value.push('1')}
    else {LikeUsers.value.pop()}
    // console.log(LikeUsers)
  })
  .catch(error => {
    console.error('좋아요 토글 실패:', error)
  })
}

// =================================================================================
// comment 관련
const commentContent = ref('')
const comments = ref([])

// 댓글 생성
const createComment = () => {
  axios({
    method: 'post',
    url: `http://127.0.0.1:8000/articles/${articleId}/comments/create/`,
    headers: {
      Authorization: `Token ${profilestore.token}`
    },
    data: {
      content: commentContent.value
    }
  })
  .then((response) => {
    comments.value.push(response.data)
    commentContent.value = ''
  })
  .catch((error) => {
    console.log(error)
    // console.error('댓글 작성 실패:', error)
    // window.alert('댓글 작성 중 에러가 발생했습니다.')
  })
}

const isCommentAuthor = (comment) => {
  return comment.user.username === profilestore.userName
}

const deleteComment = (commentId) => {
  if (confirm("댓글을 삭제하시겠습니까?") == true) {
    axios({
      method: 'delete',
      url: `http://127.0.0.1:8000/articles/comments/${commentId}/delete/`,
      headers: {
        Authorization: `Token ${profilestore.token}`
      }
    })
    .then(() => {
      comments.value = comments.value.filter(comment => comment.id !== commentId)
    })
    .catch((error) => {
      console.log(error)
    })
  }
}

// 댓글 목록 가져오기
const fetchComments = () => {
  axios({
    method: 'get',
    url: `http://127.0.0.1:8000/articles/${articleId}/comments/`,
    headers: {
      Authorization: `Token ${profilestore.token}`
    }
  })
  .then((response) => {
    comments.value = response.data
  })
  .catch((error) => {
    console.log(error)
  })
}

onMounted(() => {
  fetchLikeStatus() // 좋아요 상태를 가져옵니다.
  fetchComments()
  profilestore.getProfile()
})
</script>

<style scoped>
.d-flex.justify-content-end.gap-2 > button {
  min-width: 100px;
}
</style>
