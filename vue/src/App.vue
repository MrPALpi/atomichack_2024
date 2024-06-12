<script setup>
	import Toast from 'primevue/toast';
	import AppLayout from './layouts/AppLayout.vue';
	import { inject } from 'vue';

	const axios = inject('axios');

	axios.get('https://jsonplaceholder').then((res) => console.log(res.data));
</script>

<template>
	<Toast />
	<app-layout>
		<RouterView />
	</app-layout>
</template>
