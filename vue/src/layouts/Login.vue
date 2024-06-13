<script setup>
	import { onMounted, onUnmounted } from "vue";

onMounted(() => {
    //eslint-disable-next-line no-console
    console.log('login', "mounted");
  });

  onUnmounted(() => {
    //eslint-disable-next-line no-console
    console.log('login', "unmounted");
  });
</script>
<template>
	<main class="login">
		<slot />
	</main>
</template>
