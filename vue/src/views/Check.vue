<script setup>
	import FileUploader from '@/components/FileUploader/FileUploader.vue';
	import ToggleSwitch from 'primevue/toggleswitch';
	import { shallowRef, computed, inject } from 'vue';
	import { useUserStore } from '@/stores/user';
	import * as toast from '@/plugins/toast'


	const $user = useUserStore();

	const $axios = inject('axios');
	const fileType = shallowRef('image/*');
	const files = shallowRef([]);
	const isActiveSwitch = computed(() => {
		return !!files.value.length;
	});

	const upload = async () => {
		const formData = new FormData();
		const promise = Promise.all(files.value.map(async (file) => {
				if (fileType.value === 'image/*') {
					const res = await $axios.get(file.objectURL, {responseType: 'blob'});
					formData.append('files', res.data);
				} else {
					formData.append('files', file);
				}
			}));

		formData.append('user_id', $user.id);

		promise.then(async ()=>{
			const res = await $axios({
				method: 'post',
				url: '/api/yolo/upload',
				data: formData,
				headers: {
					'Content-Type': `multipart/form-data;`,
				},
			});

			if (res.status === 200) {
				toast.success('Успех', 'Файлы загружены! Результаты скоро будут загружены.');
			}
		})
	}
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
			url="/api/yolo/upload/"
			@uploader="upload"
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
