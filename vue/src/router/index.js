import { createRouter, createWebHistory } from 'vue-router'
import { layouts } from '../layouts'
import { middlewareTypes, middleware } from './middlewares'
import { useUserStore } from '@/stores/user'


const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: '/',
            name: 'Check',
            component: () => import('@/views/Check.vue'),
            meta: {
                layout: layouts.DEFAULT,
                middleware: middlewareTypes.AUTH
            },
        },
        {
            path: '/results/:id',
            name: 'Results',
            component: () => import('@/views/Results.vue'),
            meta: {
                layout: layouts.DEFAULT,
                middleware: middlewareTypes.AUTH
            },
        },
        {
            path: '/result/:id',
            name: 'Result',
            component: () => import('@/views/Result.vue'),
            meta: {
                layout: layouts.DEFAULT,
                middleware: middlewareTypes.AUTH
            },
        },
        {
            path: '/auth',
            name: 'Auth',
            component: () => import('@/views/Auth.vue'),
            meta: {
                layout: layouts.LOGIN,
                middleware: middlewareTypes.ENTERED
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


router.beforeEach((to, from, next)=>{
    const $user = useUserStore();
    middleware(to, from, next, $user.isAuth)    
});

export default router
