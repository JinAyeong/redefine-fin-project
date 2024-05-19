import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import SignUpView from '@/views/SignUpView.vue'
import LogInView from '@/views/LogInView.vue'
import ArticleView from '@/views/ArticleView.vue'
import ArticleDetail from '@/views/ArticleDetailView.vue'
import ArticleCreateView from '@/views/ArticleCreateView.vue'
import ArticleUpdateView from '@/views/ArticleUpdateView.vue'
import ProfileView from '@/views/ProfileView.vue'
import ProfileUpdateView from '@/views/ProfileUpdateView.vue'
import BankMapView from '@/views/BankMapView.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    // profile
    {
      path: '/signup',
      name: 'signup',
      component: SignUpView
    },
    {
      path: '/login',
      name: 'login',
      component: LogInView
    },
    {
      path: '/profile',
      name: 'profile',
      component: ProfileView
    },
    {
      path: '/profile/update',
      name: 'profileupdate',
      component: ProfileUpdateView
    },
    // article
    {
      path: '/article',
      name: 'article',
      component: ArticleView
    },
    {
      path: '/article/detail/:id',
      name: 'articledetail',
      component: ArticleDetail
    },
    {
      path: '/article/create',
      name: 'articlecreate',
      component: ArticleCreateView
    },
    {
      path: '/article/update/:id',
      name: 'articleupdate',
      component: ArticleUpdateView
    },
    {
      path: '/bankmap',
      name: 'bankmap',
      component: BankMapView
    },
  ]
})

export default router
