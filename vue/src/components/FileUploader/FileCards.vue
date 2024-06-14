<script setup>
	import Image from 'primevue/image';
	import Button from 'primevue/button';
	import { defineProps, defineEmits } from 'vue';

	const $props = defineProps({
		value: { type: Array, default: [] },
	});

	const $emit = defineEmits(['removeFile']);
</script>
<template>
	<div class="file-cards">
		<transition-group name="list">
			<div
				v-for="(file, index) of $props.value"
				:key="file.name + file.type + file.size"
				:value="file"
				class="file-cards__item"
			>
				<div class="file-cards__item-remove">
					<Button
						icon="pi pi-times"
						@click="$emit('removeFile', index)"
						size="small"
						severity="danger"
					/>
				</div>

				<Image
					v-if="file.type.split('/')[0] === 'image'"
					role="presentation"
					:alt="file.name"
					:src="file.objectURL"
					width="80px"
					preview
					class="file-cards__item-wrap-img"
					imageClass="file-cards__item-img"
				/>

				<i v-else class="pi pi-file file-cards__item-icon" />
				<div class="file-cards__item-name">{{ file.name }}</div>
			</div>
		</transition-group>
	</div>
</template>

<style lang="scss">
	.file-cards {
		display: flex;
		gap: 10px;
		flex-wrap: wrap;
	}

	.file-cards__item {
		position: relative;
		flex: 0 0 180px;
		padding: 10px;
		border-radius: 5px;
		border: 1px solid var(--p-fileupload-border-color);
		display: flex;
		flex-direction: column;
		align-items: center;
		gap: 10px;
	}

	.file-cards__item-remove {
		position: absolute;
		right: 0;
		top: 0;
		z-index: 2;
	}

	.file-cards__item-wrap-img {
		justify-content: center;
		border-radius: 50%;
		overflow: hidden;
	}

	.file-cards__item-img {
		aspect-ratio: 1 / 1;
		object-fit: cover;
	}

	.file-cards__item-icon {
		font-size: 60px;
	}

	.file-cards__item-name {
		word-break: break-word;
		text-align: center;
	}

	.list-enter-active,
	.list-leave-active {
		transition: all 0.3s ease;
	}

	.list-enter-from,
	.list-leave-to {
		opacity: 0;
		transform: translateY(-30px);
	}
</style>
