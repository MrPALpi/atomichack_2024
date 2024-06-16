<script setup>
import Card from 'primevue/card';
import InputText from 'primevue/inputtext';
import Button from 'primevue/button';
import { useUserStore } from '@/stores/user'
const userStore = useUserStore()

const submit = (e) => {
    const formData = Object.fromEntries(new FormData(e.currentTarget));
    userStore.enter(formData);
}
</script>

<template>
    <Card class="login-card">
        <template #title>Авторизация</template>
        <template #content>
            <form @submit.prevent="submit" class="login-form">
                    <InputText class="login-form__input" name="login" type="text" required="true" minlength="3" placeholder="Логин"/>
                    <InputText class="login-form__input" name="password" type="password" required="true" minlength="4" placeholder="Пароль"/>
                <Button type="submit">Войти</Button>
            </form>
        </template>
    </Card>
</template>

<style lang="scss" scoped>

    .login-form {
        margin-top: 30px;
        display: grid;
        gap: 15px;
    }

    .login-form__input {
        width: 100%;
    }
</style>
