<template>
	<div>
		 <h1>Article Page</h1>
		 <button @click="router.push({name: 'article_create'})">>게시글 작성</button>
		 <ArticleList />
	</div>

</template>

<script setup>

import { useRouter } from 'vue-router'
const router = useRouter()

import ArticleList from '@/components/ArticleList.vue'

</script>

<style scoped>

</style>