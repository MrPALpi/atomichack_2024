import { createRouter, createWebHistory } from 'vue-router'
// import { layoutTypes } from '../layouts/layoutTypes'
// import { layoutMiddleware } from './middleware/layoutMiddleware'
import {types} from '../layouts'

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: '/',
            name: 'Check',
            component: () => import('../views/Check.vue'),
            meta: {
                layout: types.DEFAULT,
            },
        },
        {
            path: '/training',
            name: 'Training',
            component: () => import('../views/Training.vue'),
            meta: {
                layout: types.DEFAULT,
            },
        },
        {
            path: '/auth',
            name: 'Auth',
            component: () => import('../views/Auth.vue'),
            meta: {
                layout: types.LOGIN,
            },
        },
        {
            path: "/:catchAll(.*)",
            name: "NotFound",
            component: () => import('../views/Error.vue'),
            meta: {
                layout: types.ERROR,
            }
        }
    ]
})

export default router
