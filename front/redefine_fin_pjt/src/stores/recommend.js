import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useDepositStore } from './deposit'
import { useProfileStore } from './profile'

import axios from 'axios'

export const useRecommendStore = defineStore('recommend', () => {
  const depositstore = useDepositStore()
  const profilestore= useProfileStore()

  const API_URL = 'http://127.0.0.1:8000'

  const productAuto = ref([])

  const recommendedProducts = computed(() => {
    const products = []
    productAuto.value.forEach(fin_prdt_cd => {      
        const ret = depositstore.depositProducts.find(product => product.fin_prdt_cd === fin_prdt_cd) || depositstore.savingProducts.find(product => product.fin_prdt_cd === fin_prdt_cd)
        if (ret) {
          products.push(ret)
        }
      })
    return products
  })

  
  // 자동 상품 추천
  const recommendAuto = function () {
    axios({
      method: 'get',
      url: `${API_URL}/finances/recommend-similar-product/`,
      headers: {
        Authorization: `Token ${profilestore.token}`
      }
    })
      .then((response) => {
        productAuto.value = response.data.most_common_products
        console.log(response.data)
      })
      .catch(error => {
        console.log(error)
      })
  }

  return { API_URL, productAuto, recommendAuto, recommendedProducts }
})