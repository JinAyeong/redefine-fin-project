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
                    <h1 class="fw-bolder">비밀번호 변경</h1>
                    <p class="lead fw-normal text-muted mb-0">새로운 비밀번호를 입력해주세요</p>
                </div>
                <div class="row gx-5 justify-content-center">
                    <div class="col-lg-8 col-xl-6">
                        <form id="contactForm" data-sb-form-api-token="API_TOKEN" @submit.prevent="updatePassword">
                            <!-- old_password input-->
                            <div class="form-floating mb-3">
                                <input class="form-control" v-model.trim="old_password" id="old_password" type="password" placeholder="Enter your old_password..." data-sb-validations="required" />
                                <label for="name">현재 비밀번호</label>
                                <div class="invalid-feedback" data-sb-feedback="name:required">old_password is required.</div>
                            </div>
                            <!-- password_1 input-->
                            <div class="form-floating mb-3">
                                <input class="form-control" v-model.trim="new_password1" id="password_1" type="password" placeholder="Enter your password_1..." data-sb-validations="required" />
                                <label for="name">새로운 비밀번호</label>
                                <div class="invalid-feedback" data-sb-feedback="name:required">password_1 is required.</div>
                            </div>
                            <!-- password_2 input-->
                            <div class="form-floating mb-3">
                                <input class="form-control" v-model.trim="new_password2" id="password_2" type="password" placeholder="Enter your password_2..." data-sb-validations="required" />
                                <label for="name">새로운 비밀번호 확인</label>
                                <div class="invalid-feedback" data-sb-feedback="name:required">password_2 is required.</div>
                            </div>
                            <!-- Submit success message-->
                            <!---->
                            <!-- This is what your users will see when the form-->
                            <!-- has successfully submitted-->
                            <div class="d-none" id="submitSuccessMessage">
                                <div class="text-center mb-3">
                                    <div class="fw-bolder">비밀번호 변경이 성공적으로 이루어졌습니다!</div>
                                    <br />
                                </div>
                            </div>
                            <!-- Submit error message-->
                            <!---->
                            <!-- This is what your users will see when there is-->
                            <!-- an error submitting the form-->
                            <div class="d-none" id="submitErrorMessage"><div class="text-center text-danger mb-3">Error sending message!</div></div>
                            <!-- Submit Button-->
                            <div class="d-grid"><button class="btn btn-primary btn-lg abled" id="submitButton" type="submit">비밀번호 변경</button></div>
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