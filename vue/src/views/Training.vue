<script setup>
import { onMounted, onUnmounted } from "vue";

onMounted(() => {
	//eslint-disable-next-line no-console
	console.log('training page', "mounted");
});

onUnmounted(() => {
	//eslint-disable-next-line no-console
	console.log('training page', "unmounted");
});
</script>

<template>
	<div>Обучение</div>
</template>
