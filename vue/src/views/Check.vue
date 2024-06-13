<script setup>
	import FileUploader from '@/components/FileUploader/FileUploader.vue';
	import ToggleSwitch from 'primevue/toggleswitch';

	import { shallowRef, computed } from 'vue';

	const fileType = shallowRef('image/*');
	const files = shallowRef([]);
	const isActiveSwitch = computed(() => {
		return !!files.value.length;
	});
</script>

<template>
	<section class="page-check">
		<div class="page-check__file-type">
			<toggle-switch
				v-model="fileType"
				:disabled="isActiveSwitch"
				trueValue=".zip"
				falseValue="image/*"
			/>
			<div>Тип файла: {{ fileType }}</div>
		</div>
		<FileUploader
			v-model="files"
			name="demo[]"
			:custom-upload="true"
			:multiple="true"
			:accept="fileType"
			:maxFileSize="10000000"
		/>
	</section>
</template>

<style lang="scss" scoped>
	.page-check {
		display: grid;
		gap: 20px;
	}
	.page-check__file-type {
		display: flex;
		align-items: center;
		gap: 20px;
	}
</style>
