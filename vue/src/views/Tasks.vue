<template>
	<DataTable :value="data" paginator :rows="10" :rowsPerPageOptions="[5, 10, 20, 50]"  scrollable scrollHeight="calc(100vh - 100px)"
			paginatorTemplate="RowsPerPageDropdown FirstPageLink PrevPageLink CurrentPageReport NextPageLink LastPageLink"
			currentPageReportTemplate="{first} to {last} of {totalRecords}" :loading="loading">
			<template #empty>
                Загрузок ещё не было
            </template>
		<Column field="link" header="Ссылка" style="width: 5%;">
			<template #body="{ data }">
				<router-link :to="{ name: 'Task', params: { id: data.task_id } }">
					<i class="pi pi-external-link"/>
				</router-link>
			</template>
		</Column>	
		<Column field="date" header="Дата загрузки" :sortable="true">
			<template #body="{ data }">
				{{ humanDate(data.created_date) }}
			</template>
		</Column>
		<Column field="count_src" header="Количество файлов" sortable/>
		<Column field="status" header="Статус" sortable>
			<template #body="{ data }">
				<Tag :severity="statusColorMap[data.status]" :value="statusWordMap[data.status]"/>
			</template>
		</Column>
	</DataTable>
</template>

<script setup>
import DataTable from 'primevue/datatable';
import Column from 'primevue/column';
import Tag from 'primevue/tag';
import humanDate from '@/util/humanDate';
import { inject, ref, shallowRef } from 'vue';
import { useRoute } from 'vue-router';
import { statusColorMap, statusWordMap } from '@/static-data/tasks.js';

const route = useRoute()
const $axios = inject('axios');
const data = ref([]);
const loading = shallowRef(true);


$axios.get(`/api/task/user-task-list?user_id=${route.params.id}`).then((res)=>{
    data.value = res.data
	loading.value=false;
});
</script>

<style lang="scss" scoped>
.pi-external-link {
	font-size: 22px;
}
</style>