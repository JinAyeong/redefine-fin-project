<template>

    <div>
        <body class="d-flex flex-column">
        <main class="flex-shrink-0">
            <!-- Page content-->
            <section class="py-5">
                <div class="container px-5">
                    <!-- Contact form-->
                    <div class="bg-light rounded-3 py-5 px-4 px-md-5 mb-5">
                        <div class="text-center mb-5">
                            <div class="feature bg-primary bg-gradient text-white rounded-3 mb-3"><i class="bi bi-envelope"></i></div>
                            <h1 class="fw-bolder">회원가입</h1>
                            <p class="lead fw-normal text-muted mb-0">맞춤 상품 추천을 위한 가입 정보를 입력해주세요</p>
                        </div>
                        <div class="row gx-5 justify-content-center">
                            <div class="col-lg-8 col-xl-6">
                                <form id="contactForm" data-sb-form-api-token="API_TOKEN" @submit.prevent="signUp">
                                    <!-- username input-->
                                    <div class="form-floating mb-3">
                                        <input class="form-control" v-model.trim="username" id="username" type="text" placeholder="Enter your ID..." data-sb-validations="required" />
                                        <label for="name">ID</label>
                                        <div class="invalid-feedback" data-sb-feedback="name:required">ID is required.</div>
                                    </div>
                                    <!-- Name input-->
                                    <div class="form-floating mb-3">
                                        <input class="form-control" v-model.trim="name" id="name" type="text" placeholder="Enter your name..." data-sb-validations="required" />
                                        <label for="name">Full name</label>
                                        <div class="invalid-feedback" data-sb-feedback="name:required">A name is required.</div>
                                    </div>
                                    <!-- Email address input-->
                                    <div class="form-floating mb-3">
                                        <input class="form-control" v-model.trim="email" id="email" type="email" placeholder="name@example.com" data-sb-validations="required,email" />
                                        <label for="email">Email address</label>
                                        <div class="invalid-feedback" data-sb-feedback="email:required">An email is required.</div>
                                        <div class="invalid-feedback" data-sb-feedback="email:email">Email is not valid.</div>
                                    </div>
                                    <!-- password1 input-->
                                    <div class="form-floating mb-3">
                                        <input class="form-control" v-model.trim="password1" id="password1" type="password" placeholder="Enter your password..." data-sb-validations="required" />
                                        <label for="name">password</label>
                                        <div class="invalid-feedback" data-sb-feedback="name:required">password is required.</div>
                                    </div>
                                    <!-- password2 input-->
                                    <div class="form-floating mb-3">
                                        <input class="form-control" v-model.trim="password2" id="password2" type="password" placeholder="Enter your password confirm..." data-sb-validations="required" />
                                        <label for="name">password confirm</label>
                                        <div class="invalid-feedback" data-sb-feedback="name:required">password confirm is required.</div>
                                    </div>
                                    <!-- age input-->
                                    <div class="form-floating mb-3">
                                        <input class="form-control" v-model.trim="age" id="age" type="number" placeholder="Enter your age..." data-sb-validations="required" />
                                        <label for="name">나이</label>
                                        <div class="invalid-feedback" data-sb-feedback="name:required">age is required.</div>
                                    </div>
                                    <!-- money input-->
                                    <div class="form-floating mb-3">
                                        <input class="form-control" v-model.trim="money" id="money" type="number" placeholder="Enter your money..." data-sb-validations="required" />
                                        <label for="name">자산</label>
                                        <div class="invalid-feedback" data-sb-feedback="name:required">money is required.</div>
                                    </div>
                                    <!-- salary input-->
                                    <div class="form-floating mb-3">
                                        <input class="form-control" v-model.trim="salary" id="salary" type="number" placeholder="Enter your salary..." data-sb-validations="required" />
                                        <label for="name">연봉</label>
                                        <div class="invalid-feedback" data-sb-feedback="name:required">salary is required.</div>
                                    </div>
                                    <!-- Submit success message-->
                                    <!---->
                                    <!-- This is what your users will see when the form-->
                                    <!-- has successfully submitted-->
                                    <div class="d-none" id="submitSuccessMessage">
                                        <div class="text-center mb-3">
                                            <div class="fw-bolder">회원가입이 성공적으로 이루어졌습니다!</div>
                                            <br />
                                        </div>
                                    </div>
                                    <!-- Submit error message-->
                                    <!---->
                                    <!-- This is what your users will see when there is-->
                                    <!-- an error submitting the form-->
                                    <div class="d-none" id="submitErrorMessage"><div class="text-center text-danger mb-3">Error sending message!</div></div>
                                    <!-- Submit Button-->
                                    <div class="d-grid"><button class="btn btn-primary btn-lg abled" id="submitButton" type="submit">회원가입</button></div>
                                </form>
                            </div>
                        </div>
                    </div>
                </div>
            </section>
        </main>
    </body>
    </div>














    <!-- <div>
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
            <input type="submit" value="SignUp">
        </form>
    </div> -->
</template>

<script setup>
import {ref} from 'vue'
import { useProfileStore } from '@/stores/profile.js'

const store = useProfileStore()

const username = ref(null)
const email = ref(null)
const password1 = ref(null)
const password2 = ref(null)
const name = ref(null)
const age = ref(null)
const money = ref(null)
const salary = ref(null)

const signUp = function () {
  const payload = {
    username: username.value,
    email : email.value,
    password1: password1.value,
    password2: password2.value,
    name : name.value,
    age: age.value,
    money: money.value,
    salary: salary.value
  }
  store.signUp(payload)
}
</script>

<style scoped>

</style>