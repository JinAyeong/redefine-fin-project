import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useProfileStore } from './signup'

export const useArticleStore = defineStore('article', () => {
  const profilestore = useProfileStore()
  const API_URL = profilestore.API_URL
  const token = profilestore.token

  const articles = ref([])

  const getArticles = function () {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/articles/`,
      headers: {
        Authorizations: `Token ${token.value}`
      }
    })
      .then(response => {
        articles.value = response.data
      })
      .catch(error => console.log(error))
  }

  return { token, API_URL, articles, getArticles }
}, { persist: true})
