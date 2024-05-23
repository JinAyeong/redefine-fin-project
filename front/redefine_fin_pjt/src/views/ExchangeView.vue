<template>

  <div class="chat-app">
    <main class="chat-container bg-light">
      <!-- Page Content-->
      <section class="chat-section">
        <div class="container my-5">
          <div class="text-center mb-5">
            <h1 class="fw-bolder">환율 계산기</h1>
            <p class="lead fw-normal text-muted mb-0">원하는 금액을 입력해주세요</p>
          </div>
          <div class="row gx-5 justify-content-center">
                <div class="col-lg-8 col-xl-8">
                  <form id="contactForm" data-sb-form-api-token="API_TOKEN" @submit.prevent="logIn">
                    <div class="filter-btn-group mb-3 row g-0">
                      <button v-for="option in filterOptions" :key="option.value" @click="rate_filter = option.value" :class="{ active: rate_filter === option.value }" class="col btn btn-outline-primary me-1">{{ option.label }}</button> <!-- 변경된 부분 -->
                    </div>
                    <div class="input-group mb-3">
                      <label class="input-group-text" for="from_currency">From</label>
                      <input class="form-control" v-model="amount" id="amount" type="number" placeholder="금액을 입력하세요" data-sb-validations="required" />
                      <select class="form-select" v-model="from_currency" id="from_currency">
                        <option v-for="exchange_val in sortedExchangeVals" :value="exchange_val.cur_unit">
                          {{ exchange_val.cur_nm }} ({{ exchange_val.cur_unit }})
                        </option>
                      </select>
                    </div>
                    <div class="input-group mb-3">
                      <label class="input-group-text" for="to_currency">To</label>
                      <select class="form-select" v-model="to_currency" id="to_currency">
                        <option v-for="exchange_val in sortedExchangeVals" :value="exchange_val.cur_unit">
                          {{ exchange_val.cur_nm }} ({{ exchange_val.cur_unit }})
                        </option>
                      </select>
                      <button @click="convertCurrency" class="btn btn-primary" type="button">계산하기</button>
                    </div>
                    <div v-if="result !== null" class="alert alert-success">
                      {{ result }} {{ to_currency }} ({{ getCurrencyName(to_currency) }})
                    </div>
                  </form>
                </div>
              </div>
        </div>
      </section>
    </main>
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

<style>

.chat-app {
  display: flex;
  flex-direction: column;
  height: 100%;
  justify-content: center;
  align-items: center;
  background-color: #f0f0f0;
  padding: 20px; /* 화면 상하좌우에 여백 추가 */
}

.chat-container {
  width: 100%;
  max-width: 700px; /* 너비를 700px로 늘림 */
  height: 700px; /* 상하 여백을 고려한 높이 */
  display: flex;
  flex-direction: column;
  border: 1px solid #ccc;
  border-radius: 10px;
  overflow: hidden;
  background-color: #ffffff;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  margin: 20px 0; /* 상하 여백 추가 */
}

.chat-section {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  height: 100%;
}

#chat-container {
  display: flex;
  flex-direction: column;
  height: 100%;
}

#chat-messages {
  flex: 1;
  overflow-y: auto;
  padding: 10px;
}

.message {
  max-width: 80%;
  margin: 10px; /* 위아래 여백 추가 */
  padding: 10px;
  border-radius: 20px;
  word-wrap: break-word;
}

.ai-message {
  align-self: flex-start;
  background-color: #e3f2fd;
  color: #1e88e5;
}

.user-message {
  align-self: flex-end;
  background-color: #d1c4e9;
  color: #673ab7;
}

#user-input {
  display: flex;
  align-items: center;
  padding: 10px;
  border-top: 1px solid #ccc;
  background-color: #f1f1f1;
  position: sticky;
  bottom: 0;
  width: 100%;
}

#user-input input {
  flex: 1;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 20px;
  margin-right: 10px;
  outline: none;
}

#user-input button {
  border: none;
  background-color: #1e88e5;
  color: white;
  padding: 10px 20px;
  border-radius: 20px;
  cursor: pointer;
  transition: background-color 0.3s;
}

#user-input button:hover {
  background-color: #1565c0;
}

</style>
