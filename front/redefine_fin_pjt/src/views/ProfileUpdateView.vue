<template>
    <div>
        <h1>회원정보 수정</h1>
        <form @submit.prevent="profileUpdate">
            <p>username : {{ userProfile.username }}</p>
            <div>
                <label for="name">name : </label>
                <input type="text" v-model.trim="name" id="name">
            </div>
            <div>
                <label for="email">email : </label>
                <input type="text" v-model.trim="email" id="email">
            </div>
            <div>
                <label for="age">age : </label>
                <input type="number" v-model.trim="age" id="age">
            </div>
            <div>
                <label for="money">money : </label>
                <input type="number" v-model.trim="money" id="money">
            </div>
            <div>
                <label for="salary">salary : </label>
                <input type="number" v-model.trim="salary" id="salary">
            </div>
            <input type="submit" value="회원정보 수정">
        </form>
        <button @click="profilestore.signOut">회원탈퇴</button>
    </div>
</template>

<script setup>

import { ref } from 'vue'
import { useProfileStore } from '@/stores/profile';

const profilestore = useProfileStore()
const userProfile = profilestore.userProfile

const name = ref(userProfile.name)
const email = ref(userProfile.email)
const age = ref(userProfile.age)
const money = ref(userProfile.money)
const salary = ref(userProfile.salary)

const profileUpdate = function () {
    const payload = {
        name: name.value,
        email: email.value,
        age: age.value,
        money: money.value,
        salary: salary.value
    }
    profilestore.profileUpdate(payload)
}


</script>

<style scoped>

</style>