<template>
  <div>
    <nav>
      <RouterLink :to="{name : 'profile'}">
        <img src="" alt="profile_img">
      </RouterLink>
      <RouterLink :to="{name : 'article'}">게시판</RouterLink>
      <RouterLink :to="{name : 'bankmap'}">지도</RouterLink>
      <RouterLink :to="{name : 'home'}">메인페이지</RouterLink>
      <span v-if="!profilestore.isLogin">
        <RouterLink :to="{name : 'signup'}">회원가입</RouterLink>
        <RouterLink :to="{name : 'login'}">로그인</RouterLink>
      </span>
      <span v-if="profilestore.isLogin">
        <span>환영해~</span>
        <button @click="profilestore.logOut">로그아웃</button>
      </span>
    </nav>
  </div>
  <RouterView />
</template>

<script setup>
  import { RouterLink } from 'vue-router'
  import { useProfileStore } from '@/stores/profile';
  const profilestore = useProfileStore()
  
</script>

<style scoped>

</style>