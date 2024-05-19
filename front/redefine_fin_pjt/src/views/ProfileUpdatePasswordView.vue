<template>
  <div>
    <h1>비밀번호 변경</h1>
    <form @submit.prevent="updatePassword">
      <div>
        <label for="old_password">기존 비밀번호</label>
        <input type="password" id="old_password" v-model="old_password" required>
      </div>
      <div>
        <label for="new_password1">새 비밀번호</label>
        <input type="password" id="new_password1" v-model="new_password1" required>
      </div>
      <div>
        <label for="new_password2">새 비밀번호 확인</label>
        <input type="password" id="new_password2" v-model="new_password2" required>
      </div>
      <button type="submit">비밀번호 변경</button>
    </form>
  </div>
</template>

<script setup>

import { ref } from 'vue'
import { useProfileStore } from '@/stores/profile';

const profilestore = useProfileStore()

const old_password = ref(null)
const new_password1 = ref(null)
const new_password2 = ref(null)

const updatePassword = function () {
  if (new_password1.value === new_password2.value) {
    const payload = {
      old_password: old_password.value,
      new_password1: new_password1.value,
      new_password2: new_password2.value,
    }
    profilestore.updatePassword(payload)
  } else {
    alert('비밀번호가 일치하지 않습니다.')
  }
}


</script>

<style scoped>

</style>