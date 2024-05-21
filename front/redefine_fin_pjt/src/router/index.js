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
import FinanceView from '@/views/FinanceView.vue'
import DepositView from '@/views/DepositView.vue'
import DepositDetailView from '@/views/DepositDetailView.vue'
import SavingView from '@/views/SavingView.vue'
import SavingDetailView from '@/views/SavingDetailView.vue'

// exchange
import ExchangeView from '@/views/ExchangeView.vue'

// AI Chat
import AIChatView from '@/views/AIChatView.vue'


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
      path: '/finance',
      name: 'finance',
      component: FinanceView,
      children: [
        {
          path: 'deposit',
          name: 'deposit',
          component: DepositView
        },
        {
          path: 'saving',
          name: 'saving',
          component: SavingView
        }
      ]
    },
    {
      path: '/finance/deposit/:fin_prdt_cd',
      name: 'depositdetail',
      component: DepositDetailView
    },
    {
      path: '/finance/saving/:fin_prdt_cd',
      name: 'savingdetail',
      component: SavingDetailView
    },

    // exchange
    {
      path: '/exchange',
      name: 'exchange',
      component: ExchangeView
    },
    // AI Chat
    {
      path: '/aichat',
      name: 'aichat',
      component: AIChatView
    },
  ]
})

export default router
