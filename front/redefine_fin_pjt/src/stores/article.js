import { ref } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useArticleStore = defineStore('article', () => {

  const API_URL = 'http://127.0.0.1:8000'
  const articles = ref([])

  // 게시물 리스트 불러오기
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

  return { API_URL, articles, getArticles }
}, { persist: true })
