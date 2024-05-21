import { ref } from 'vue';
import { defineStore } from 'pinia';
import axios from 'axios';

export const useDepositStore = defineStore('deposit', () => {
  const API_URL = "http://127.0.0.1:8000";

  const depositProducts = ref([]);  // 정기예금 상품 목록
  const depositProductOptions = ref([]);  // 특정 정기 예금 상품의 옵션 리스트
  const savingProducts = ref([]);  // 적금 상품 목록
  const savingProductOptions = ref([]);  // 특정 적금 상품의 옵션 리스트

  // 정기예금 상품 목록, 옵션 DB에 저장
  const saveDeposit = async function () {
    try {
      const response = await axios.get(`${API_URL}/finances/save-deposit-products/`);
      console.log(response.data);
      console.log('정기예금 상품 목록 DB에 저장');
    } catch (error) {
      console.log(error);
    }
  };

  // 정기 예금 상품 목록 조회
  const getDeposits = async function () {
    try {
      const response = await axios.get(`${API_URL}/finances/deposit-products/`);
      depositProducts.value = response.data;
      console.log(response.data);
    } catch (error) {
      console.log(error);
    }
  };


    // 정기 특정 예금 상품 조회 (filter)
    const getDeposit = (params = {}) => {
      axios({
        method: "get",
        url: `${API_URL}/finances/deposit-products-filter/`,
        params: params,
      })
        .then((res) => {
          depositProducts.value = res.data;
          // console.log(depositProducts.value)
        })
        .catch((err) => {
          console.log(err);
        });
    };

  // 적금 상품 목록, 옵션 DB에 저장
  const saveSaving = async function () {
    try {
      const response = await axios.get(`${API_URL}/finances/save-saving-products/`);
      console.log(response.data);
      console.log('적금 상품 목록 DB에 저장');
    } catch (error) {
      console.log(error);
    }
  };

  // 적금 상품 목록 조회
  const getSavings = async function () {
    try {
      const response = await axios.get(`${API_URL}/finances/saving-products/`);
      savingProducts.value = response.data;
      console.log(response.data);
    } catch (error) {
      console.log(error);
    }
  };

  // 관심 상품 등록
  const addFavoriteProduct = async (product) => {
    try {
      const response = await axios.post(`${API_URL}/user/favorite-products`, product);
      console.log('관심 상품 등록:', response.data);
      return response.data;
    } catch (error) {
      console.log('관심 상품 등록 실패:', error);
      throw error;
    }
  };

  return {
    API_URL, depositProducts, depositProductOptions, savingProducts, savingProductOptions,
    saveDeposit, getDeposits, saveSaving, getSavings, addFavoriteProduct, getDeposit
  };
});
