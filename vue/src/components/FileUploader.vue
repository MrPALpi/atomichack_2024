<script setup>
	import Card from 'primevue/card';
	import FileUpload from 'primevue/fileupload';

	import Image from 'primevue/image';
</script>
<template>
	<card>
		<template #content>
			<FileUpload
				name="demo[]"
				:custom-upload="true"
				@uploader="onAdvancedUpload"
				:multiple="true"
				accept="image/*"
				:maxFileSize="10000000"
			>
				<template #empty>
					<p>Drag and drop files to here to upload.</p>
				</template>
			</FileUpload>
		</template>
	</card>
</template>
