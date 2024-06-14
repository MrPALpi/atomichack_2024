<script setup>
	import Toast from 'primevue/toast';
	import AppLayout from './layouts/AppLayout.vue';
</script>

<template>
	<Toast />
	<app-layout>
		<RouterView />
	</app-layout>
</template>
