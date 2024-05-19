<template>
    <div>
        <h1>Profile Page</h1>
        <p>아이디 : {{ userProfile.username }}</p>
        <p>이메일 : {{ userProfile.email }}</p>
        <p>이름 : {{ userProfile.name }}</p>
        <p>나이 : {{ userProfile.age }}</p>
        <p>자산 : {{ userProfile.money }}</p>
        <p>연봉 : {{ userProfile.salary }}</p>
        <p v-if="userProfile.financial_products">가입 상품 리스트 : {{ userProfile.financial_products }}</p>
        <p v-else>아직 가입한 상품이 없습니다.</p>
        <button @click="goUpdateProfile">회원정보 수정</button>
        <button>비밀번호 변경</button>
        <button>내가 쓴 글 보기</button>
    </div>
</template>

<script setup>

import { ref } from 'vue'
import { useRouter } from 'vue-router';
import { useProfileStore } from '@/stores/profile';

const router = useRouter()
const profilestore = useProfileStore()
const userProfile = profilestore.userProfile

const goUpdateProfile = function () {
    router.push({name: 'profileupdate'})
}

</script>

<style scoped>

</style>