<template>
<div>
  <h1>메인페이지</h1>
  <button @click="findProduct">상품 추천받기!</button>
</div>
          <!-- Header-->
          <header class="bg-dark py-5">
              <div class="container px-5">
                  <div class="row gx-5 align-items-center justify-content-center">
                      <div class="col-lg-8 col-xl-7 col-xxl-6">
                          <div class="my-5 text-center text-xl-start">
                              <h1 class="display-5 fw-bolder text-white mb-2">Poster</h1>
                              <p class="lead fw-normal text-white-50 mb-4">Quickly design and customize responsive mobile-first sites with Bootstrap, the world’s most popular front-end open source toolkit!</p>
                              <div class="d-grid gap-3 d-sm-flex justify-content-sm-center justify-content-xl-start">
                                  <a class="btn btn-primary btn-lg px-4 me-sm-3" href="#features">상품 추천 바로가기</a>
                              </div>
                          </div>
                      </div>
                      <!-- <div class="col-xl-5 col-xxl-6 d-none d-xl-block text-center"><img class="img-fluid rounded-3 my-5" src="https://dummyimage.com/600x400/343a40/6c757d" alt="..." /></div> -->
                  </div>
              </div>
          </header>
          
          
          <!-- Features section-->
          <section class="py-5" id="features">
              <div class="container px-5 my-5">
                  <div class="row gx-5">
                      <div class="col-lg-4 mb-5 mb-lg-0"><h2 class="fw-bolder mb-0">reFINe의 다양한 서비스를 이용해보세요 !</h2></div>
                      <div class="col-lg-8">
                          <div class="row gx-5 row-cols-1 row-cols-md-2">
                              <div class="col mb-5 h-100">
                                <div class="col-xl-5 col-xxl-6 d-none d-xl-block text-center"><img class="img-fluid rounded-3 my-5" src="C:\ssafy\redefine-fin-project\front\imgs\map_icon.png" alt="..." /></div>

                                  <!-- <div class="feature bg-primary bg-gradient text-white rounded-3 mb-3"><i class="bi bi-collection"></i></div> -->
                                  <h2 class="h5">통합 금융 상품 조회</h2>
                                  <p class="mb-0">
                                    쉽고 편리하게! 모든 은행의 금융 상품을 한눈에 모아 볼 수 있는 서비스를 경험하고, 
                                    더 나은 금융 결정을 내리세요.
                                  </p>
                              </div>
                              <div class="col mb-5 h-100">
                                  <div class="feature bg-primary bg-gradient text-white rounded-3 mb-3"><i class="bi bi-building"></i></div>
                                  <h2 class="h5">맞춤 금융 상품 추천</h2>
                                  <p class="mb-0">                                    
                                    복잡한 상품 비교는 이제 그만! 우리의 맞춤형 추천 서비스로 시간을 절약하세요.
                                    여러분의 금융 상황과 목표에 맞춘 최적의 예적금 상품을 추천해드립니다.
                                  </p>
                              </div>
                              <div class="col mb-5 mb-md-0 h-100">
                                  <div class="feature bg-primary bg-gradient text-white rounded-3 mb-3"><i class="bi bi-toggles2"></i></div>
                                  <h2 class="h5">AI Chatbot</h2>
                                  <p class="mb-0">
                                    언제 어디서나 궁금한 정보를 물어보세요 !
                                    최신 AI 기술을 기반으로 한 정확하고 신뢰성 있는 답변을 실시간으로 얻을 수 있습니다.
                                  </p>
                              </div>
                              <div class="col mb-5 mb-md-0 h-100">
                                  <div class="feature bg-primary bg-gradient text-white rounded-3 mb-3"><i class="bi bi-toggles2"></i></div>
                                  <h2 class="h5">지도</h2>
                                  <p class="mb-0">
                                    은행의 위치 정보를 조회해보세요! 전국 모든 은행의 위치를 조회할 수 있습니다.
                                  </p>
                              </div>
                              <div class="col mt-5 h-100">
                                  <div class="feature bg-primary bg-gradient text-white rounded-3 mb-3"><i class="bi bi-toggles2"></i></div>
                                  <h2 class="h5">환율 계산기</h2>
                                  <p class="mb-0">간편하고 빠른 환율 계산기 서비스를 경험해보세요! 
                                    실시간 업데이트 되는 환율 정보를 기반으로 원하는 화폐로 환율을 계산합니다.
                                  </p>
                              </div>
                              <div class="col mt-5 h-100">
                                  <div class="feature bg-primary bg-gradient text-white rounded-3 mb-3"><i class="bi bi-toggles2"></i></div>
                                  <h2 class="h5">후기 게시판</h2>
                                  <p class="mb-0">
                                    금융 상품 사용자들의 생생한 후기를 들을 수 있습니다. 
                                    댓글 서비스를 통해 소통할 수 있습니다. 유익한 정보는 저장하여 이용해보세요!
                                  </p>
                              </div>
                          </div>
                      </div>
                  </div>
              </div>
          </section>

</template>

<script setup>

import { onMounted } from 'vue';
import { useDepositStore } from '@/stores/deposit';
import { useRouter } from 'vue-router';

const depositstore = useDepositStore();
const router = useRouter()

if (depositstore.saveDeposit.length === 0) {
  onMounted(async () => {
    await depositstore.saveDeposit();
    await depositstore.saveSaving();
    await depositstore.getDeposits();
    await depositstore.getSavings();
    await depositstore.getAllProducts();
  });
}

const findProduct = function () {
  router.push({name: 'recommend'})
}

</script>

<style scoped>

</style>