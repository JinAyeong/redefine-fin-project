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
                                <h1 class="fw-bolder">로그인</h1>
                                <p class="lead fw-normal text-muted mb-0">회원 정보를 입력해주세요</p>
                            </div>
                            <div class="row gx-5 justify-content-center">
                                <div class="col-lg-8 col-xl-6">
                                    <form id="contactForm" data-sb-form-api-token="API_TOKEN" @submit.prevent="logIn">
                                        <!-- username input-->
                                        <div class="form-floating mb-3">
                                            <input class="form-control" v-model.trim="username" id="username" type="text" placeholder="Enter your ID..." data-sb-validations="required" />
                                            <label for="name">ID</label>
                                            <div class="invalid-feedback" data-sb-feedback="name:required">ID is required.</div>
                                        </div>
                                        <!-- password input-->
                                        <div class="form-floating mb-3">
                                            <input class="form-control" v-model.trim="password" id="password" type="password" placeholder="Enter your password..." data-sb-validations="required" />
                                            <label for="name">password</label>
                                            <div class="invalid-feedback" data-sb-feedback="name:required">password is required.</div>
                                        </div>
                                        <!-- Submit success message-->
                                        <!---->
                                        <!-- This is what your users will see when the form-->
                                        <!-- has successfully submitted-->
                                        <div class="d-none" id="submitSuccessMessage">
                                            <div class="text-center mb-3">
                                                <div class="fw-bolder">로그인이 성공적으로 이루어졌습니다!</div>
                                                <br />
                                            </div>
                                        </div>
                                        <!-- Submit error message-->
                                        <!---->
                                        <!-- This is what your users will see when there is-->
                                        <!-- an error submitting the form-->
                                        <div class="d-none" id="submitErrorMessage"><div class="text-center text-danger mb-3">Error sending message!</div></div>
                                        <!-- Submit Button-->
                                        <div class="d-grid"><button class="btn btn-primary btn-lg abled" id="submitButton" type="submit">로그인</button></div>
                                    </form>
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
