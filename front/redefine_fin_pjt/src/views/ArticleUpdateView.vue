<template>
    <div>
        <h1>게시글 수정</h1>
        <form @submit.prevent="updateArticle">
            <label for="title">제목 : </label>
            <input type="text" v-model.trim="title" id="title"><br>
            <label for="content">내용 : </label>
            <input type="text" v-model.trim="content" id="content"><br>
            <input type="submit" value="게시글 수정">
        </form>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useArticleStore } from '@/stores/article'
import { useProfileStore } from '@/stores/profile'
import axios from 'axios'

const route = useRoute()
const router = useRouter()
const articlestore = useArticleStore()
const profilestore = useProfileStore()

const articleId = route.params.id
const article = ref(null)
const title = ref('')
const content = ref('')

const loadArticle = async () => {
    try {
        const response = await axios.get(`${articlestore.API_URL}/articles/${articleId}/`, {
            headers: {
                Authorization: `Token ${profilestore.token}`,
            },
        })
        article.value = response.data
        title.value = response.data.title
        content.value = response.data.content
    } catch (error) {
        console.error('Error loading article:', error)
    }
}

onMounted(() => {
    loadArticle()
})

const updateArticle = async () => {
    try {
        await axios({
            method: 'put',
            url: `${articlestore.API_URL}/articles/${articleId}/`,  // Ensure the trailing slash if required by the backend framework
            headers: {
                Authorization: `Token ${profilestore.token}`,
            },
            data: {
                title: title.value,
                content: content.value,
            },
        })
        console.log('게시물 수정 완료!')
        await loadArticle() // Reload the article to get the updated data
        router.push({ name: 'article' })
    } catch (error) {
        console.error('Error updating article:', error)
        if (error.response) {
            console.error('Error response data:', error.response.data)
            console.error('Error response status:', error.response.status)
        }
    }
}
</script>
