import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import login from '../views/LoginView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/login',
      name: 'Login',
      component: () => login,
      meta: {
        title: '登录'
      }
    }
  ]
})

router.beforeEach((to, from, next) => {
  document.title = to.meta.title as string
  if (to.name !== 'Login') return next({ name: 'Login' })
  next()
})

export default router
