<template>

<div>
        <body class="d-flex flex-column">
        <main class="flex-shrink-0">
            <!-- Page content-->
            <section class="py-5">
                <div class="container px-5">
                    <!-- Contact form-->
                    <div class="bg-light rounded-3 py-5 px-4 px-md-5 mb-5" style="width: 70%; margin: auto;">
                        <div class="text-center mb-5">
                            <div class="feature bg-primary bg-gradient text-white rounded-3 mb-3"><i class="bi bi-envelope"></i></div>
                            <h1 class="fw-bolder">회원정보 수정</h1>
                            <p class="lead fw-normal text-muted mb-0">맞춤 상품 추천을 위한 가입 정보를 수정해주세요</p>
                        </div>
                        <div class="row gx-5 justify-content-center">
                            <div class="col-lg-8 col-xl-6">
                                <form id="contactForm" data-sb-form-api-token="API_TOKEN" @submit.prevent="profileUpdate">
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
                                    <div class="d-grid"><button class="btn btn-primary btn-lg abled" id="submitButton" type="submit">회원 정보 수정</button></div>
                                </form>
                                <div class="d-grid"><button @click="profilestore.signOut" class="btn btn-outline-primary btn-lg abled" id="submitButton" type="submit">회원 탈퇴</button></div>
                            </div>
                        </div>
                    </div>
                </div>
            </section>
        </main>
    </body>
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