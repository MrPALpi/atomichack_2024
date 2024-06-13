<script setup>
	import FileUpload from 'primevue/fileupload';
	import FileCards from './FileCards.vue';
	import { defineModel } from 'vue';

	const files = defineModel();

	const onSelectedFiles = (event) => {
		files.value = event.files;
	};

	const onRemoveFile = (event) => {
		files.value = event.files;
	};
</script>
<template>
	<FileUpload
		v-bind="$attrs"
		@select="onSelectedFiles"
		@remove="onRemoveFile"
		@clear="files = []"
		class="file-upload"
	>
		<template #content="{ files, removeFileCallback }">
			<file-cards :value="files" @remove-file="removeFileCallback" />
		</template>
		<template #empty>
			<p>Перенесите или выберите файлы для загрузки.</p>
		</template>
	</FileUpload>
</template>
