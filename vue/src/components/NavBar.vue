<script setup>
	import { useUserStore } from '@/stores/user';
	import SplitButton from 'primevue/splitbutton';

	const $user = useUserStore();
</script>
<template>
	<nav class="navbar">
		<div class="navbar__container container">
			<div class="navbar__links">
				<RouterLink class="navbar__link" to="/">Проверка</RouterLink>
				<RouterLink class="navbar__link" :to="{ name: 'Tasks', params: { id: $user.id } }">Результаты</RouterLink>
			</div>
			<div class="navbar__user">
				<SplitButton
					:label="$user.name"
					:model="[
						{
							label: 'Выйти',
							icon: 'pi pi-times',
							command: () => {
								$user.exit();
							},
						},
					]"
				></SplitButton>
			</div>
		</div>
	</nav>
</template>
<style lang="scss" scoped>
	.navbar {
		position: fixed;
		top: 0;
		width: 100%;
		background-color: var(--p-content-background);
		padding: 20px 0;
		z-index: 1;
		border-bottom: 1px solid var(--p-fileupload-border-color);
	}

	.navbar__container {
		display: flex;
		align-items: center;
		justify-content: space-between;
	}

	.navbar__links {
		display: flex;
		gap: 20px;
	}

	.navbar__link {
		position: relative;
	}

	.navbar__link::after {
		position: absolute;
		content: ' ';
		width: 100%;
		display: block;
		height: 2px;
		bottom: -4px;
		background: linear-gradient(
			to right,
			var(--p-primary-color) 50%,
			var(--p-content-background) 50%
		);
		background-size: 200% 100%;
		background-position: right bottom;
		transition: background-position 0.3s ease-in-out;
	}

	.navbar__link.router-link-active::after {
		background-position: left bottom;
	}
</style>
