import { createRouter, createWebHistory } from 'vue-router'
import { layoutTypes } from '../layouts/layoutTypes'
import { layoutMiddleware } from './middleware/layoutMiddleware'

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: '/',
            name: 'Check',
            component: () => import('../views/Check.vue'),
            meta: {
                layout: layoutTypes.DEFAULT,
            },
        },
        {
            path: '/training',
            name: 'Training',
            component: () => import('../views/Training.vue'),
            meta: {
                layout: layoutTypes.DEFAULT,
            },
        },
        {
            path: '/auth',
            name: 'Auth',
            component: () => import('../views/Auth.vue'),
            meta: {
                layout: layoutTypes.LOGIN,
            },
        }
    ]
})


router.beforeEach(layoutMiddleware);

export default router
