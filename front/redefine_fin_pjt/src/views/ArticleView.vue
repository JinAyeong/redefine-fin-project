<template>
	<div>
		 <h1>Article Page</h1>
		 <button @click="router.push({name: 'articlecreate'})">>게시글 작성</button>
		 <ArticleList />
	</div>

</template>

<script setup>

import { useRouter } from 'vue-router'
import ArticleList from '@/components/ArticleList.vue'
const router = useRouter()

</script>

<style scoped>

</style>