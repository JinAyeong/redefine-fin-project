import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router'

export const useProfileStore = defineStore('profile', () => {
  const token = ref(null)
  const API_URL = 'http://127.0.0.1:8000'

  const isLogin = computed(() => {
    if (token.value === null) {
      return false
    } else {
      return true
    }
  })

  const router = useRouter()

  const signUp = function(payload) {
    const { username, email, password1, password2, name } = payload

    axios({
      method : 'post',
      url : `${API_URL}/accounts/signup/`,
      data : {
        username, email, password1, password2, name, age, money, salary
      }
    })
    .then((response) => {
      console.log('회원가입 성공!')
      // const password = password1
    })
    .catch((error) => {
      console.log(error)
    })
  }

  
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
      })
      .catch(error => console.log(error))
  }

  return { token, signUp, logIn, isLogin }
})
