import { defineStore } from 'pinia'
import { inject, ref, computed } from 'vue';
import { useRouter } from 'vue-router'
import * as toast from '@/plugins/toast'

export const useUserStore = defineStore('user', () => {
    const router = useRouter()
    const axios = inject('axios')
    const user = ref({})

    const isAuth = computed(() => {
        const isAuth = !!user.value.id

        if (isAuth) return isAuth

        setUserFromCookie();

        return !!user.value.id
    });
    const name = computed(() => user.value.name);
    const id = computed(() => user.value.id);
    const isAdmin = computed(() => user.value.is_admin);


    function setUser(newUser) {
        document.cookie = `user=${JSON.stringify(newUser)}; path=/; domain=.${location.hostname};` 
        user.value = newUser
    }

    function exit() {
        setUser({});
        router.push('/auth');
    }

    function setUserFromCookie () {
        const userString = ('; '+document.cookie).split(`; user=`).pop().split(';')[0];
        
        if (!userString) {
            return
        }

        user.value = JSON.parse(userString);
    }

    async function enter(formData) {

        const result = await axios.post('/api/auth/login', formData).catch((e) => console.log(e));
        const newUser = result?.data;

        if (!!newUser) {
            setUser(newUser);
            router.push('/');
        } else {
            toast.error('Error', 'Неверный логин или пароль');
        }
    }

    return { name, id, isAuth, isAdmin, enter, exit }
})