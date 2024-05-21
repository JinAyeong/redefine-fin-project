<template>
  <div>
    <nav>
      <button @click="goBack">뒤로가기</button>
      <RouterLink :to="{name : 'article'}">게시판</RouterLink>
      <RouterLink :to="{name : 'home'}">메인페이지</RouterLink>
      <RouterLink :to="{name : 'bankmap'}">지도</RouterLink>
      <RouterLink :to="{name : 'finance'}">예적금상품</RouterLink>
      <RouterLink :to="{name : 'exchange'}">환율계산기</RouterLink>
      <RouterLink :to="{name : 'aichat'}">AI Chat</RouterLink>
      <span v-if="profilestore.userName">
        <RouterLink :to="{name : 'profile'}">
          <img src="" alt="profile_img">
        </RouterLink>
        <span>{{ profilestore.userName }}님 어솨~^^</span>
        <button @click="profilestore.logOut">로그아웃</button>
      </span>
      <span v-else>
        <RouterLink :to="{name : 'login'}">로그인</RouterLink>
        <RouterLink :to="{name : 'signup'}">회원가입</RouterLink>
      </span>
    </nav>
  </div>
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