<script setup>
import { onMounted, onUnmounted } from "vue";

onMounted(() => {
//eslint-disable-next-line no-console
console.log('auth page', "mounted");
});

onUnmounted(() => {
//eslint-disable-next-line no-console
console.log('auth page', "unmounted");
});
</script>

<template>
    <div>
        Авторизация
    </div>
</template>
