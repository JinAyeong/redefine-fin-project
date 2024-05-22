<template>
  <div>
    <body class="d-flex flex-column">
        <main class="flex-shrink-0">
            <!-- Page Content-->
            <section class="py-5">
                <div class="container px-5 my-5">
                    <div class="text-center mb-5">
                        <h1 class="fw-bolder">게시글 작성</h1>
                        <p class="lead fw-normal text-muted mb-0">후기를 남겨주세요!</p>
                    </div>
                    <div class="row gx-5 justify-content-center">
                        <div class="col-lg-9">
                            <!-- Comments section-->
                            <section>
                                <div class="card bg-light">
                                    <div class="card-body">
                                        <!-- Comment form-->
                                        <form @submit.prevent="createArticle">
                                          <div class="mb-4"><textarea v-model.trim="title" class="form-control" rows="1" placeholder="제목을 입력해주세요"></textarea></div>
                                          <div class="mb-4"><textarea v-model.trim="content" class="form-control" rows="20" placeholder="내용을 입력해주세요"></textarea></div>
                                          <div class="d-flex justify-content-end">
                                            <input type="submit" value="게시글 작성" class="btn btn-secondary">
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
        router.push({ name: 'article' })
      })
      .catch(error => {
        console.log(error)
        console.log(profilestore.token)
      })
  }
</script>

<style scoped>
/* 추가 스타일을 원한다면 여기서 정의할 수 있습니다. */
</style>
