<template>
  <div>
    <div v-if="loading">Loading...</div>
    <div v-else>
      <!-- <h1>환율 정보</h1>
      <div v-for="exchange_val in exchange_vals" :key="exchange_val.cur_unit">
        <p>통화: {{ exchange_val.cur_nm }} ({{ exchange_val.cur_unit }})</p>
        <p>매매 기준 환율: {{ exchange_val.deal_bas_r }}</p>
        <p>송금 보낼 때: {{ exchange_val.tts }}</p>
        <p>송금 받을 때: {{ exchange_val.ttb }}</p>
      </div> -->
      <div>
        <h2>환율 계산기</h2>
        <div>
          <label for="amount">금액: </label>
          <input type="number" v-model="amount" id="amount" />
        </div>
        <div>
          <label for="filter">필터: </label>
          <select v-model="rate_filter" id="filter">
            <option value="deal_bas_r">매매 기준 환율</option>
            <option value="tts">송금 보낼 때</option>
            <option value="ttb">송금 받을 때</option>
          </select>
        </div>
        <div>
          <label for="from_currency">From: </label>
          <select v-model="from_currency" id="from_currency">
            <option v-for="exchange_val in sortedExchangeVals" :value="exchange_val.cur_unit">
              {{ exchange_val.cur_nm }} ({{ exchange_val.cur_unit }})
            </option>
          </select>
        </div>
        <div>
          <label for="to_currency">To: </label>
          <select v-model="to_currency" id="to_currency">
            <option v-for="exchange_val in sortedExchangeVals" :value="exchange_val.cur_unit">
              {{ exchange_val.cur_nm }} ({{ exchange_val.cur_unit }})
            </option>
          </select>
        </div>
        <button @click="convertCurrency">변환</button>
        <div v-if="result !== null">
          <p>결과: {{ result }} {{ to_currency }} ({{ getCurrencyName(to_currency) }})</p>
        </div>
      </div>
    </div>
  </div>
</template>


<script>
import { ref } from 'vue';
import axios from 'axios';

export default {
  data() {
    return {
      exchange_vals: [], // 데이터를 저장할 배열을 data 속성으로 추가
      loading: false,
      amount: 0,
      from_currency: '',
      to_currency: '',
      result: null,
    };
  },
  // 옵션 오름차순 정렬
  computed: {
    sortedExchangeVals() {
      return this.exchange_vals.slice().sort((a, b) => {
        if (a.cur_nm < b.cur_nm) return -1;
        if (a.cur_nm > b.cur_nm) return 1;
        return 0;
      });
    }
  },
  mounted() {
    this.loading = true;
    // Django API에 GET 요청 보내기
    axios.get('http://127.0.0.1:8000/exchange/')
      .then(res => {
        this.exchange_vals = res.data; // 데이터를 data 속성에 할당
        this.loading = false;
        console.log(this.exchange_vals); // 데이터가 잘 받아와졌는지 확인
      })
      .catch(error => {
        console.error('에러 발생:', error);
        this.loading = false;
      });
  },
  methods: {
    convertCurrency() {
      const fromRate = this.exchange_vals.find(val => val.cur_unit === this.from_currency).deal_bas_r;
      const toRate = this.exchange_vals.find(val => val.cur_unit === this.to_currency).deal_bas_r;
      this.result = ((this.amount * fromRate) / toRate).toFixed(2)
    },
    getCurrencyName(unit) {
      const currency = this.exchange_vals.find(val => val.cur_unit === unit);
      return currency ? currency.cur_nm : '';
    }
  }
};
</script>


<style>
/* 여기에 CSS 스타일링 추가 가능 */
div {
  margin: 10px 0;
}

label {
  margin-right: 10px;
}

input, select {
  margin-bottom: 10px;
}
</style>
