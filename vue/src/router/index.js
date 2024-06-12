import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: '/',
            name: 'Check',
            component: () => import('../views/Check.vue')
        },
        {
            path: '/training',
            name: 'Training',
            component: () => import('../views/Training.vue')
        },
        {
            path: '/auth',
            name: 'Auth',
            component: () => import('../views/Auth.vue')
        }
    ]
})

export default router
