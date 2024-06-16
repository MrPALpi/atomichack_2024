<script setup>
	import Toast from 'primevue/toast';
	import AppLayout from './layouts/AppLayout.vue';
</script>

<template>
	<Toast />
	<app-layout>
		<Suspense>
			<RouterView />
		</Suspense>
	</app-layout>
</template>
