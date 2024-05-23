<template>
  <div>
    <div v-if="loading">Loading...</div>
    <div v-else>
      <div class="exchange-calculator">
        <h2>환율 계산기</h2>
        <div class="input-group">
          <label for="amount">금액: </label>
          <input type="number" v-model="amount" id="amount" />
        </div>
        <div class="input-group">
          <label for="filter">필터: </label>
          <div class="filter-btn-group">
            <button v-for="option in filterOptions" :key="option.value" @click="rate_filter = option.value" :class="{ active: rate_filter === option.value }" class="btn btn-outline-primary">{{ option.label }}</button> <!-- 변경된 부분 -->
          </div>
        </div>
        <div class="input-group">
          <label for="from_currency">From: </label>
          <select v-model="from_currency" id="from_currency" class="form-select"> <!-- 변경된 부분 -->
            <option v-for="exchange_val in sortedExchangeVals" :value="exchange_val.cur_unit">
              {{ exchange_val.cur_nm }} ({{ exchange_val.cur_unit }})
            </option>
          </select>
        </div>
        <div class="input-group">
          <label for="to_currency">To: </label>
          <select v-model="to_currency" id="to_currency" class="form-select"> <!-- 변경된 부분 -->
            <option v-for="exchange_val in sortedExchangeVals" :value="exchange_val.cur_unit">
              {{ exchange_val.cur_nm }} ({{ exchange_val.cur_unit }})
            </option>
          </select>
        </div>
        <button @click="convertCurrency" class="btn btn-primary">변환</button> <!-- 변경된 부분 -->
        <div v-if="result !== null">
          <p>결과: {{ result }} {{ to_currency }} ({{ getCurrencyName(to_currency) }})</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      exchange_vals: [],
      loading: false,
      amount: 0,
      from_currency: '',
      to_currency: '',
      rate_filter: 'deal_bas_r',
      result: null,
      filterOptions: [
        { label: '매매 기준 환율', value: 'deal_bas_r' },
        { label: '송금 보낼 때', value: 'tts' },
        { label: '송금 받을 때', value: 'ttb' }
      ]
    };
  },
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
    this.updateExchangeRates();
  },
  methods: {
    fetchExchangeRates() {
      this.loading = true;
      axios.get('http://127.0.0.1:8000/exchange/')
        .then(res => {
          this.exchange_vals = res.data;
          this.loading = false;
        })
        .catch(error => {
          console.error('에러 발생:', error);
          this.loading = false;
        });
    },
    updateExchangeRates() {
      this.loading = true;
      return axios.get('http://127.0.0.1:8000/exchange/save_rate/')
        .then(res => {
          console.log('환율 정보가 업데이트되었습니다.');
          return this.fetchExchangeRates();
        })
        .catch(error => {
          console.error('환율 정보 업데이트 중 에러 발생:', error);
          this.loading = false;
        });
    },
    convertCurrency() {
      const fromRate = this.exchange_vals.find(val => val.cur_unit === this.from_currency)[this.rate_filter];
      const toRate = this.exchange_vals.find(val => val.cur_unit === this.to_currency)[this.rate_filter];
      this.result = ((this.amount * fromRate) / toRate).toFixed(2);
    },
    getCurrencyName(unit) {
      const currency = this.exchange_vals.find(val => val.cur_unit === unit);
      return currency ? currency.cur_nm : '';
    }
  }
};
</script>

<style scoped>
.exchange-calculator {
  width: 70%;
  margin: auto;
}

.input-group {
  margin-bottom: 1.5rem;
}

.label {
  margin-right: 10px;
}

.filter-btn-group {
  display: flex;
}

.filter-btn-group button {
  margin-right: 10px;
}

.filter-btn-group button.active {
  background-color: #007bff;
  color: #fff;
}
</style>
