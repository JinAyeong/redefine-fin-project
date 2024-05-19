// src/store/profileStore.js
import { ref, computed, watch } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router'

export const useProfileStore = defineStore('profile', () => {
  const router = useRouter()
  const token = ref(null)
  const API_URL = 'http://127.0.0.1:8000'

  // 로그인 확인
  const isLogin = computed(() => token.value !== null)

  watch(token, () => {
    if (token.value) {
      getProfile()
    } else {
      userProfile.value = null
    }
  })

  // 회원가입
  const signUp = async (payload) => {
    const { username, email, password1, password2, name, age, money, salary } = payload

    try {
      await axios.post(`${API_URL}/accounts/registration/`, {
        username, email, password1, password2, name, age, money, salary
      })
      console.log('회원가입 성공')
      await logIn({ username, password: password1 })
      router.push({ name: 'home' })
    } catch (error) {
      console.error('회원가입 실패:', error)
    }
  }

  // 로그인
  const logIn = async (payload) => {
    const { username, password } = payload

    try {
      const response = await axios.post(`${API_URL}/accounts/login/`, { username, password })
      console.log('로그인 성공!', response.data)
      token.value = response.data.key
      router.push({ name: 'home' })
    } catch (error) {
      console.error('로그인 실패:', error)
    }
  }

  // 로그아웃
  const logOut = async () => {
    try {
      await axios.post(`${API_URL}/accounts/logout/`, {}, {
        headers: { Authorization: `Token ${token.value}` }
      })
      alert('로그아웃 완료!')
      token.value = null
      router.push({ name: 'login' })
    } catch (error) {
      console.error('로그아웃 실패:', error)
    }
  }

  // 유저 profile 가져오기
  const userProfile = ref(null)
  const getProfile = async () => {
    try {
      const response = await axios.get(`${API_URL}/accounts/profile/`, {
        headers: { Authorization: `Token ${token.value}` }
      })
      userProfile.value = response.data
      console.log('프로필 불러오기 성공!', response.data)
    } catch (error) {
      console.error('프로필 불러오기 실패:', error)
    }
  }

  return { API_URL, token, isLogin, signUp, logIn, logOut, userProfile, getProfile }
}, {
  persist: {
    storage: localStorage,
  }
})
