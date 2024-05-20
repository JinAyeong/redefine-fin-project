import { ref } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useDepositStore = defineStore('deposit', () => {
  const API_URL = "http://127.0.0.1:8000"

  const depositProducts = ref([])  // 정기예금 상품 목록
  const depositProductOptions = ref([])  // 특정 정기 예금 상품의 옵션 리스트


  // 정기예금 상품 목록, 옵션 DB에 저장
  const saveDeposit = function () {
    axios({
      method: 'get',
      url: `${API_URL}/finances/save-deposit-products/`,
    })
      .then((response) => {
        console.log(response.data)
        console.log('정기예금 상품 목록 DB에 저장')

      })
      .catch((error) => {
        console.log(error)
      })
  }

  // 정기 예금 상품 목록 조회
  const getDeposits = function () {
    axios({
      method: 'get',
      url: `${API_URL}/finances/deposit-products/`,
    })
      .then((response) => {
        depositProducts.value = response.data
        console.log(response.data)
      })
      .catch((error) => {
        console.log(error)
      })
  }




  return { API_URL, depositProducts, depositProductOptions, saveDeposit, getDeposits }
})
