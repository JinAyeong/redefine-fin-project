import { createRouter, createWebHistory } from 'vue-router'

// home
import HomeView from '@/views/HomeView.vue'
// accounts
import SignUpView from '@/views/SignUpView.vue'
import LogInView from '@/views/LogInView.vue'
import ProfileView from '@/views/ProfileView.vue'
import ProfileUpdateView from '@/views/ProfileUpdateView.vue'
import ProfileUpdatePasswordView from '@/views/ProfileUpdatePasswordView.vue'
// article
import ArticleView from '@/views/ArticleView.vue'
import ArticleDetail from '@/views/ArticleDetailView.vue'
import ArticleCreateView from '@/views/ArticleCreateView.vue'
import ArticleUpdateView from '@/views/ArticleUpdateView.vue'
// bankmap
import BankMapView from '@/views/BankMapView.vue'
// deposit
import DepositView from '@/views/DepositView.vue'
import DepositDetailView from '@/views/DepositDetailView.vue'



const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    // accounts
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
    {
      path: '/profile/update/password/',
      name: 'passwordupdate',
      component: ProfileUpdatePasswordView
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
    // bankmap
    {
      path: '/bankmap',
      name: 'bankmap',
      component: BankMapView
    },
    // deposit
    {
      path: '/deposit',
      name: 'deposit',
      component: DepositView
    },
    {
      path: '/deposit/:fin_prdt_cd',
      name: 'depositdetail',
      component: DepositDetailView
    },
  ]
})

export default router
