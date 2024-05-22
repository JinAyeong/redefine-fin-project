<template>

<body class="d-flex flex-column h-100">
        <main class="flex-shrink-0">
            <!-- Page Content-->
            <section class="py-5">
                <div class="container px-5 my-5">
                    <div class="text-center mb-5">
                        <h1 class="fw-bolder">후기 게시판</h1>
                        <p class="lead fw-normal text-muted mb-0">금융 상품을 한눈에 비교하세요!</p>
                    </div>
                    <table class="table table-hover">
                      <thead>
                        <tr>
                          <th scope="col">#</th>
                          <th scope="col">제목</th>
                          <th scope="col">작성시간</th>
                          <th scope="col">작성자</th>
                        </tr>
                      </thead>
                      <tbody>
                          <template v-if="store.articles">
                            <ArticleListItem 
                              v-for="article in store.articles"
                              :key="article.id"
                              :article="article"/>
                          </template>
                      </tbody>
                    </table>



                    <!--광고-->
                    <div class="row gx-5">

                        <div class="col-xl-4">
                            <div class="card border-0 bg-light mt-xl-5">
                                <div class="card-body p-4 py-lg-5">
                                    <div class="d-flex align-items-center justify-content-center">
                                        <div class="text-center">
                                            <div class="h6 fw-bolder">Have more questions?</div>
                                            <p class="text-muted mb-4">
                                                Contact us at
                                                <br />
                                                <a href="#!">support@domain.com</a>
                                            </p>
                                            <div class="h6 fw-bolder">Follow us</div>
                                            <a class="fs-5 px-2 link-dark" href="#!"><i class="bi-twitter"></i></a>
                                            <a class="fs-5 px-2 link-dark" href="#!"><i class="bi-facebook"></i></a>
                                            <a class="fs-5 px-2 link-dark" href="#!"><i class="bi-linkedin"></i></a>
                                            <a class="fs-5 px-2 link-dark" href="#!"><i class="bi-youtube"></i></a>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </section>
        </main>
    </body>




  <!-- <div v-if="store.articles">
    <ArticleListItem 
      v-for="article in store.articles"
      :key="article.id"
      :article="article"/>
  </div> -->
</template>

<script setup>

import { onMounted } from 'vue'
import { useArticleStore } from '@/stores/article';
import ArticleListItem from '@/components/ArticleListItem.vue'

const store = useArticleStore()

onMounted(() => {
  store.getArticles()
})

</script>

<style scoped>

</style>