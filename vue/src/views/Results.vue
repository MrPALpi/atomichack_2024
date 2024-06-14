<template>
	<DataTable :value="data" paginator :rows="10" :rowsPerPageOptions="[5, 10, 20, 50]" 
			paginatorTemplate="RowsPerPageDropdown FirstPageLink PrevPageLink CurrentPageReport NextPageLink LastPageLink"
			currentPageReportTemplate="{first} to {last} of {totalRecords}">
		<Column field="date" header="Дата загрузки" sortable>
			<template #body="{ data }">
				{{ humanDate(data.date) }}
			</template>
		</Column>
		<Column field="count" header="Количество файлов" sortable/>
	</DataTable>
</template>

<script setup>
import DataTable from 'primevue/datatable';
import Column from 'primevue/column';
import humanDate from '@/util/humanDate';
import { inject, ref } from 'vue';
import { useRoute } from 'vue-router';

const route = useRoute()
const $axios = inject('axios');
const data = ref([
	{date: Date.now(), count: 1},
	{date: Date.now() + 10000000, count: 2},
	{date: Date.now() + 3000000000, count: 3},
	{date: Date.now() + + 100000000, count: 6},
	{date: Date.now(), count: 73},
	{date: Date.now(), count: 59},
	{date: Date.now(), count: 58},
	{date: Date.now(), count: 75},
	{date: Date.now() + 5000000000, count: 65},
	{date: Date.now(), count: 56},
	{date: Date.now(), count: 52},
	{date: Date.now(), count: 45},
	{date: Date.now() + 7000000000, count: 54},
	{date: Date.now(), count: 55},
	{date: Date.now(), count: 35},
	{date: Date.now(), count: 25},
	{date: Date.now(), count: 51},
	{date: Date.now(), count: 15},
]);



// $axios.get(`/api/task/${route.params.id}/result/meta`).then((req)=>{
    // data.value = req.data
//     console.log(req)
// });


</script>