import PrimeVue from 'primevue/config';
import Aura from 'primevue/themes/aura';
import ToastService from 'primevue/toastservice';

export { PrimeVue, ToastService }

export const PrimeVueConfig = {
    theme: {
        preset: Aura,
        options: {
            prefix: 'p',
            cssLayer: false
        }
    }
}
