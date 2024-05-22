import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useRecommendStore = defineStore('recommend', () => {

  const API_URL = 'http://127.0.0.1:8000'

  const productAuto = ref([])
  
  // 자동 상품 추천
  const recommendAuto = function (token) {
    axios({
      method: 'get',
      url: `${API_URL}/finances/recommend-similar-product/`,
      headers: {
        Authorization: `Token ${token}`
      }
    })
      .then((response) => {
        productAuto.value = response.data
        console.log(productAuto.value.most_common_products)
      })
      .catch(error => {
        console.log(error)
      })
  }

  return { API_URL, productAuto, recommendAuto }
})
