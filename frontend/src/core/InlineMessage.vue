<template>
  <section class="InlineMessage">
      <img class="InlineMessage__image" :src="messageType" :alt="messageType" />
      <span>{{ message }}</span>
  </section>
</template>
<script setup lang="ts">
import { computed } from 'vue'

interface Props {
  type: string,
  message: string | undefined,
}

const props = defineProps<Props>()

const messageType = computed(() => {
  console.log()
  return props.type === 'error' ? `src/core/errorVocGraph.png` : 'src/core/successVocGraph.jpg'
})
</script>

<style scoped lang="scss">
.InlineMessage {
  display: flex;
  align-items: center;
  justify-content: center;

  &__image {
    width: 60px;
    height: 60px;
  }
}
</style>
