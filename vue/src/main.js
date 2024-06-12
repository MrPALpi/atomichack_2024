import { createApp } from 'vue'
import './style.scss'
import App from './App.vue'
import router from './router'
import { createPinia } from 'pinia'
import { axiosInstance } from './plugins/api'
import { PrimeVue, PrimeVueConfig, ToastService } from './plugins/primeVue'

const app = createApp(App)

app.use(router);
app.use(createPinia())
app.provide('axios', axiosInstance);
app.use(PrimeVue, PrimeVueConfig);
app.use(ToastService);
app.mount('#app')
