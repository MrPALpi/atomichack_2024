<script setup>
	import { useRoute } from 'vue-router';
	import { defineAsyncComponent, watch, shallowRef } from 'vue';

	import { layouts } from './index.js';

	const route = useRoute();

	const layout = shallowRef(defineAsyncComponent(layouts['DEFAULT'].component));

	watch(
		() => route.meta.layout,
		async (newvalue) => {
			const layoutName = newvalue.component ?? layouts['DEFAULT'].component;
			layout.value = defineAsyncComponent(layoutName);
		}
	);
</script>

<template>
	<component :is="layout">
		<slot />
	</component>
</template>
