import { createRouter, createWebHistory } from 'vue-router'
import { layouts } from '../layouts'

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: '/',
            name: 'Check',
            component: () => import('@/views/Check.vue'),
            meta: {
                layout: layouts.DEFAULT,
            },
        },
        {
            path: '/training',
            name: 'Training',
            component: () => import('@/views/Training.vue'),
            meta: {
                layout: layouts.DEFAULT,
            },
        },
        {
            path: '/result/:id',
            name: 'Result',
            component: () => import('@/views/Result.vue'),
            meta: {
                layout: layouts.DEFAULT,
            },
        },
        {
            path: '/auth',
            name: 'Auth',
            component: () => import('@/views/Auth.vue'),
            meta: {
                layout: layouts.LOGIN,
            },
        },
        {
            path: "/:catchAll(.*)",
            name: "NotFound",
            component: () => import('@/views/Error.vue'),
            meta: {
                layout: layouts.ERROR,
            }
        }
    ]
})

export default router
