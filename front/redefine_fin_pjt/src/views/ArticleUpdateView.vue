<template>
    <div>
      <body class="d-flex flex-column">
          <main class="flex-shrink-0">
              <!-- Page Content-->
              <section class="py-5">
                  <div class="container px-5 my-5">
                      <div class="text-center mb-5">
                          <h1 class="fw-bolder">게시글 수정</h1>
                          <p class="lead fw-normal text-muted mb-0">후기를 수정해주세요!</p>
                      </div>
                      <div class="row gx-5 justify-content-center">
                          <div class="col-lg-9">
                              <!-- Comments section-->
                              <section>
                                  <div class="card bg-light">
                                      <div class="card-body">
                                          <!-- Comment form-->
                                          <form @submit.prevent="updateArticle">
                                            <div class="mb-4"><textarea v-model.trim="title" class="form-control" rows="1" placeholder="제목을 입력해주세요"></textarea></div>
                                            <div class="mb-4"><textarea v-model.trim="content" class="form-control" rows="20" placeholder="내용을 입력해주세요"></textarea></div>
                                            <div class="d-flex justify-content-end">
                                              <input type="submit" value="게시글 수정" class="btn btn-secondary">
                                            </div>
                                          </form>
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


<!-- <template>
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
</template> -->

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

// 게시글 불러오기
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

// 게시글 수정
const updateArticle = async () => {
    try {
        await axios({
            method: 'put',
            url: `${articlestore.API_URL}/articles/${articleId}/`,
            headers: {
                Authorization: `Token ${profilestore.token}`,
            },
            data: {
                title: title.value,
                content: content.value,
            },
        })
        console.log('게시물 수정 완료!')
        await loadArticle()
        router.push({name: 'article'});
        alert('게시물이 수정되었습니다.')
    } catch (error) {
        console.error('Error updating article:', error)
        if (error.response) {
            console.error('Error response data:', error.response.data)
            console.error('Error response status:', error.response.status)
        }
    }
}
</script>
