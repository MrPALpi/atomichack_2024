export const types = {
  DEFAULT: 'default',
  LOGIN: 'login',
  ERROR: 'error',
}

export const layouts = {
  'default': () => import('./Default.vue'),
  'login': () => import('./Login.vue'),
  'error': () => import('./Error.vue')
};
