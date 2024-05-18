<template>
    <div>
        <h1>게시글 수정</h1>
        <form @submit.prevent="updateArticle">
        <label for="title">제목 : </label>
        <input type="text" v-model.trim="title"><br>
        <label for="content">내용 : </label>
        <input type="text" v-model.trim="content"><br>
        <input type="submit" value="게시글 수정">
    </form>
    </div>
</template>

<script setup>

import { ref, onMounted, onUpdated } from 'vue'
import { useRoute, useRouter } from 'vue-router';
import { useArticleStore } from '@/stores/article';
import { useProfileStore } from '@/stores/profile';
import axios from 'axios';

const route = useRoute()
const router = useRouter()
const articlestore = useArticleStore()
const profilestore = useProfileStore()

const articleId = route.params.id
const article = ref(
    articlestore.articles.find((product) => product.id == articleId)
)
const title = ref(article.value.title)
const content = ref(article.value.content)
// const article = ref(null)
// const title = ref(null)
// const content = ref(null)

// 게시물 수정
const updateArticle = function () {
    axios({
        method: 'put',
        url: `${articlestore.API_URL}/articles/${articleId}/`,
        headers: {
            Authorization: `Token ${profilestore.token}`
        },
        data: {
            title: title.value,
            content: content.value,
        },
    })
        .then((response) => {
            console.log('게시물 수정 완료!')
            router.push({name: 'articledetail', params: {id: articleId}})
        })
        .catch((error) => {
            console.log(profilestore.token)
            console.log(error)
        })
}

// 게시물 불러오기
// onMounted(() => {
//     axios({
//         method: 'get',
//         url: `${articlestore.API_URL}/articles/${articleId}`
//     })
//         .then((response) => {
//             article.value = response.data
//             title.value = response.data.title
//             content.value = response.data.content
//         })
//         .catch((error) => {
//             console.log(error)
//         })
// })


</script>

<style scoped>

</style>