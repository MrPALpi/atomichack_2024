export const layouts = {
    DEFAULT: { name: 'DEFAULT', component: () => import('./Default.vue') },
    LOGIN: { name: 'LOGIN', component: () => import('./Login.vue') },
    ERROR: { name: 'ERROR', component: () => import('./Error.vue') }
};
