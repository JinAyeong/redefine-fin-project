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
      console.log(response.data)
      console.log('회원가입 성공')
      const password = password1
      logIn({username, password})
    })
    .catch((error) => {
      console.log(error)
    })
  }

  // 회원탈퇴
  const signOut = function () {
    // 로그아웃 먼저 진행
    if (confirm("정말로 탈퇴하시겠습니까?") == true) {
      axios({
        method: 'post',
        url: `${API_URL}/accounts/logout/`,
        headers: {
          Authorization: `Token ${token.value}`
        }
      })
        .then((response) => {
          console.log(response.data)
        })
        .catch(error => {
          console.log(error)
        })
      // 탈퇴 진행
      axios({
        method: 'delete',
        url: `${API_URL}/accounts/profile/delete/`,
        headers: {
          Authorization: `Token ${token.value}`
        }
      })
        .then((response) => {
          console.log(response.data)
          token.value = null
          userProfile.value = null
          userName.value = null
          // localStorage.removeItem('profile')
          alert('탈퇴가 완료되었습니다')
          router.push({name: 'home'})
        })
        .catch((error) => {
          console.log(error)
        })
    }
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
        getProfile()
        console.log(userProfile.value)
        router.push({name:'home'})
      })
      .catch(error => {
        console.log(error)
      })
  }
  

  // 로그아웃
  const logOut = function () {
    if (confirm("로그아웃 하시겠습니까?") == true) {
    axios({
      method: 'post',
      url: `${API_URL}/accounts/logout/`,
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
      .then((response) => {
        alert('로그아웃 완료!')
        console.log(response.data)
        token.value = null
        userProfile.value = null
        userName.value = null
        // localStorage.removeItem('profile')
        router.push({name: 'login'})
      })
      .catch(error => {
        console.log(error)
      })
  }}

  
  // 회원정보 수정
  const profileUpdate = function (payload) {
    const { name, email, age, money, salary } = payload

    axios({
      method: 'put',
      url: `${API_URL}/accounts/profile/update/`,
      headers: {
        Authorization: `Token ${token.value}`
      },
      data: {
        name, email, age, money, salary
      }
    })
      .then((response) => {
        alert("프로필 수정 완료!")
        console.log(response.data)
        userProfile.value = response.data 
        router.push({name: 'profile'})
      })
      .catch((error) => {
        console.log(error)
      })
  }

  // 비밀번호 수정
  const updatePassword = function (payload) {
    const { old_password, new_password1, new_password2 } = payload;
    
    axios({
      method: "post",
      url: `${API_URL}/accounts/password/change/`,
      headers: {
        Authorization: `Token ${token.value}`,
      },
      data: {
        old_password,
        new_password1,
        new_password2,
      },
    })
      .then((response) => {
        console.log(response.data)
        console.log("비밀번호 변경 성공!");
        alert("비밀번호가 변경되었습니다. 다시 로그인해주세요.")
        logOut()
      })
      .catch((error) => {
        console.log(error)
        alert("비밀번호 변경에 실패했습니다. 다시 시도해 주세요")
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
        console.log('프로필 불러오기 성공!')
      })
      .catch((error) => {
        console.log(error)
      })
  }

  return { API_URL, token, userName, isLogin, signUp, signOut, logIn, logOut, profileUpdate, updatePassword, userProfile, getProfile }
}, {
  persist: true
})