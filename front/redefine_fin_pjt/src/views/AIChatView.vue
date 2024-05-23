<template>
  <div class="chat-app">
    <main class="chat-container bg-light">
      <!-- Page Content-->
      <section class="chat-section">
        <div class="container my-5">
          <div class="text-center mb-5">
            <h1 class="fw-bolder">AI Chat</h1>
            <p class="lead fw-normal text-muted mb-0">언제든지 즉각적인 응답을 받아보세요!</p>
          </div>
          <div id="chat-container">
            <div id="chat-messages">
              <div v-for="(msg, index) in messages" :key="index" :class="['message', msg.sender === '챗봇' ? 'ai-message' : 'user-message']">
                <strong>{{ msg.sender }}:</strong> {{ msg.content }}
              </div>
            </div>
          </div>
        </div>
      </section>
      <div id="user-input">
        <input v-model="userMessage" @keyup.enter="sendMessage" type="text" placeholder="메시지를 입력하세요..." />
        <button @click="sendMessage">전송</button>
      </div>
    </main>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const messages = ref([])
const userMessage = ref('')

const OPENAI_API_KEY = 'sk-proj-2g7Rsh3XZPbeRzk990wrT3BlbkFJ9PIwHqZEzCv1Jvrk82jP'

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
  messages.value.push({ sender, content: message });
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
.chat-app {
  display: flex;
  flex-direction: column;
  height: 90vh;
  justify-content: center;
  align-items: center;
  background-color: #f0f0f0;
  padding: 20px; /* 화면 상하좌우에 여백 추가 */
}

.chat-container {
  width: 100%;
  max-width: 700px; /* 너비를 700px로 늘림 */
  height: calc(80vh - 40px); /* 상하 여백을 고려한 높이 */
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
  height: 70%;
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
