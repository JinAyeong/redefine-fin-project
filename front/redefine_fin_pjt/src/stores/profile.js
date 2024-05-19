import { ref, computed, watch } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router'

export const useProfileStore = defineStore('profile', () => {
  const router = useRouter()
  const token = ref(null)
  const API_URL = 'http://127.0.0.1:8000'
  const userProfile = ref(null)
  const userName = ref(null)

  // 로그인 확인
  const isLogin = computed(() => {
    return token.value !== null
  })

  watch(token, (newToken) => {
    if (newToken) {
      localStorage.setItem('token', newToken)
    } else {
      localStorage.removeItem('token')
    }
  })

  // 회원가입
  const signUp = function(payload) {
    const { username, email, password1, password2, name, age, money, salary } = payload

    axios({
      method : 'post',
      url : `${API_URL}/accounts/registration/`,
      data : {
        username, email, password1, password2, name, age, money, salary
      }
    })
    .then((response) => {
      console.log('회원가입 성공')
      const password = password1
      logIn({username, password})
    })
    .catch((error) => {
      console.log(error)
    })
  }

  // 로그인
  const logIn = function (payload) {
    const { username, password } = payload

    axios({
      method: 'post',
      url: `${API_URL}/accounts/login/`,
      data: {
        username, password
      }
    })
      .then(response => {
        token.value = response.data.key
        userName.value = username
        console.log('로그인 성공!')
        console.log(token.value)
        router.push({name:'home'})
      })
      .catch(error => {
        console.log(error)
      })
  }

  // 로그아웃
  const logOut = function () {
    axios({
      method: 'post',
      url: `${API_URL}/accounts/logout/`,
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
      .then((response) => {
        alert('로그아웃 완료!')
        token.value = null
        userProfile.value = null
        userName.value = null
        localStorage.removeItem('profile')
        router.push({name: 'login'})
      })
      .catch(error => {
        console.log(error)
      })
  }

  // 유저 profile 가져오기
  const getProfile = function () {
    axios({
      method: 'get',
      url: `${API_URL}/accounts/profile/`,
      headers: {
          Authorization: `Token ${token.value}`
      },
    })
      .then((response) => {
        userProfile.value = response.data
        console.log(userProfile.value)
        console.log('프로필 불러오기 성공!')
      })
      .catch((error) => {
        console.log(error)
      })
  }

  return { API_URL, token, userName, isLogin, signUp, logIn, logOut, userProfile, getProfile }
}, {
  persist: true
  // persist: {storage: localStorage}
})
