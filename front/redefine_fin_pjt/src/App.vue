<template>
  <div>
    <nav>
      <RouterLink :to="{name : 'profile'}">
        <img src="" alt="profile_img">
      </RouterLink>
      <RouterLink :to="{name : 'login'}">로그인</RouterLink>
      <RouterLink :to="{name : 'article'}">게시판</RouterLink>
      <RouterLink :to="{name : 'signup'}">회원가입</RouterLink>
      <RouterLink :to="{name : 'home'}">메인페이지</RouterLink>
      <RouterLink :to="{name : 'bankmap'}">지도</RouterLink>
    </nav>
  </div>
  <RouterView />
</template>

<script setup>
  import { RouterLink } from 'vue-router'
  
</script>

<style scoped>

</style>