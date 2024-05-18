<template>
    <div>
        <h1>디테일페이지</h1>
        <p v-if="article.created_at === article.updated_at">작성시간 : {{ article.created_at }}</p>
        <p v-if="article.created_at !== article.updated_at">수정시간 : {{ article.updated_at }}</p>
        <button @click="deleteArticle">게시물 삭제</button>
        <button @click="articleUpdate">게시물 수정</button>
        <p>작성자 : {{ article.user_name }}</p>
        <p>제목 : {{ article.title }}</p>
        <p>내용 : {{ article.content }}</p>

    </div>
</template>

<script setup>

import { ref } from 'vue'
import { useRoute, useRouter } from 'vue-router';
import axios from 'axios';
import { useArticleStore } from '@/stores/article';
import { useProfileStore } from '@/stores/profile';

const route = useRoute()
const router = useRouter()
const articlestore = useArticleStore()
const profilestore = useProfileStore()

// 해당 article 가져오기
const articleId = route.params.id
const article = ref(
    articlestore.articles.find((product) => product.id == articleId)
)

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


</script>

<style scoped>

</style>