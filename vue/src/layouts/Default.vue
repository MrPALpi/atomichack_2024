<script setup>
	import NavBar from '../components/NavBar.vue';
	import { onMounted, onUnmounted } from "vue";

	onMounted(() => {
    //eslint-disable-next-line no-console
    console.log('default', "mounted");
  });

  onUnmounted(() => {
    //eslint-disable-next-line no-console
    console.log('default', "unmounted");
  });
</script>

<template>
	<nav-bar></nav-bar>
	<main class="container content">
		<slot />
	</main>
</template>
