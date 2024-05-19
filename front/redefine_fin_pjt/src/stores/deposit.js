import { ref } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useDepositStore = defineStore('deposit', () => {
  const API_URL = "http://127.0.0.1:8000"

  // 정기예금 상품 목록 DB에 저장
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


  return { saveDeposit, }
})
