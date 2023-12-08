<template>
    <ElAlert :class="styleClass" :type="type!" :show-icon="showIcon!" :closable="closable!" :title="titleMessage" :description="message">
        <slot />
    </ElAlert>
</template>

<script lang="ts" setup>
import { ElAlert } from 'element-plus'
import {computed, PropType} from "vue";


type TypeAlert = "success" | "warning" | "error" | "info";

const props = defineProps({
    message: { type: String, required: true },
    showIcon: { type: Boolean, default: true},
    closable: { type: Boolean, default: false },
    title: String,
    type: { type: String as PropType<TypeAlert>, default: "error" }
})

const titleMessage = computed( () => {
    if(props.title) {
        return props.title
    } else {
        return `${props.type} alert`;
    }
})

const styleClass = computed( () => ({
    "VocAlert": props.showIcon
}))
</script>

<style lang="scss" scoped>
.VocAlert {
   margin-bottom: 10px;
}
</style>
