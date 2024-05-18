import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router'

export const useProfileStore = defineStore('profile', () => {
  const router = useRouter()
  const token = ref(null)
  const API_URL = 'http://127.0.0.1:8000'

  // 로그인 확인
  const isLogin = computed(() => {
    if (token.value === null) {
      return false
    } else {
      return true
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
      router.push({name:'home'})
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
        console.log('로그인 성공!')
        console.log(response.data)
        token.value = response.data.key
        router.push({name:'home'})
      })
      .catch(error => console.log(error))
  }

  return { API_URL, token, signUp, logIn, isLogin }
}, {persist: true})
