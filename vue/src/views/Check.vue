<script setup>
	import FileUploader from '../components/FileUploader.vue';
	import { onMounted, onUnmounted } from "vue";

	onMounted(() => {
    //eslint-disable-next-line no-console
    console.log('check page', "mounted");
  });

  onUnmounted(() => {
    //eslint-disable-next-line no-console
    console.log('check page', "unmounted");
  });
</script>

<template>
	<FileUploader></FileUploader>
	<div>Проверка</div>
</template>
