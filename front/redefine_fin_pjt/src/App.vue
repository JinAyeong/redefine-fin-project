<template class="d-flex flex-column h-100">
      <main class="flex-shrink-0">
          <!-- Navigation-->
          <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
              <div class="container px-5">
                  <a class="navbar-brand" href="http://localhost:5173/"><img src="C:\Users\Jin\Desktop\PJT\redefine-fin-project\front\imgs\Logo.png" alt=""></a>
                  <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation"><span class="navbar-toggler-icon"></span></button>
                  <div class="collapse navbar-collapse" id="navbarSupportedContent">
                      <ul class="navbar-nav ms-auto mb-2 mb-lg-0">
                        <li class="nav-item"><RouterLink class="nav-link" :to="{name : 'article'}">게시판</RouterLink></li>
                          <li class="nav-item"><RouterLink class="nav-link" :to="{name : 'bankmap'}">지도</RouterLink></li>
                          <li class="nav-item"><RouterLink class="nav-link" :to="{name : 'finance'}">예적금상품</RouterLink></li>
                          <li class="nav-item"><RouterLink class="nav-link" :to="{name : 'exchange'}">환율계산기</RouterLink></li>
                          <li class="nav-item"><RouterLink class="nav-link" :to="{name : 'aichat'}">AI Chat</RouterLink></li>
                          <li class="nav-item"></li>

                          <span v-if="profilestore.userName" class="navbar-nav mb-2 mb-lg-0">
                            <li class="nav-item"><a class="nav-link" @click="profilestore.logOut">로그아웃</a></li>
                            <li class="nav-item"><a class="nav-link">{{ profilestore.userProfile.name }}님 환영합니다</a></li>
                          </span>

                          <span v-else class="navbar-nav mb-2 mb-lg-0">
                            <li class="nav-item"><RouterLink class="nav-link" :to="{name : 'login'}">로그인</RouterLink></li>
                            <li class="nav-item"><RouterLink class="nav-link" :to="{name : 'signup'}">회원가입</RouterLink></li>
                          </span>
                      </ul>
                  </div>
              </div>
          </nav>
      </main>
    <RouterView />
</template>

<script setup>
  import { useRouter } from 'vue-router';
  import { RouterLink } from 'vue-router'
  import { useProfileStore } from './stores/profile';
  const router = useRouter()
  const profilestore = useProfileStore()
  
  const goBack = function () {
    router.go(-1)
  }

</script>

<style scoped>

</style>