import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import router from './router'
import { axiosInstance } from './plugins/api'
import { PrimeVue, PrimeVueConfig, ToastService } from './plugins/primeVue'

const app = createApp(App)

app.use(router);
app.provide('axios', axiosInstance);
app.use(PrimeVue, PrimeVueConfig);
app.use(ToastService);
app.mount('#app')
