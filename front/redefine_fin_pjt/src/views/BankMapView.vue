<template>
    <div>
      <div>
        <h1>🔍 주변 은행 검색 🔎</h1>
        <h3> ✅현재 내 주변 은행을 검색해보세요 !  </h3>
      </div>
      <div class="content-map">
        <form class="search-form" @submit.prevent="search">
          <select
            class="form-select"
            name="location1"
            id="location1"
            v-model="mainRegion"
            @change="updateSubRegion"
          >
            <option :value="null" selected hidden>시 / 도 를 선택해주세요</option>
            <option v-for="locate1 in store.sectionList" :value="locate1" :key="locate1">
              {{ locate1 }}
            </option>
          </select>
          <select
            class="form-select"
            name="location2"
            id="location2"
            v-model="subRegion"
          >
            <option :value="null" selected hidden>
              시 / 군 / 구 를 선택해주세요
            </option>
            <option v-for="locate2 in store.detailList[mainRegion]" :value="locate2" :key="locate2">
              {{ locate2 }}
            </option>
          </select>
          <select class="form-select" name="bank" id="bank" v-model="selectedBank">
            <option :value="null" selected hidden>은행을 선택해주세요</option>
            <option v-for="bank in store.banks" :value="bank" :key="bank">
              {{ bank }}
            </option>
          </select>
          <button class="btn btn-info" type="submit">검색</button>
        </form>
        <div id="map" style="width: 70%; height: 600px"></div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from "vue";
  import { usePlacesStore } from "@/stores/place";
  
  const store = usePlacesStore();
  
  const mainRegion = ref(null);
  const subRegion = ref(null);
  const selectedBank = ref(null);
  
  const searchword = ref(null);
  const API_KEY = '1766462dae4b78aff86eb4373ecb1bc4';
  
  const search = () => {
    searchword.value = `${mainRegion.value || ''} ${subRegion.value || ''} ${selectedBank.value || ''}`.trim();
    if (searchword.value.length === 0) {
      alert("지역과 은행을 선택해주세요.");
      return;
    }
  
    // Kakao 지도 API 스크립트 로드
    if (window.kakao && window.kakao.maps) {
      // 이미 kakao 객체가 정의되어 있을 경우 initMap 호출
      initMap(searchword.value);
    } else {
      // kakao 객체가 정의되어 있지 않으면 스크립트 로드
      const script = document.createElement("script");
      script.onload = () => initMap(searchword.value); // 로드 후 initMap 호출
      script.src = `https://dapi.kakao.com/v2/maps/sdk.js?autoload=false&appkey=${API_KEY}&libraries=services`;
      document.head.appendChild(script);
    }
  };
  
  const initMap = (keyword) => {
    // kakao 객체가 정의되어 있는지 확인
    if (typeof kakao === 'undefined' || !kakao.maps) {
      console.error('Kakao 지도 API가 로드되지 않았습니다.');
      return;
    }
  
    kakao.maps.load(() => {
      var infowindow = new kakao.maps.InfoWindow({ zIndex: 1 });
      var mapContainer = document.getElementById("map"),
        mapOption = {
          center: new kakao.maps.LatLng(36.2683, 127.6358), // 대한민국 중심 좌표
          level: 3, // 확대 레벨 
        };
  
      var map = new kakao.maps.Map(mapContainer, mapOption);
      map.setMapTypeId(kakao.maps.MapTypeId.ROADMAP);
      var ps = new kakao.maps.services.Places(map);
      ps.keywordSearch(keyword, placesSearchCB);
  
      function placesSearchCB(data, status, pagination) {
        if (status === kakao.maps.services.Status.OK) {
          var bounds = new kakao.maps.LatLngBounds();
          for (var i = 0; i < data.length; i++) {
            displayMarker(data[i]);
            bounds.extend(new kakao.maps.LatLng(data[i].y, data[i].x));
          }
          map.setBounds(bounds);
        }
      }
  
      function displayMarker(place) {
        var marker = new kakao.maps.Marker({
          map: map,
          position: new kakao.maps.LatLng(place.y, place.x),
        });
  
        kakao.maps.event.addListener(marker, "click", function () {
          infowindow.setContent('<div style="padding:5px;font-size:12px;">' + place.place_name + "</div>");
          infowindow.open(map, marker);
        });
      }
    });
  };
  
  // 페이지가 로드될 때 initMap 호출
  onMounted(() => {
    // 기본 키워드로 초기화
    initMap("은행");
  });
  </script>
  
  <style scoped>
  /* 스타일링 추가 */
  .search-form {
    display: flex;
    align-items: center;
  }
  
  .search-form .form-select {
    margin-right: 10px;
  }
  
  .btn-info {
    background-color: rgb(253, 253, 200);
  }
  </style>
  