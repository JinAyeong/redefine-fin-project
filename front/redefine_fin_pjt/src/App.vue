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
<<<<<<< HEAD
      <RouterLink :to="{name : 'bankmap'}">지도</RouterLink>
=======
      <p v-if="profilestore.isLogin">환영해~</p>
>>>>>>> fcfc8bc056adb64813e42abbef1e95cbddafae02
    </nav>
  </div>
  <RouterView />
</template>

<script setup>
  import { RouterLink } from 'vue-router'
  import { useProfileStore } from './stores/profile';
  const profilestore = useProfileStore()
  
</script>

<style scoped>

</style>