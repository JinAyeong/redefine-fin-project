<template>
  <div>
    <body class="d-flex flex-column">
      <main class="flex-shrink-0">
        <!-- Page content-->
        <section class="py-5">
          <div class="container px-5">
            <!-- Contact form-->
            <div class="bg-light rounded-3 py-5 px-4 px-md-5 mb-5" style="width: 70%; margin: auto;">
              <div class="text-center mb-5">
                <div class="feature bg-primary bg-gradient text-white rounded-3 mb-3"><i class="bi bi-envelope"></i></div>
                <h1 class="fw-bolder">환율 계산기</h1>
                <p class="lead fw-normal text-muted mb-0">원하는 금액을 입력해주세요</p>
              </div>
              <div class="row gx-5 justify-content-center">
                <div class="col-lg-8 col-xl-8">
                  <form id="contactForm" data-sb-form-api-token="API_TOKEN" @submit.prevent="logIn">
                    <div class="filter-btn-group mb-3 row g-0">
                      <button v-for="option in filterOptions" :key="option.value" @click="rate_filter = option.value" :class="{ active: rate_filter === option.value }" class="col btn btn-outline-primary">{{ option.label }}</button> <!-- 변경된 부분 -->
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
                      결과: {{ result }} {{ to_currency }} ({{ getCurrencyName(to_currency) }})
                    </div>
                  </form>
                </div>
              </div>
            </div>
          </div>
        </section>
      </main>
    </body>
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
/* 여기에 CSS 스타일링 추가 가능 */
.input-group {
  margin-bottom: 1.5rem;
}

.input-group-text {
  width: 80px;
}

.feature {
  font-size: 2rem;
}

h1 {
  font-size: 2.5rem;
  margin-bottom: 1rem;
}

p {
  font-size: 1.2rem;
}

.btn-primary {
  font-size: 1.2rem;
  padding: 0.5rem 1rem;
}

.alert {
  font-size: 1.2rem;
}


</style>
