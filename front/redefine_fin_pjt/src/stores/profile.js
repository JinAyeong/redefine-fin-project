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
      url : `${API_URL}/dj-rest-auth/registration/`,
      data : {
        username, email, password1, password2, name
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

  return { signUp, isLogin }
})
