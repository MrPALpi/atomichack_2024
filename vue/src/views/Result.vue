<template>
    <div class="card">
        <DataView :value="products" paginator :rows="10" emptyMessage="Файлы ещё обрабатываются">
            <template #list="slotProps">
                <div class="flex flex-col">
                    <div v-for="(item, index) in slotProps.items" :key="item">
                        
                    </div>
                </div>
            </template>
        </DataView>
    </div>
</template>

<script setup>
import Image from 'primevue/image';
import DataView from 'primevue/dataview';
import { ref, onMounted, inject } from "vue";
import { useRoute } from 'vue-router'

const route = useRoute()
const $axios = inject('axios');
const data = ref();
// console.log(route.params.id);

$axios.get(`/api/task/${route.params.id}/result/meta`).then((req)=>{
    // data.value = req.data
    console.log(req)
});


</script>