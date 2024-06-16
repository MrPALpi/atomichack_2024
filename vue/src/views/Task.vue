<template>
	<DataTable :value="data" paginator :rows="10" :rowsPerPageOptions="[5, 10, 20, 50]" scrollHeight="calc(100vh - 100px)"
			paginatorTemplate="RowsPerPageDropdown FirstPageLink PrevPageLink CurrentPageReport NextPageLink LastPageLink"
			currentPageReportTemplate="{first} to {last} of {totalRecords}" :loading="loading" :globalFilterFields="['defects']">
            <template #empty>
                Изображений пока нет
            </template>
		<Column field="id" header="Изображения">
			<template #body={data}>
				<Image :src="`/api/attachment/${data.id}`" width="150px" preview/>
			</template>
		</Column>	
		<Column field="defects" header="Дефекты" sortable>
			<template #body="{ data }">
                <div v-if="data.is_processed && data.defects[0] !== null" class="defects">
                    <DefectChip v-for="defect in data.defects" :key="data.id + defect" :value="defect"/>
                </div>
				<div v-else-if="!data.is_processed"class="defects">
                    <Skeleton width="100px" borderRadius="16px"/>
                    <Skeleton width="100px" borderRadius="16px"/>
                    <Skeleton width="100px" borderRadius="16px"/>
                </div>
                <div>
                    Дефекты не найдены
                </div>
			</template>
            <template #filter="{ filterModel, filterCallback }">
                <Select v-model="filterModel.value" @change="filterCallback()" :options="defects" placeholder="Поиск по дефектам" style="min-width: 12rem" :showClear="true">
                    <template #option="slotProps">
                        <Tag :value="slotProps.option" :severity="defectColors(slotProps.option)" />
                    </template>
                </Select>
            </template>
		</Column>
        <Column field="is_processed" header="Статус" :sortable="true" style="width: 10%;">
			<template #body="{ data }">
				<Tag :severity="statusColor(data.is_processed)" :value="statusLocale(data.is_processed)"/>
			</template>
		</Column>
	</DataTable>
</template>

<script setup>
import DataTable from 'primevue/datatable';
import Column from 'primevue/column';
import Tag from 'primevue/tag';
import Image from 'primevue/image';
import Select from 'primevue/select';
import Skeleton from 'primevue/skeleton';
import DefectChip from '@/components/DefectChip.vue';
import { defects, defectColors } from '@/static-data/defects';
import { inject, shallowRef } from 'vue';
import { useRoute } from 'vue-router';

const route = useRoute()
const $axios = inject('axios');
const data = shallowRef([]);
const loading = shallowRef(true)


const statusColor = (status) => status ? 'succes' : 'warn';
const statusLocale = (status) => status ? 'Обработано' : 'В процессе'

$axios.get(`/api/task/${route.params.id}`).then((res)=>{
    data.value = Object.values(res.data.images);
    loading.value=false;
});
</script>

<style lang="scss" scoped>
.defects {
    display: grid;
    gap: 10px;
}
</style>