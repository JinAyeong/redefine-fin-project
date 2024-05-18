<template>
  <div>
    <div>
      <h1>🔍 주변 은행 검색</h1>
    </div>
    <div class="content-map">
      <form @submit.prevent="search" class="search-form">
        <select
          class="form-select"
          name="location1"
          id="location1"
          v-model="selectedSection"
        >
          <option :value="null" selected hidden>시 / 도 를 선택해주세요</option>
          <option v-for="locate1 in store.sectionList" :value="locate1">
            {{ locate1 }}
          </option>
        </select>
        <select
          class="form-select"
          name="location2"
          id="location2"
          v-model="selectedDetail"
        >
          <option :value="null" selected hidden>
            시 / 군 / 구 를 선택해주세요
          </option>
          <option v-for="locate2 in store.detailList[selectedSection]" :value="locate2">
            {{ locate2 }}
          </option>
        </select>
        <select class="form-select" name="bank" id="bank" v-model="selectedBank">
          <option :value="null" selected hidden>은행을 선택해주세요</option>
          <option v-for="bank in store.banks" :value="bank">
            {{ bank }}
          </option>
        </select>
        검색어 : {{ searchKeyword }} <input class="btn btn-info" type="submit" value="검색" />
      </form>

      <div id="map" style="width: 70%; height: 600px"></div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from "vue";
import { usePlacesStore } from "@/stores/place";

const store = usePlacesStore();

const selectedSection = ref("");
const selectedDetail = ref("");
const selectedBank = ref("");

const API_KEY = '1766462dae4b78aff86eb4373ecb1bc4'

// computed 속성을 사용하여 세 개의 값을 하나의 문자열로 결합
const searchKeyword = computed(() => {
  return `${selectedSection.value} ${selectedDetail.value} ${selectedBank.value}`.trim();
});


onMounted(() => {
  if (window.kakao && window.kakao.maps) {
    initMap();
  } else {
    const script = document.createElement("script");
    /* global kakao */
    script.onload = () => kakao.maps.load(initMap);
    script.src = `http://dapi.kakao.com/v2/maps/sdk.js?autoload=false&appkey=${API_KEY}&libraries=services`;
    document.head.appendChild(script);
  }
});

let ps

const search = () => {
  if (selectedBank.value) {
    // 선택된 은행이 있는 경우에만 검색 수행
    ps.\(searchKeyword.value, placesSearchCB, { useMapBounds: true });
  } else {
    alert("은행을 선택해주세요.");
  }
};

const initMap = () => {
  var mapContainer = document.getElementById('map');
  var mapOption = {
    center: new kakao.maps.LatLng(37.566826, 126.9786567), // 서울시청 좌표
    level: 5 // 지도의 확대 레벨
  };  
  
  var map = new kakao.maps.Map(mapContainer, mapOption); 
  var infowindow = new kakao.maps.InfoWindow({zIndex:1});
  ps = new kakao.maps.services.Places(map); 

  // 검색 결과를 받아와서 마커를 표시하는 콜백함수
  const placesSearchCB = (data, status, pagination) => {
    if (status === kakao.maps.services.Status.OK) {
      for (var i=0; i<data.length; i++) {
        displayMarker(data[i]);    
      }       
    }
  };
    // 키워드로 장소를 검색합니다
    ps.keywordSearch(searchKeyword.value, placesSearchCB); 


  // 마커를 생성하고 지도에 표시하는 함수
  const displayMarker = (place) => {
    var marker = new kakao.maps.Marker({
      map: map,
      position: new kakao.maps.LatLng(place.y, place.x) 
    });

    kakao.maps.event.addListener(marker, 'click', function() {
      infowindow.setContent('<div style="padding:5px;font-size:12px;">' + place.place_name + '</div>');
      infowindow.open(map, marker);
    });
  };
};
</script>

<style scoped>
/* 스타일링 추가 */
</style>