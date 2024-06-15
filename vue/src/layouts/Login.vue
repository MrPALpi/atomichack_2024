<template>
	<main class="login container content">
		<section class="login__wrapper">
			<slot />
		</section>
		
	</main>
</template>

<style lang="scss" scoped>
.login {
	display: flex;
	align-items: center;
	justify-content: center;
	min-height: 100vh;
}

.login__wrapper {
	
	flex: 0 1 450px;
}

</style
