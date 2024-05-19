<template>
    <div>
      <p>
        {{ comment.username }} 님의 댓글
        <span style="font-size: smaller; color: gray; font-weight: lighter">
          {{ comment.created_at.slice(0, 10) }}
        </span>
      </p>
  
      <p>
        {{ comment.content }}
        <button class="btn" v-if="checkUser" @click="commentId">X</button>
      </p>
  
      <hr />
    </div>
  </template>
  
  <script setup>
  import { defineEmits, defineProps, ref, computed, onMounted } from "vue";
  import { useProfileStore } from "@/stores/sign.js";
  
  const props = defineProps({
    comment: Object,
  });
  
  // 댓글 삭제 : 권한 추가 필요
  
//   const emit = defineEmits(["commentId"]);
//   const commentId = function () {
//     emit("commentId", props.comment.id);
//   };
  
//   // console.log(props.comment.username);
  
//   const user = useProfileStore().username;
  
//   const checkUser = computed(() => {
//     if (props.comment.username == user) {
//       return true;
//     } else {
//       return false;
//     }
//   });
  </script>
  
  <style scoped>
  .btn {
    width: 28px;
    height: 28px;
    border: 1px solid rgba(119, 185, 252, 0.1);
    background-color: rgba(119, 185, 252, 0.2);
    color: rgba(60, 60, 60, 0.4);
    font-weight: bolder;
    padding: 0px 0px 2px 0px;
  }
  </style>