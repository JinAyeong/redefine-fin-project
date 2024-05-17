<template>
    <div>
        <h1>SignUp Page</h1>
        <form @submit.prevent="signUp">
            <div>
                <label for="username">username : </label>
                <input type="text" v-model.trim="username" id="username">
            </div>
            <div>
                <label for="name">name : </label>
                <input type="text" v-model.trim="name" id="name">
            </div>
            <div>
                <label for="email">email : </label>
                <input type="text" v-model.trim="email" id="email">
            </div>
            <div>
                <label for="password1">password : </label>
                <input type="password" v-model.trim="password1" id="password1">
            </div>
            <div>
                <label for="password2">password confirmation : </label>
                <input type="password" v-model.trim="password2" id="password2">
            </div>
            <div>
                <label for="age">age : </label>
                <input type="text" v-model.trim="age" id="age">
            </div>
            <div>
                <label for="money">money : </label>
                <input type="password" v-model.trim="money" id="money">
            </div>
            <div>
                <label for="salary">salary : </label>
                <input type="password" v-model.trim="salary" id="salary">
            </div>
            <input type="submit" value="SignUp">
        </form>
    </div>
</template>

<script setup>
import {ref} from 'vue'

const username = ref(null)
const name = ref(null)
const email = ref(null)
const password1 = ref(null)
const password2 = ref(null)
const age = ref(null)
const money = ref(null)
const salary = ref(null)

const signUp = function () {
  const payload = {
    username: username.value,
    name : name.value,
    email : email.value,
    password1: password1.value,
    password2: password2.value,
    age: age.value,
    money: money.value,
    salary: salary.value
  }
  store.signUp(payload)
}
</script>

<style scoped>

</style>