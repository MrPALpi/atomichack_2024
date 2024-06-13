<script setup>
import { useRoute } from 'vue-router';
import { defineAsyncComponent, computed } from 'vue';

import { layouts } from './index.js';

const route = useRoute();
const layout = computed(() => {
	const layoutName = route.meta.layout ?? layouts['DEFAULT'];
	return defineAsyncComponent(layoutName);
})

</script>

<template>
	<component :is="layout">
		<slot />
	</component>
</template>
