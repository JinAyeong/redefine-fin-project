import { ref } from 'vue';
import { defineStore } from 'pinia';
import axios from 'axios';
import { useProfileStore } from './profile';

export const useDepositStore = defineStore('deposit', () => {
  const API_URL = "http://127.0.0.1:8000";
  const profilestore = useProfileStore()

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
      console.log(depositProducts.data);
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
      // console.log(response.data);
    } catch (error) {
      console.log(error);
    }
  };


  // 정기예금과 적금 상품 목록 조회
  const getAllProducts = async function () {
    allProducts.value = depositProducts.value.concat(savingProducts.value);
  }

  // 정기 특정 예금 상품 조회 (filter)
  const getSaving = (params = {}) => {
    axios({
      method: "get",
      url: `${API_URL}/finances/saving-products-filter/`,
      params: params,
    })
      .then((res) => {
        savingProducts.value = res.data;
        // console.log(savingProducts.value)
      })
      .catch((err) => {
        console.log(err);
      });
  };

  // 관심상품 등록
  const addProduct = function (product_cd, option_trm) {
    
    axios({
      method: 'post',
      url: `${API_URL}/accounts/profile/add_product/${product_cd}/${option_trm}`,
      headers: {
        Authorization: `Token ${profilestore.token}`
      },
    })
      .then((response) => {
        console.log(response.data)
        profilestore.getProfile()
      })
      .catch((error) => {
        console.log(error)
      })
  }

  return {
    API_URL, depositProducts, allProducts, depositProductOptions, savingProducts, savingProductOptions, addProduct,
    saveDeposit, getDeposits, saveSaving, getSavings, getAllProducts, getDeposit, getSaving
  };

}, {
  persist: true
  // persist: {storage: localStorage}
})