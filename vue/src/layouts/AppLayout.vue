<script setup>
	import { useRoute } from 'vue-router';
	const route = useRoute();
</script>

<template>
	<component :is="route.meta.layoutComponent">
		<slot />
	</component>
</template>
