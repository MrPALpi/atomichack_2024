<script setup>
    import Chip from 'primevue/chip';
    import { defineProps } from 'vue';
    import { defectColors, defectLocales } from '@/static-data/defects';

    const $props = defineProps({
        value: String
    })
</script>
<template>
    <Chip class="defect-chip">
        <!-- v-show="defectLocales[$props.value]" -->
        <span class="defect-chip__color" :style="`background-color: ${defectColors[$props.value]}`"></span>
        <span class="defect-chip__text">
            {{ defectLocales[$props.value] }}
        </span>
    </Chip>
</template>
<style lang="scss" scoped>
.defect-chip {
    display: flex;
    gap: 10px;
}
.defect-chip__color {
    width: 20px;
    height: 20px;
    border-radius: 50%;
    border: 1px solid var(--p-stone-500)

}
</style>