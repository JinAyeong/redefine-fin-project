<template>
<<<<<<< HEAD
    <!-- Header-->
    <header class="bg-dark py-5">
        <div class="container px-5">
            <div class="row gx-5 align-items-center justify-content-center">
                <div class="col-lg-8 col-xl-7 col-xxl-6">
                    <div class="my-5 text-center text-xl-start">
                        <h1 class="display-5 fw-bolder text-white mb-2">Poster</h1>
                        <p class="lead fw-normal text-white-50 mb-4">Quickly design and customize responsive mobile-first sites with Bootstrap, the world’s most popular front-end open source toolkit!</p>
                        <div class="d-grid gap-3 d-sm-flex justify-content-sm-center justify-content-xl-start">
                            <a class="btn btn-primary btn-lg px-4 me-sm-3"  @click="findProduct">상품 추천 바로가기</a>
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
        <div class="col-lg-4 mb-5 mb-lg-0">
          <h2 class="fw-bolder mb-0">redeFINe의 다양한 서비스를 이용해보세요!</h2>
        </div>
        <div class="col-lg-8">
          <div id="featureCarousel" class="carousel slide" data-bs-ride="carousel">
            <div class="carousel-inner">
              <div class="carousel-item active">
                <div class="row gx-5">
                  <div class="col-lg-6 mb-5">
                    <div class="card h-100 shadow border-0">
                      <img class="card-img-top" src="C:\ssafy\redefine-fin-project\front\imgs\productList.png" alt="통합 금융 상품 조회" />
                      <div class="card-body p-4">
                        <a class="text-decoration-none link-dark stretched-link" href="#!">
                          <div class="h5 card-title mb-3">통합 금융 상품 조회</div>
                        </a>
                        <hr>
                        <p class="card-text mb-0">
                          쉽고 편리하게! <br>
                          모든 은행의 금융 상품을 한눈에 모아 볼 수 있는 서비스를 경험하고, 더 나은 금융 결정을 내리세요.
                        </p>
                      </div>
                    </div>
                  </div>
                  <div class="col-lg-6 mb-5">
                    <div class="card h-100 shadow border-0">
                      <img class="card-img-top" src="https://dummyimage.com/600x350/ced4da/6c757d" alt="맞춤 금융 상품 추천" />
                      <div class="card-body p-4">
                        <a class="text-decoration-none link-dark stretched-link" href="#!">
                          <div class="h5 card-title mb-3">맞춤 금융 상품 추천</div>
                        </a>
                        <hr>
                        <p class="card-text mb-0">
                          복잡한 상품 비교는 이제 그만! <br> 우리의 맞춤형 추천 서비스로 시간을 절약하세요. <br>
                          여러분의 금융 상황과 목표에 맞춘 최적의 예적금 상품을 추천해드립니다.
                        </p>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <div class="carousel-item">
                <div class="row gx-5">
                  <div class="col-lg-6 mb-5">
                    <div class="card h-100 shadow border-0">
                      <img class="card-img-top" src="C:\ssafy\redefine-fin-project\front\imgs\AI_chat.png" alt="AI Chatbot" />
                      <div class="card-body p-4">
                        <a class="text-decoration-none link-dark stretched-link" href="#!"> 
                          <div class="h5 card-title mb-3">AI Chatbot</div>
                        </a>
                        <hr>
                        <p class="card-text mb-0">
                          언제 어디서나 궁금한 정보를 물어보세요! <br>
                          최신 AI 기술을 기반으로 한 정확하고 신뢰성 있는 답변을 실시간으로 얻을 수 있습니다.
                        </p>
                      </div>
                    </div>
                  </div>
                  <div class="col-lg-6 mb-5">
                    <div class="card h-100 shadow border-0">
                      <img class="card-img-top" src="https://dummyimage.com/600x350/ced4da/6c757d" alt="지도" />
                      <div class="card-body p-4">
                        <a class="text-decoration-none link-dark stretched-link" href="#!">
                          <div class="h5 card-title mb-3">지도</div>
                        </a>
                        <hr>
                        <p class="card-text mb-0">
                          은행의 위치 정보를 조회해보세요! <br> 전국 모든 은행의 위치를 조회할 수 있습니다.
                        </p>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <div class="carousel-item">
                <div class="row gx-5">
                  <div class="col-lg-6 mb-5">
                    <div class="card h-100 shadow border-0">
                      <img class="card-img-top" src="C:\ssafy\redefine-fin-project\front\imgs\exchange_cal.png" alt="환율 계산기" />
                      <div class="card-body p-4">
                        <a class="text-decoration-none link-dark stretched-link" href="#!">
                          <div class="h5 card-title mb-3">환율 계산기</div>
                        </a>
                        <hr>
                        <p class="card-text mb-0">
                          간편하고 빠른 환율 계산기 서비스를 경험해보세요! <br>
                          실시간 업데이트 되는 환율 정보를 기반으로 원하는 화폐로 환율을 계산합니다.
                        </p>
                      </div>
                    </div>
                  </div>
                  <div class="col-lg-6 mb-5">
                    <div class="card h-100 shadow border-0">
                      <img class="card-img-top" src="C:\ssafy\redefine-fin-project\front\imgs\article.png" alt="후기 게시판" />
                      <div class="card-body p-4">
                        <a class="text-decoration-none link-dark stretched-link" href="#!">
                          <div class="h5 card-title mb-3">후기 게시판</div>
                        </a>
                        <hr>
                        <p class="card-text mb-0">
                          금융 상품 사용자들의 생생한 후기를 들을 수 있습니다. <br>
                          댓글 서비스를 통해 소통할 수 있습니다. 유익한 정보는 저장하여 이용해보세요!
                        </p>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <button class="carousel-control-prev" type="button" data-bs-target="#featureCarousel" data-bs-slide="prev">
              <span class="carousel-control-prev-icon" aria-hidden="true"></span>
              <span class="visually-hidden">Previous</span>
            </button>
            <button class="carousel-control-next" type="button" data-bs-target="#featureCarousel" data-bs-slide="next">
              <span class="carousel-control-next-icon" aria-hidden="true"></span>
              <span class="visually-hidden">Next</span>
            </button>
          </div>
        </div>
      </div>
    </div>
  </section>
