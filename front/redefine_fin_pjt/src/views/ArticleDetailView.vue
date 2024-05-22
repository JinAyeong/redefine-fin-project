<template>
    <div>
      <h1>디테일페이지</h1>
      <p v-if="article.created_at === article.updated_at">작성시간 : {{ article.created_at }}</p>
      <p v-if="article.created_at !== article.updated_at">수정시간 : {{ article.updated_at }}</p>

      <!-- 본인일 경우에만 게시글 조작 버튼 출력되도록 -->
      <div v-if="userProfile.username===article.user_name">
        <button @click="deleteArticle">게시물 삭제</button>
        <button @click="articleUpdate">게시물 수정</button>
      </div>


      <p>작성자 : {{ article.user_name }}</p>
      <p>제목 : {{ article.title }}</p>
      <p>내용 : {{ article.content }}</p>
      <p>좋아요 수 : {{ LikeUsers.length }}</p>
      <hr>


      <!-- 댓글  -->
      <textarea v-model.trim="commentContent"></textarea><br>
      <button @click="createComment">댓글 작성</button>
      <hr>
      <h2 v-if="comments.length">댓글 목록</h2>
      <div v-for="comment in comments" :key="comment.id">
        <p>{{ comment.user.username }} - {{ comment.content }}</p>

          <!-- 본인 댓글만 삭제 가능 -->
            <button v-if="isCommentAuthor(comment)" @click="deleteComment(comment.id)">댓글 삭제</button>
          <hr>
      </div>


      <!-- 좋아요 버튼 (본인 게시물일 경우 좋아요 버튼 X) -->
      <div v-if="userProfile.username != article.user_name">
        <button v-if="!isLiked" @click="toggleLike">
          <span>좋아요</span>
        </button>
        <button v-if="isLiked" @click="toggleLike">
          <span>좋아요 취소</span>
        </button>
      </div>
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
//   console.log('Current user:', profilestore.userName)
//   console.log('Comment user:', comment.user.username)
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

</style>