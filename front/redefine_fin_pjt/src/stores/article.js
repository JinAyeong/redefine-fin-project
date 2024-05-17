import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useProfileStore } from './profile'

export const useArticleStore = defineStore('article', () => {
  const profilestore = useProfileStore()
  const token = profilestore.token
  const API_URL = 'http://127.0.0.1:8000'

  const articles = ref([])

  const getArticles = function () {
    axios({
      method: 'get',
      url: `${API_URL}/articles/`,
    })
      .then(response => {
        articles.value = response.data
        console.log('게시물 불러오기 성공!')
        console.log(articles)
      })
      .catch(error => {
        console.log(error)
      })
  }

  // const createArticle = function (payload) {
  //   const { title, content } = payload

  //   axios({
  //     method: 'post',
  //     url: `${API_URL}/articles/`,
  //     data: {
  //       title: title.value,
  //       content: content.value
  //     },
  //     headers: {
  //       Authorization: `Token ${token}`
  //     }
  //   })
  //     .then(response => {
  //       console.log('게시글 생성 완료!')
  //     })
  //     .catch(error => {
  //       console.log(error)
  //       console.log(token)
  //     })
  // }

  return { API_URL, articles, getArticles }
}, { persist: true })
