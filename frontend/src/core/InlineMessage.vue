<template>
  <section class="InlineMessage">
    <img class="InlineMessage__image" :src="messageType" :alt="messageType" />
  </section>
</template>
<script setup lang="ts">
import { computed } from 'vue'

interface Props {
  type: string
}

const props = defineProps<Props>()

const messageType = computed(() => {
  console.log()
  return props.type === 'error' ? `src/core/errorVocGraph.png` : 'src/core/successVocGraph.jpg'
})
</script>

<style scoped lang="scss">
.InlineMessage {
  &__image {
    width: 60px;
    height: 60px;
  }
}
</style>
