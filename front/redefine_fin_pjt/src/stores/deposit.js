import { ref } from 'vue';
import { defineStore } from 'pinia';
import axios from 'axios';

export const useDepositStore = defineStore('deposit', () => {
  const API_URL = "http://127.0.0.1:8000";

  const depositProducts = ref([]);  // 정기예금 상품 목록
  const depositProductOptions = ref([]);  // 특정 정기 예금 상품의 옵션 리스트
  const savingProducts = ref([]);  // 적금 상품 목록
  const savingProductOptions = ref([]);  // 특정 적금 상품의 옵션 리스트
  const allProducts = ref([])  // 모든 상품 목록

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

  // 정기예금과 적금 상품 목록 조회
  const getAllProducts = async function () {
    allProducts.value = depositProducts.value.concat(savingProducts.value);
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
    API_URL, depositProducts, allProducts, depositProductOptions, savingProducts, savingProductOptions,
    saveDeposit, getDeposits, saveSaving, getSavings, getAllProducts, addFavoriteProduct
  };
});
