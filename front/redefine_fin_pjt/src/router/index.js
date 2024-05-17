import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import SignUpView from '@/views/SignUpView.vue'
import LogInView from '@/views/LogInView.vue'
import ArticleView from '@/views/ArticleView.vue'
import ArticleCreateView from '@/views/ArticleCreateView.vue'
import ProfileView from '@/views/ProfileView.vue'
import BankMapView from '@/views/BankMapView.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
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
      path: '/article',
      name: 'article',
      component: ArticleView
    },
    {
      path: '/create',
      name: 'create',
      component: ArticleCreateView
    },
    {
      path: '/profile',
      name: 'profile',
      component: ProfileView
    },
    {
      path: '/bankmap',
      name: 'bankmap',
      component: BankMapView
    },
  ]
})

export default router
