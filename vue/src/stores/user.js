import { inject } from 'vue';
import { useRouter } from 'vue-router'
const router = useRouter()
const axios = inject('axios');

export const useUserStore = defineStore('user', () => {
    const login = ref('')
    const isAuth = computed(() => !!login.value.length)


    function setUser(newLogin) {
        login.value = newLogin;
    }

    async function enter(formData) {
        try {
            const response = await axios.post('enter', formData);

            if (response.status === 200) {
                setUser(formData.login);
                router.push('/');
            }
        } catch (e) {
            console.log(e)
        }
    }

    return { login, isAuth, enter }
})