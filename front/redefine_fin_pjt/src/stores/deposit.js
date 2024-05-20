import { ref } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useDepositStore = defineStore('deposit', () => {
  const API_URL = "http://127.0.0.1:8000"

  const saving_products = ref([])  // 정기예금 상품 목록

  // 정기예금 상품 목록, 옵션 DB에 저장
  const saveDeposit = function () {
    axios({
      method: 'get',
      url: `${API_URL}/finances/save-deposit-products/`,
    })
      .then((response) => {
        console.log(response.data)
        // saving_products.value = response.data
        console.log('정기예금 상품 목록 DB에 저장')

      })
      .catch((error) => {
        console.log(error)
      })
  }

  // 정기 예금 상품 목록 조회
  const getDeposit = function () {
    axios({
      method: 'get',
      url: `${API_URL}/finances/deposit_products`,
    })
      .then((response) => {
        saving_products.value = response.data
        console.log(response.data)
      })
      .catch((error) => {
        console.log(error)
      })
  }


  return { saving_products, saveDeposit, getDeposit }
})
