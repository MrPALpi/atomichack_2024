import { defineStore } from 'pinia'
import { inject, ref, computed } from 'vue';
import { useRouter } from 'vue-router'
import * as toast from '@/plugins/toast'

export const useUserStore = defineStore('user', () => {
    const router = useRouter()
    const axios = inject('axios')
    const user = ref({
        id: '1',
        login: 'Ivan'
    })

    const isAuth = computed(() => !!Object.keys(user.value).length);

    const login = computed(() => user.value.login);
    const id = computed(() => user.value.id);


    function setUser(newUser) {
        user.value = newUser
    }

    function exit() {
        setUser('');
        router.push('/auth');
    }

    async function enter(formData) {

        const result = await axios.post('/api/auth/', formData).catch((e) => console.log(e));
        const newUser = result?.data;

        if (!!newUser) {
            setUser(formData);
            router.push('/');
        } else {
            toast.error('Error', 'Неверный логин или пароль');
        }
        


    }

    return { login, id, isAuth, enter, exit }
})