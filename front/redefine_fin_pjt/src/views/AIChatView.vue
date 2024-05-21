<template>
  <body>
    <div id="chat-container">
      <div id="chat-messages">
        <div v-for="(msg, index) in messages" :key="index" class="message">{{ msg.sender }}: {{ msg.content }}</div>
      </div>
      <div id="user-input">
        <input v-model="userMessage" @keyup.enter="sendMessage" type="text" placeholder="# 곧 결혼하는데 좋은 예적금 없을까?" />
        <button @click="sendMessage">전송</button>
      </div>
    </div>
  </body>
</template>

<script setup>
import { ref } from 'vue'

const messages = ref([])
const userMessage = ref('')

const OPENAI_API_KEY='sk-proj-2g7Rsh3XZPbeRzk990wrT3BlbkFJ9PIwHqZEzCv1Jvrk82jP'

async function fetchAIResponse(prompt) {
  const apiEndpoint = 'https://api.openai.com/v1/chat/completions';
  const apiKey = OPENAI_API_KEY;
  let chatHistory = []

  const fixedPrompts = [
    { keywords: ["환율", "환율 정보", "환율 정보 궁금"], response: "redeFINe의 환율 계산기 기능을 이용해보세요!" },
    { keywords: ["예금", "예금 정보", "예금 정보 궁금"], response: "redeFINe의 예금 비교 기능을 이용해보세요!" },
    { keywords: ["적금", "적금 정보", "적금 정보 궁금"], response: "redeFINe의 적금 비교 기능을 이용해보세요!" },
    { keywords: ["주변 은행", "주변 은행 정보", "주변 은행 궁금"], response: "redeFINe의 주변 은행 지도를 이용해보세요!" },
    { keywords: ["예적금 추천", "예적금 추천해줘", "금융 상품 추천"], response: "redeFINe의 금융 상품 추천 서비스를 이용해보세요!" },
    // "제일 예쁜 사람은 누구야?": "사용자가 '제일 예쁜 사람은 누구야?'와 비슷하게 말하면 '제일 예쁜 사람은 홍수인씨인것 같아요'",
    // "예쁜 사람": "사용자가 '예쁜 사람'과 비슷하게 물어하면 '홍수인씨인것 같아요!'",
    // "예쁜 사람에 대해 알려줘": "사용자가 '예쁜 사람에 대해 알려줘'와 비슷하게 말하면 '그것은 홍수인! !'",
    // "제일 알고리즘 잘하는 사람은 누구야?":"사용자가'제일 ~한 천재 or 알고리즘 천재 누구야?'와 비슷하게 말하면 '그건 바로 진아영 님입니다. 역시 A+ 아영님'로 답해주세요.",
    // "차유림이 누구야?": "'차유림이 누구야?'라고 물어보면 '정말 대단하신 분이죠. 이 시대의 킹'",
    // "싸피 강사님에 대해 알려줘": "'싸피 강사님'과 관련해서 물어보면 '싸피의 최고 강사님은 정종윤, 그리고 정현조가 있습니다'",
    // "결혼":"'결혼 예적금 추천'과 비슷하게 물어보면 '결혼을 하면 자금이 많이 필요하기 때문에 높은 금리 혜택이 있는 예적금 상품을 추천해요!'"
]

  let adjustedPrompt = prompt

  if (fixedPrompts[prompt]) {
    adjustedPrompt = fixedPrompts[prompt];
  } else {
    adjustedPrompt = `당신은 금리비교 사이트인 'redeFINe'에서 금융상품을 알려주는 챗봇(은행이 아닙니다). 
    'redeFINe'은 은행별 금융 상품 목록을 조회하고 나와 비슷한 사람들이 많이 가입한 상품을 기준으로 추천해주는 서비스
    다른 사람들의 이야기가 궁금하거나 궁금한 사항이 생기면 게시판 서비스를 이용하여 소통할 수도 있음
    "${prompt}"에 적절히 짧게 답하고, 예적금 상품에 대해서 물어보면 잘 대답해주겠다고 해
      주요 서비스는 환율 계산기, 주변 은행 찾기, 금융 상품 맞춤 추천, 예적금 리스트 조회, 게시판 커뮤니티가 있음
      모든 답변은 100자 이내로
      묻는 말에만 똑바로 대답해
      상품 추천을 원한다면 redeFINe의 예적금 금융상품 추천 서비스를 소개해
      추가로 궁금한 사항은 고객센터 1234-3210 으로 문의하라고 안내해

      `
      
  }

  chatHistory.push({ role: "user", content: adjustedPrompt });

  const requestOptions = {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${apiKey}`
    },
    body: JSON.stringify({
      model: "gpt-3.5-turbo",
      messages: chatHistory,
      temperature: 0.6,
      max_tokens: 300,
      top_p: 1,
      frequency_penalty: 0.5,
      presence_penalty: 0.5,
      stop: ["Human"],
    }),
  };

  try {
    const response = await fetch(apiEndpoint, requestOptions);
    const data = await response.json();
    console.log(data); // 응답을 콘솔에 출력하여 구조 확인

    if (data.choices && data.choices.length > 0) {
      const aiResponse = data.choices[0].message.content;
      chatHistory.push({ role: "assistant", content: aiResponse });
      return aiResponse;
    } else {
      throw new Error('API 응답이 예상한 형식이 아닙니다.');
    }
  } catch (error) {
    console.error('OpenAI API 호출 중 오류 발생:', error);
    return 'OpenAI API 호출 중 오류 발생';
  }
}

function addMessage(sender, message) {
  messages.value.unshift({ sender, content: message });
}

function sendMessage() {
  const message = userMessage.value.trim();
  if (message.length === 0) return;
  
  addMessage('나', message);
  userMessage.value = '';

  fetchAIResponse(message).then(aiResponse => {
    addMessage('챗봇', aiResponse);
  });
}
</script>

<style scoped>
body {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  margin: 0;
}
.message {
  border-top: 1px solid #ccc;
  padding: 10px;
  margin-top: 5px;
  background-color: #e6e6e6;
}
#chat-container {
  width: 400px;
  height: 600px;
  display: flex;
  flex-direction: column;
  border: 1px solid #ccc;
}
#chat-messages {
  flex: 1;
  overflow-y: auto;
  padding: 10px;
  display: flex;
  flex-direction: column-reverse;
}
#user-input {
  display: flex;
  padding: 10px;
}
#user-input input {
  flex: 1;
  padding: 10px;
  outline: none;
}
#user-input button {
  border: none;
  background-color: #1e88e5;
  color: white;
  padding: 10px 15px;
  cursor: pointer;
}
</style>