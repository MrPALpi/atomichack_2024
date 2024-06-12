import { defineStore } from 'pinia'
import { inject, ref, computed } from 'vue';
import { useRouter } from 'vue-router'

export const useUserStore = defineStore('user', () => {
    const router = useRouter()
    const axios = inject('axios');
    const login = ref('Иван')
    const isAuth = computed(() => !!login.value.length)


    function setUser(newLogin) {
        login.value = newLogin;
    }

    function exit() {
        setUser('');
        router.push('/auth');
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

    return { login, isAuth, enter, exit }
})