=======
  <!-- Header-->
  <header class="bg-dark py-5">
      <div class="container px-5">
          <div class="row gx-5 align-items-center justify-content-center">
              <div class="col-lg-8 col-xl-7 col-xxl-6">
                  <div class="my-5 text-center text-xl-start">
                      <h1 class="display-5 fw-bolder text-white mb-2">Poster</h1>
                      <p class="lead fw-normal text-white-50 mb-4">Quickly design and customize responsive mobile-first sites with Bootstrap, the world’s most popular front-end open source toolkit!</p>
                      <div class="d-grid gap-3 d-sm-flex justify-content-sm-center justify-content-xl-start">
                          <a class="btn btn-primary btn-lg px-4 me-sm-3"  @click="findProduct">상품 추천 바로가기</a>
                      </div>
                  </div>
              </div>
              <div class="col-xl-5 col-xxl-6 d-none d-xl-block text-center"><img class="img-fluid rounded-3 my-5" src="https://dummyimage.com/600x400/343a40/6c757d" alt="..." /></div>
          </div>
      </div>
  </header>
>>>>>>> eb29c167b3a29165720d5f30f097b23e6223cef3
  
  
  <!-- Features section-->
  <section class="py-5" id="features">
      <div class="container px-5 my-5">
          <div class="row gx-5">
              <div class="col-lg-4 mb-5 mb-lg-0"><h2 class="fw-bolder mb-0">redeFINe의 다양한 서비스를 이용해보세요 !</h2></div>
              <div class="col-lg-8">
                  <div class="row gx-5 row-cols-1 row-cols-md-2">
                      <div class="col mb-5 h-100">
                        <div class="col-xl-5 col-xxl-6 d-none d-xl-block text-center"><img class="img-fluid rounded-3 my-5" src="" alt="..." /></div>
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
      <!-- Team members section-->
      <section class="py-5 bg-light">
          <div class="container px-5 my-5">
              <div class="text-center">
                  <h2 class="fw-bolder">Our team</h2>
                  <p class="lead fw-normal text-muted mb-5">"redeFINe" Developers</p>
              </div>
              <div class="row gx-5 row-cols-1 row-cols-sm-2 row-cols-xl-4 justify-content-center">
                  <div class="col mb-5 mb-5 mb-xl-0">
                      <div class="text-center">
                          <img class="img-fluid rounded-circle mb-4 team-img" src="" alt="진아영" />
                          <h5 class="fw-bolder">진아영</h5>
                          <div class="fst-italic text-muted">Jin Ayoung</div>
                      </div>
                  </div>
                  <div class="col mb-5 mb-5 mb-xl-0">
                      <div class="text-center">
                          <img class="img-fluid rounded-circle mb-4 team-img" src="../../../imgs/IMG_0707.jpg" alt="홍수인" />
                          <h5 class="fw-bolder">홍수인</h5>
                          <div class="fst-italic text-muted">Hong Suin</div>
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
  const router = useRouter();
  
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
  .team-img {
    width: 180px;
    height: 180px;
    object-fit: cover;
  }
  </style>