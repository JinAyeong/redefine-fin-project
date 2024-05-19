<template>
    <div>
        <h1>Login Page</h1>
        <form @submit.prevent="logIn">
            <label for="username">username : </label>
            <input type="text" v-model.trim="username"><br>
            <label for="password">password : </label>
            <input type="password" v-model.trim="password"><br>
            <input type="submit" value="login">
        </form>
    </div>
</template>

<script setup>

import { ref } from 'vue'
import { useProfileStore } from '@/stores/profile';

const profilestore = useProfileStore()

const username = ref(null)
const password = ref(null)

const logIn = function () {
    const payload = {
        username: username.value,
        password: password.value
    }
    profilestore.logIn(payload)
}

</script>

<style scoped>

</style>